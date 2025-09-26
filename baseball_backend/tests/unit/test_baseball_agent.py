"""Unit tests for the baseball agent."""

import pytest
from baseball_backend.agents.baseball_agent import BaseballAgent, create_baseball_agent
from baseball_backend.models.player_info import BaseballPlayerInfo


class TestBaseballAgent:
    """Test cases for the BaseballAgent class."""

    def test_baseball_agent_initialization(self):
        """Test that BaseballAgent can be initialized."""
        # This test will fail until BaseballAgent is implemented
        agent = BaseballAgent()
        assert agent is not None

    def test_create_baseball_agent_function(self):
        """Test the create_baseball_agent factory function."""
        # This test will fail until create_baseball_agent is implemented
        agent = create_baseball_agent()
        assert agent is not None
        assert hasattr(agent, "tools") or hasattr(agent, "functions")

    def test_agent_has_required_tools(self):
        """Test that the agent has database and web search tools."""
        # This test will fail until agent is properly configured with tools
        agent = create_baseball_agent()
        # Check that agent has access to database and web search functionality
        # This might be through tools attribute or similar
        assert hasattr(agent, "tools") or hasattr(agent, "functions")

    def test_agent_loads_prompts_from_files(self):
        """Test that agent loads system and user prompts from .txt files."""
        # This test will fail until prompt loading is implemented
        agent = BaseballAgent()
        # Should have loaded prompts from prompts/ directory
        assert hasattr(agent, "system_prompt") or hasattr(agent, "prompts")
        assert hasattr(agent, "user_prompt") or hasattr(agent, "prompts")

    @pytest.mark.asyncio
    async def test_agent_query_processing(self):
        """Test that agent can process a player query."""
        # This test will fail until agent query processing is implemented
        agent = create_baseball_agent()
        player_name = "Shohei Ohtani"

        # This should return streaming response or final result
        result = await agent.query_player(player_name)
        assert result is not None

    @pytest.mark.asyncio
    async def test_agent_returns_baseball_player_info(self):
        """Test that agent returns properly formatted BaseballPlayerInfo."""
        # This test will fail until agent returns correct format
        agent = create_baseball_agent()
        player_name = "Shohei Ohtani"

        result = await agent.query_player(player_name)
        assert isinstance(result, BaseballPlayerInfo)
        assert hasattr(result, "history")
        assert hasattr(result, "simple_information")
        assert hasattr(result, "statistics")
        assert hasattr(result, "games")

    @pytest.mark.asyncio
    async def test_agent_handles_unknown_player(self):
        """Test agent behavior with unknown player."""
        # This test will fail until error handling is implemented
        agent = create_baseball_agent()
        player_name = "Unknown Player XYZ"

        result = await agent.query_player(player_name)
        # Should still return BaseballPlayerInfo but with appropriate messaging
        assert isinstance(result, BaseballPlayerInfo)
