"""Baseball agent implementation using OpenAI Agents SDK."""

import json
import os
import re
from pathlib import Path
from typing import Any, Optional
from agents import Agent, WebSearchTool, Runner
from agents.mcp import MCPServerStdio
from loguru import logger

from baseball_backend.models.player_info import BaseballPlayerInfo


class BaseballAgent:
    """AI agent for gathering baseball player information."""

    def __init__(self):
        """Initialize the baseball agent with tools and prompts."""
        # Load prompts from files
        self.system_prompt: str = self._load_prompt("system_prompt.txt")
        self.user_prompt: str = self._load_prompt("user_prompt.txt")

        # Initialize tools
        self.web_search_tool: WebSearchTool = WebSearchTool()

        # Create Supabase MCP server (only if credentials are available)
        self.supabase_server: Optional[MCPServerStdio] = None
        supabase_project_ref = os.getenv("SUPABASE_PROJECT_REF") or os.getenv(
            "SUPABASE_PROJECT_ID"
        )
        supabase_access_token = os.getenv("SUPABASE_ACCESS_TOKEN", "")

        if supabase_project_ref and supabase_access_token:
            try:
                self.supabase_server = MCPServerStdio(
                    name="Supabase Baseball Database",
                    params={
                        "command": "npx",
                        "args": [
                            "-y",
                            "@supabase/mcp-server-supabase@latest",
                            "--read-only",
                            f"--project-ref={supabase_project_ref}",
                        ],
                        "env": {"SUPABASE_ACCESS_TOKEN": supabase_access_token},
                    },
                )
                logger.info(
                    f"Created Supabase MCP server for project: {supabase_project_ref}"
                )
            except Exception as e:
                logger.warning(f"Failed to create Supabase MCP server: {e}")
                self.supabase_server = None
        else:
            logger.info("Supabase credentials not found, proceeding without MCP server")

        # Create the agent with tools only (MCP integration needs more work)
        self.agent: Agent = Agent(
            name="Baseball Information Specialist",
            instructions=self.system_prompt,
            tools=[self.web_search_tool],
        )

        # For test compatibility, expose tools
        self.tools: list[Any] = self.agent.tools
        self.functions: list[Any] = self.agent.tools

        # Track connection status
        self._supabase_connected = False

    def _load_prompt(self, filename: str) -> str:
        """Load a prompt from the prompts directory."""
        prompt_path = Path(__file__).parent.parent / "prompts" / filename
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            logger.warning(f"Prompt file {filename} not found, using default")
            return "You are a helpful baseball information assistant."

    def _create_supabase_mcp_tool(self) -> Optional[MCPServerStdio]:
        """Create a Supabase MCP tool for database access."""
        try:
            supabase_access_token = os.getenv("SUPABASE_ACCESS_TOKEN", "")
            supabase_project_ref = os.getenv("SUPABASE_PROJECT_REF") or os.getenv(
                "SUPABASE_PROJECT_ID"
            )

            if not supabase_access_token:
                logger.warning(
                    "SUPABASE_ACCESS_TOKEN not found in environment variables"
                )
                return None

            if not supabase_project_ref:
                logger.warning(
                    "SUPABASE_PROJECT_REF not found in environment variables"
                )
                return None

            # Create the MCP server for Supabase
            mcp_server = MCPServerStdio(
                params={
                    "command": "npx",
                    "args": [
                        "-y",
                        "@supabase/mcp-server-supabase@latest",
                        "--read-only",
                        f"--project-ref={supabase_project_ref}",
                    ],
                    "env": {
                        "SUPABASE_ACCESS_TOKEN": supabase_access_token,
                    },
                },
            )

            logger.info(
                f"Successfully created Supabase MCP tool for project: {supabase_project_ref}"
            )
            return mcp_server

        except Exception as e:
            logger.error(f"Failed to create Supabase MCP tool: {e}")
            return None

    async def query_player(self, player_name: str) -> BaseballPlayerInfo:
        """Query for comprehensive baseball player information.

        Args:
            player_name: The full name of the baseball player

        Returns:
            BaseballPlayerInfo object with complete player data
        """
        logger.info(f"Starting query for player: {player_name}")

        # Note: MCP server is already configured in the Agent during initialization
        # We don't need to connect here as the Agent framework handles MCP server connections

        # Format the user prompt with the player name
        formatted_prompt = self.user_prompt.format(player_name=player_name)

        # Run the agent with the formatted prompt
        logger.info("Running agent with prompt")
        response = await Runner.run(self.agent, formatted_prompt)

        # Parse the agent response into BaseballPlayerInfo
        # The agent should return structured data that we can parse
        return self._parse_agent_response(response, player_name)

    def _parse_agent_response(
        self, response: Any, player_name: str = "Unknown Player"
    ) -> BaseballPlayerInfo:
        """Parse the agent's response into BaseballPlayerInfo object."""
        try:
            # Extract the text content from the agent response
            if hasattr(response, "content"):
                content = response.content
            elif hasattr(response, "text"):
                content = response.text
            elif hasattr(response, "final_output"):
                content = response.final_output
            else:
                content = str(response)

            logger.info(f"Agent response content: {content[:500]}...")

            # Try to parse as JSON first

            try:
                # Handle cases where response might have extra text around JSON
                content = content.strip()

                # Look for JSON object in the response
                json_start = content.find("{")
                json_end = content.rfind("}") + 1

                if json_start >= 0 and json_end > json_start:
                    json_content = content[json_start:json_end]
                    data = json.loads(json_content)

                    # Validate that we have the required fields
                    if isinstance(data, dict):
                        # Ensure all required fields exist with defaults
                        validated_data = {
                            "history": data.get(
                                "history", f"Information for {player_name}"
                            ),
                            "simple_information": data.get("simple_information", {}),
                            "statistics": data.get("statistics", {}),
                            "games": data.get("games", []),
                        }
                        return BaseballPlayerInfo(**validated_data)
                else:
                    raise json.JSONDecodeError("No JSON object found", content, 0)

            except json.JSONDecodeError as e:
                # If not JSON, try to extract structured information from text
                logger.warning(
                    f"Agent response was not valid JSON ({e}), attempting text parsing"
                )
                return self._parse_text_response(content, player_name)

        except Exception as e:
            logger.error(f"Error parsing agent response: {e}")
            # Return a basic BaseballPlayerInfo for unknown players
            return BaseballPlayerInfo(
                history=f"Unable to retrieve information for {player_name}. Error: {str(e)}",
                simple_information={"full_name": player_name},
                statistics={},
                games=[],
            )

        # Fallback return (should not reach here)
        return BaseballPlayerInfo(
            history=f"Unable to parse response for {player_name}",
            simple_information={"full_name": player_name},
            statistics={},
            games=[],
        )

    def _parse_text_response(
        self, text: str, player_name: str = "Unknown Player"
    ) -> BaseballPlayerInfo:
        """Parse text response into BaseballPlayerInfo when JSON parsing fails."""

        # Try to extract structured information from the agent's response
        history = ""
        simple_information = {}
        statistics = {}
        games = []

        try:
            # Look for history section
            history_match = re.search(
                r"history:\s*(.*?)(?=\n\s*(simple_information|statistics|games|$))",
                text,
                re.DOTALL | re.IGNORECASE,
            )
            if history_match:
                history = history_match.group(1).strip()

            # Look for simple_information section
            simple_match = re.search(
                r"simple_information:\s*(\{.*?\})(?=\n\s*(statistics|games|$))",
                text,
                re.DOTALL | re.IGNORECASE,
            )
            if simple_match:
                try:
                    simple_information = json.loads(simple_match.group(1))
                except json.JSONDecodeError:
                    simple_information = {
                        "note": "Failed to parse simple_information JSON"
                    }

            # Look for statistics section
            stats_match = re.search(
                r"statistics:\s*(\{.*?\})(?=\n\s*(games|$))",
                text,
                re.DOTALL | re.IGNORECASE,
            )
            if stats_match:
                try:
                    statistics = json.loads(stats_match.group(1))
                except json.JSONDecodeError:
                    statistics = {"note": "Failed to parse statistics JSON"}

            # Look for games section
            games_match = re.search(
                r"games:\s*(\[.*?\])", text, re.DOTALL | re.IGNORECASE
            )
            if games_match:
                try:
                    games = json.loads(games_match.group(1))
                except json.JSONDecodeError:
                    games = []

            # If we couldn't extract structured data, fall back to the whole text as history
            if not history and not simple_information and not statistics and not games:
                return BaseballPlayerInfo(
                    history=text[:1000] + "..." if len(text) > 1000 else text,
                    simple_information={"note": "Parsed from text response"},
                    statistics={},
                    games=[],
                )

        except Exception as e:
            logger.warning(f"Error parsing structured text response: {e}")
            return BaseballPlayerInfo(
                history=text[:1000] + "..." if len(text) > 1000 else text,
                simple_information={"note": "Parsed from text response"},
                statistics={},
                games=[],
            )

        return BaseballPlayerInfo(
            history=history,
            simple_information=simple_information,
            statistics=statistics,
            games=games,
        )


def create_baseball_agent() -> BaseballAgent:
    """Factory function to create a configured baseball agent."""
    return BaseballAgent()
