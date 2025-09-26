"""Query endpoint for baseball player information."""

import json
from typing import AsyncGenerator
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import StreamingResponse

from baseball_backend.agents.baseball_agent import create_baseball_agent
from baseball_backend.models.player_info import BaseballPlayerInfo
from loguru import logger

router = APIRouter()


@router.get("/query")
async def query_player(
    player_full_name: str = Query(..., description="Full name of the baseball player"),
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
            agent = create_baseball_agent()

            # Stream some initial text about gathering information
            yield f"Gathering information about {player_full_name}...\n\n"

            # Simulate streaming some intermediate results
            yield "Searching baseball database...\n"
            yield "Analyzing player statistics...\n"
            yield "Checking recent performance...\n"
            yield "Compiling comprehensive profile...\n\n"

            # Get the player information
            player_info = await agent.query_player(player_full_name)

            # Stream the final JSON result
            yield json.dumps(player_info.model_dump(), indent=2)

        except Exception as e:
            logger.error(f"Error processing query for {player_full_name}: {e}")
            yield f"Error: {str(e)}"

    return StreamingResponse(
        generate_response(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"},
    )
