# Implementation Plan: Baseball Backend API with AI Agent

**Branch**: `001-the-backend-project` | **Date**: 2025-09-26 | **Spec**: [./spec.md](./spec.md)
**Input**: Feature specification from `/Users/leo/workspace/workshop-03-project-share/specs/001-the-backend-project/spec.md`

## Execution Flow (/plan command scope)

```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from file system structure or context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:

- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary

This plan outlines the implementation of a FastAPI backend that exposes a `/query` endpoint to stream information about a baseball player. An AI agent, built with the OpenAI Agents SDK, will fetch data from a Supabase database and web searches to construct a comprehensive response. The implementation will adhere to the project's constitution, including using Python 3.12, FastAPI, and a TDD approach with `pytest`.

## Technical Context

**Language/Version**: Python 3.12
**Primary Dependencies**: FastAPI, OpenAI Agents SDK, Loguru, uv
**Storage**: Supabase (via MCP)
**Testing**: pytest
**Target Platform**: Linux server
**Project Type**: Web Application (backend only for this feature)
**Performance Goals**: Low-latency streaming response.
**Constraints**: Must use `MCPServerStdio` for agent communication.
**Scale/Scope**: Single endpoint with AI agent integration.

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

| Principle                         | Adherence   | Notes                                                       |
| --------------------------------- | ----------- | ----------------------------------------------------------- |
| 6. Backend Language and Typing    | ✅ Adherent | Project will use Python 3.12 with modern type hints.        |
| 7. Backend Web Framework          | ✅ Adherent | FastAPI is the selected framework.                          |
| 8. Backend AI Integration         | ✅ Adherent | OpenAI Agents SDK will be used.                             |
| 9. Backend Testing Strategy       | ✅ Adherent | A strict TDD approach with `pytest` will be followed.       |
| 10. Backend Dependency Management | ✅ Adherent | `uv` will be used for dependency management.                |
| 11. Backend Code Philosophy       | ✅ Adherent | The design prioritizes simplicity and clear error handling. |

## Project Structure

### Documentation (this feature)

```
specs/001-the-backend-project/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
│   └── openapi.json
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)

```
baseball_backend/
├── src/
│   └── baseball_backend/
│       ├── api/
│       │   └── endpoints/
│       │       └── query.py
│       ├── agents/
│       │   └── baseball_agent.py
│       ├── tools/
│       │   ├── database_tool.py
│       │   └── web_search_tool.py
│       ├── prompts/
│       │   ├── system_prompt.txt
│       │   └── user_prompt.txt
│       ├── models/
│       │   └── player_info.py
│       └── main.py
└── tests/
    ├── integration/
    │   └── test_query_endpoint.py
    └── unit/
        ├── test_baseball_agent.py
        └── tools/
            ├── test_database_tool.py
            └── test_web_search_tool.py
```

**Structure Decision**: The project follows a standard web application backend structure. The feature-specific implementation will be contained within the existing `baseball_backend` directory, organized by functionality (api, agents, tools, models).

## Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:

   - All technical context items are resolved. No further research is needed.

2. **Generate and dispatch research agents**:

   - Not applicable as there are no unresolved unknowns.

3. **Consolidate findings** in `research.md`:
   - A `research.md` file will be created to formally state that no research was necessary as the technical direction is clear from the feature specification and constitution.

**Output**: `research.md` confirming no research was needed.

## Phase 1: Design & Contracts

_Prerequisites: research.md complete_

1. **Extract entities from feature spec** → `data-model.md`:

   - **Entity**: `BaseballPlayerInfo`
   - **Fields**: `history: str`, `simple_information: dict`, `statistics: dict`, `games: list`
   - **Validation**: To be enforced by Pydantic.
   - The output will be a `data-model.md` file detailing this entity.

2. **Generate API contracts** from functional requirements:

   - **Endpoint**: `GET /query`
   - **Request**: Query parameter `player_full_name: str`
   - **Response**: Streaming response of text, concluding with a JSON object matching the `BaseballPlayerInfo` model.
   - An `openapi.json` file will be generated in the `/contracts/` directory.

3. **Generate contract tests** from contracts:

   - A failing contract test will be created to verify the `openapi.json` schema.

4. **Extract test scenarios** from user stories:

   - The primary user story will be translated into an integration test scenario in `quickstart.md`. This will detail the steps to query the endpoint and validate the streamed response.

5. **Update agent file incrementally**:
   - Run `.specify/scripts/bash/update-agent-context.sh cursor`

**Output**: `data-model.md`, `/contracts/openapi.json`, failing tests, `quickstart.md`, agent-specific file

## Phase 2: Task Planning Approach

_This section describes what the /tasks command will do - DO NOT execute during /plan_

**Task Generation Strategy**:

- Load `.specify/templates/tasks-template.md` as base.
- Generate tasks based on the TDD methodology mandated by the constitution.
- For each component in the source code structure, a failing test will be created first, followed by the implementation task.
- Tasks will be created for setting up the FastAPI application, creating the AI agent, developing the database and web search tools, and defining the Pydantic model.

**Ordering Strategy**:

- TDD order: Tests before implementation.
- Dependency order: Models → Tools → Agent → API Endpoint.
- [P] marks tasks that can be parallelized.

**Estimated Output**: 15-20 numbered, ordered tasks in `tasks.md`.

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation

_These phases are beyond the scope of the /plan command_

**Phase 3**: Task execution (/tasks command creates `tasks.md`)
**Phase 4**: Implementation (execute `tasks.md` following constitutional principles)
**Phase 5**: Validation (run tests, execute `quickstart.md`, performance validation)

## Complexity Tracking

_Fill ONLY if Constitution Check has violations that must be justified_

| Violation | Why Needed | Simpler Alternative Rejected Because |
| --------- | ---------- | ------------------------------------ |
| N/A       | N/A        | N/A                                  |

## Progress Tracking

_This checklist is updated during execution flow_

**Phase Status**:

- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:

- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [x] Complexity deviations documented

---

_Based on Constitution v2.0.0 - See `/.specify/memory/constitution.md`_
