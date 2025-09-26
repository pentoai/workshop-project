# Data Model

## BaseballPlayerInfo

This entity represents the comprehensive information about a baseball player, which is the final output of the AI agent.

- **Type**: Pydantic Model

### Fields

| Name                 | Type   | Description                                                          |
| -------------------- | ------ | -------------------------------------------------------------------- |
| `history`            | `str`  | A narrative of the player's career history.                          |
| `simple_information` | `dict` | A dictionary containing basic player details (e.g., team, position). |
| `statistics`         | `dict` | A dictionary of the player's key statistics.                         |
| `games`              | `list` | A list of recent or notable games the player has participated in.    |

### Validation

- Validation is handled by Pydantic at runtime to ensure the agent's output conforms to this structure.
