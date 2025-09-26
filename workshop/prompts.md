# Constitution prompt

```markdown
/constitution

I want to make an application with two main parts: a frontend application using NextJS15 with App router and server actions, using typescript. And a backend using Python and FastAPI, that is going to deliver AI services though the OpenAI Agents SDK.

I want the frontend to:

1. Use tailwindcss for styling
2. Use shadcn for components (include instructions on how to add new shadcn components and how to list available components)
3. Use server actions instead of regular API endpoints
4. Implement tests for all the actions and logic, not the UI components.
5. AVOID test driven development for the frontend, make it way simpler and easier.

I want the backend to:

1. Use python 3.12
2. Use type hints and modern python typing hints (avoid importing stuff from the `typing` python sdk library) Don't do `from typing import List, Dict, Optional` - prefer using `list[x]`, `dict[x, x]` or `x | None`
3. Use FastAPI for the backend api
4. Use OpenAI's Agents SDK for building AI agents (https://openai.github.io/openai-agents-python/)
5. Implement tests using pytest and implement a Test-Driven Development approach.
6. We'll use UV python to manage the dependencies and the project (you should add dependencies using `uv add <package>` or `uv add -d <package>` for development dependencies)
7. Don't over complicate the code with unnecessary abstractions or fallbacks. Assume that failing is normal and you should handle it gracefully at the API level.
```

# Backend development

Some resources:

- [Python UV](https://docs.astral.sh/uv/)
- [OpenAI Agents SDK Python](https://openai.github.io/openai-agents-python/)
- [Supabase MCP](https://github.com/supabase-community/supabase-mcp)
- [OpenAI Agents SDK MCPServerStdio](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio)

## Specify

```markdown
/specify baseball-backend

I want to start by implementing the backend of this application. My objective is to:

0. The backend project is alread initialized in the `baseball_backend` folder.
1. Have a FastAPI API with an endpoint called /query that will receive a baseball player full name
2. Then, we'll start streaming the results of an AI agent developed with the OpenAI Agents SDK framework @OpenAI-Agents (see docs here https://openai.github.io/openai-agents-python/)
3. The agent need to have two main tools: searching inside a database and searching the web.
4. The agent will retrieve information of the given baseball player from the database using a Supabase database MCP where you can get all the tables schemas as needed. The agent will analyze the schema and decide what tables it needs to get extractions and make queries about them. IMPORTANT: the Supabase database is already set up and ready to use, there's no need to create any tables, databases or other resources. You can get all the tables schemas as needed.
5. The agent will search the web for the baseball player to get news, articles, and general information about the player. The agent should use the WebSearchTool to search the web (https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.WebSearchTool)
6. The endpoint should stream the agent's response, not wait for the agent to finish to get the final response.
7. The prompts should be defined outside the python code and defined in .txt files in a "prompts" folder. The agents will load the prompts from the files and put any variables inside using python string formatting.
8. The response format of the agent will be a Pydantic class which will contain all the important information of a baseball player including: history, simple information, statistics, games.
9. There will be no authentication for now
10. If the endpoint fails, return a 500 http error - the client will handle it
11. No worries about rate limits
12. Use loguru for logging and tracking all requests and progress of the requests.
13. Remember to add the python dependencies to the pyproject.toml file using uv add <package> or uv add -d <package> for development dependencies.
14. Remember to use python 3.12 for the backend.
15. You'll use the OpenAI Agents SDK MCPServerStdio class (https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio) to communicate with the OpenAI MCP server with the Supabase database (https://github.com/supabase-community/supabase-mcp).
```

Note: see the branch you're now working!

## Plan

```markdown
/plan Create the plan for this first implementation of the backend
```

## Clarifications

Here we'll see the Agent's plans and see if there's any clarification needed.

We can use the following command in the agent to clarify parts of the plan.

```markdown
/clarify
```

## Tasks

Once every aspect of the plan is clarified, we can create the tasks to be done.

```markdown
/tasks
```

## Implement

We'll implement the phases of the plan iteratively. You'll likely need to iterate on the /implement command a few times and potentially fix a few things manually or prompting the agent to fix specific parts.

```markdown
/implement
```

# Frontend development

## Specify

```markdown
/specify baseball-frontend

Now I want to implement a frontend application in nextJS in the @baseball-frontend/ folder.
The application should have a title "Know your player" title and in the center-left of the application you'll see a input text box to put a player name

You'll use tailwindcss for styling and theing
Use NY Mets blue/orange primary/accent color themes, with light gray for the background.
Use Shadcn components (install them using npx command)
You'll use server actions to communicate with the backend developed in the @main.py (use the /query endpoint to send the player name and stream the results into the application

The results will appear on the center right. While streaming, you'll show all the results and a loading indicator
When it finishes, you'll see the structured output results from @models.py and show the information properly in the frontend.
```
