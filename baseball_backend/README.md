# Baseball Backend API

API for querying baseball player information using AI agents with Supabase MCP integration.

## Setup

1. Install dependencies:

   ```bash
   uv install
   ```

2. Set up environment variables:
   Create a `.env` file in the root directory with the following variables:

   ```bash
   # Supabase Configuration (Required)
   SUPABASE_ACCESS_TOKEN=your_supabase_access_token_here
   SUPABASE_PROJECT_REF=your_supabase_project_reference_here

   # OpenAI Configuration (if using OpenAI APIs)
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. Run the server:
   ```bash
   uv run uvicorn src.baseball_backend.main:app --reload
   ```

## Environment Variables

### Required

- `SUPABASE_ACCESS_TOKEN`: Your Supabase access token for database access
- `SUPABASE_PROJECT_REF`: Your Supabase project reference ID
  - Alternative: `SUPABASE_PROJECT_ID` (both are supported)

### Optional

- `OPENAI_API_KEY`: OpenAI API key if using OpenAI models in the agents

## API Endpoints

### GET /query

Query for comprehensive baseball player information.

**Parameters:**

- `player_full_name` (query param): Full name of the baseball player

**Response:**
Returns a streaming response with player information that concludes with a JSON object containing:

- `history`: Career narrative
- `simple_information`: Basic player facts
- `statistics`: Performance metrics
- `games`: Recent notable games

**Example:**

```bash
curl "http://localhost:8000/query?player_full_name=Babe Ruth"
```

## Architecture

The API uses:

- **FastAPI** for the web framework
- **OpenAI Agents SDK** for AI agent orchestration
- **Supabase MCP** for database access
- **Web Search** for supplementary information
- **Loguru** for structured logging

## Development

Run tests:

```bash
uv run pytest
```

The agent system combines:

1. Supabase MCP tool for database queries
2. Web search tool for current information
3. Structured prompts for consistent output formatting
