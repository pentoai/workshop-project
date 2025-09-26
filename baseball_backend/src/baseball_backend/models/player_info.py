"""Pydantic model for baseball player information."""

from pydantic import BaseModel
from typing import Dict, List, Any


class BaseballPlayerInfo(BaseModel):
    """Model representing comprehensive information about a baseball player.

    This model is the final output of the AI agent, containing all gathered
    information about a baseball player including their history, basic info,
    statistics, and notable games.
    """

    history: str
    """A narrative of the player's career history."""

    simple_information: Dict[str, Any]
    """A dictionary containing basic player details (e.g., team, position)."""

    statistics: Dict[str, Any]
    """A dictionary of the player's key statistics."""

    games: List[Dict[str, Any]]
    """A list of recent or notable games the player has participated in."""
