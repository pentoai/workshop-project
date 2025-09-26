"""Query endpoint for baseball player information."""

import json
from collections.abc import AsyncGenerator
from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse

from baseball_backend.agents.baseball_agent import create_baseball_agent
from loguru import logger

router = APIRouter()


@router.get("/query")
async def query_player(
    player_full_name: str,
):
    """Query for comprehensive baseball player information.

    Returns a streaming response with player information that concludes with a JSON object.

    Args:
        player_full_name: The full name of the baseball player to query

    Returns:
        StreamingResponse with text and JSON data
    """
    logger.info(f"Received query request for player: {player_full_name}")

    async def generate_response() -> AsyncGenerator[str, None]:
        """Generate streaming response with player information."""
        try:
            # Create agent and query player
            logger.info(f"Creating baseball agent for query: {player_full_name}")
            agent = create_baseball_agent()

            # Stream some initial text about gathering information
            yield f"Gathering information about {player_full_name}...\n\n"

            # Provide status updates about the search process
            yield "Searching for baseball player information...\n"
            yield "Querying web sources for player data...\n"
            yield "Gathering career statistics and biographical information...\n"
            yield "Analyzing recent performance and current status...\n"
            yield "Compiling comprehensive player profile...\n\n"

            # Get the player information
            logger.info(f"Querying agent for player: {player_full_name}")
            player_info = await agent.query_player(player_full_name)

            # Log successful query
            logger.info(f"Successfully retrieved information for {player_full_name}")

            # Stream the final JSON result
            yield json.dumps(player_info.model_dump(), indent=2)

        except Exception as e:
            logger.error(f"Error processing query for {player_full_name}: {e}")
            # Return a structured error response
            error_response = {
                "error": True,
                "message": f"Failed to retrieve information for {player_full_name}",
                "details": str(e),
                "player_name": player_full_name,
            }
            yield json.dumps(error_response, indent=2)

    return StreamingResponse(
        generate_response(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"},
    )
