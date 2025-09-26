# Quickstart

This document outlines the steps to test the primary user story for the Baseball Backend API.

## Prerequisites

- The backend server is running.
- `curl` or a similar tool is available.

## Test Scenario

### Query for a Baseball Player

1.  **Execute the following command in your terminal:**

    ```bash
    curl "http://localhost:8000/query?player_full_name=Shohei%20Ohtani"
    ```

2.  **Expected Outcome:**

    - The terminal should begin to stream text-based output from the AI agent.
    - The stream should contain information about Shohei Ohtani, including his history, stats, and recent games.
    - The stream will conclude with a complete JSON object matching the `BaseballPlayerInfo` data model.

### Example Final JSON Output

```json
{
  "history": "Shohei Ohtani is a Japanese professional baseball pitcher...",
  "simple_information": {
    "team": "Los Angeles Dodgers",
    "position": "Pitcher/Designated Hitter"
  },
  "statistics": {
    "batting_average": ".274",
    "home_runs": "171"
  },
  "games": [
    {
      "date": "2025-09-25",
      "opponent": "San Francisco Giants",
      "result": "W 5-3"
    }
  ]
}
```
