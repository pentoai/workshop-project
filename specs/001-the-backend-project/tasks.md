# Tasks: Baseball Backend API with AI Agent

**Input**: Design documents from `/specs/001-the-backend-project/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Phase 3.1: Setup

- [x] T001 Create project structure in `baseball_backend/` as defined in `plan.md`.
- [x] T002 Initialize Python project with `uv` and install dependencies: `fastapi`, `openai`, `loguru`, `pytest`, `uvicorn`.
- [x] T003 [P] Configure `loguru` for structured logging in `baseball_backend/src/baseball_backend/main.py`.

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3

**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**

- [x] T004 [P] Create failing unit test for the database tool in `baseball_backend/tests/unit/tools/test_database_tool.py`.
- [x] T005 [P] Create failing unit test for the web search tool in `baseball_backend/tests/unit/tools/test_web_search_tool.py`.
- [x] T006 [P] Create failing unit test for the baseball agent in `baseball_backend/tests/unit/test_baseball_agent.py`.
- [x] T007 [P] Create failing integration test for the `/query` endpoint in `baseball_backend/tests/integration/test_query_endpoint.py` based on `quickstart.md`.

## Phase 3.3: Core Implementation (ONLY after tests are failing)

- [x] T008 [P] Implement the `BaseballPlayerInfo` Pydantic model in `baseball_backend/src/baseball_backend/models/player_info.py` as defined in `data-model.md`.
- [x] T009 Implement the database tool in `baseball_backend/src/baseball_backend/tools/database_tool.py` to pass the test from T004.
- [x] T010 Implement the web search tool in `baseball_backend/src/baseball_backend/tools/web_search_tool.py` to pass the test from T005.
- [x] T011 Implement the AI agent logic in `baseball_backend/src/baseball_backend/agents/baseball_agent.py` to pass the test from T006.
- [x] T012 Implement the `/query` endpoint in `baseball_backend/src/baseball_backend/api/endpoints/query.py`.
- [x] T013 Implement the main FastAPI application in `baseball_backend/src/baseball_backend/main.py`, integrating the `query` endpoint.
- [x] T014 Ensure the integration test from T007 passes.

## Phase 3.4: Polish

- [x] T015 [P] Add comprehensive docstrings to all new functions and classes.
- [x] T016 [P] Review and refactor for clarity and simplicity.
- [x] T017 Execute the `quickstart.md` manual test scenario to validate the end-to-end functionality.

## Dependencies

- **Setup (T001-T003)** must be completed before all other tasks.
- **Tests (T004-T007)** must be completed before Core Implementation (T008-T014).
- **T008 (Model)** is a dependency for T011 (Agent) and T012 (Endpoint).
- **T009 (DB Tool)** and **T010 (Web Tool)** are dependencies for **T011 (Agent)**.
- **T011 (Agent)** is a dependency for **T012 (Endpoint)**.
- **T012 (Endpoint)** is a dependency for **T013 (Main App)**.
- **Core Implementation (T008-T014)** must be completed before Polish (T015-T017).

## Parallel Example

The unit tests can be developed in parallel as they target different, isolated components.

```
# Launch T004, T005, and T006 together:
Task: "Create failing unit test for the database tool in baseball_backend/tests/unit/tools/test_database_tool.py"
Task: "Create failing unit test for the web search tool in baseball_backend/tests/unit/tools/test_web_search_tool.py"
Task: "Create failing unit test for the baseball agent in baseball_backend/tests/unit/test_baseball_agent.py"
```
