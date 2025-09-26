<!--
SYNC IMPACT REPORT
- Version: 1.0.0 -> 2.0.0
- Modified Principles:
  - [PRINCIPLE_1_NAME] -> Frontend Framework and Architecture
  - [PRINCIPLE_2_NAME] -> Frontend Styling
  - [PRINCIPLE_3_NAME] -> Frontend Component Library
  - [PRINCIPLE_4_NAME] -> Frontend API Layer
  - [PRINCIPLE_5_NAME] -> Frontend Testing Strategy
  - [PRINCIPLE_6_NAME] -> Backend Language and Typing
  - [PRINCIPLE_7_NAME] -> Backend Web Framework
  - [PRINCIPLE_8_NAME] -> Backend AI Integration
  - [PRINCIPLE_9_NAME] -> Backend Testing Strategy
  - [PRINCIPLE_10_NAME] -> Backend Dependency Management
  - [PRINCIPLE_11_NAME] -> Backend Code Philosophy
- Templates requiring updates: none
- Follow-up TODOs: none
-->

# [Baseball App] Project Constitution

## Governance

- **Constitution Version**: 2.0.0
- **Ratification Date**: 2025-09-26
- **Last Amended Date**: 2025-09-26
- **Amendment Process**: Changes to this constitution must be proposed as a pull request and approved by the project maintainers.
- **Compliance**: All code contributed to this project must adhere to the principles outlined in this document.

---

## Principles

### 1. Frontend Framework and Architecture

- **Principle**: The frontend application will be built using Next.js 15 with the App Router. All data fetching and mutations must be handled by Server Actions. The primary language for frontend development is TypeScript.
- **Rationale**: This stack provides a modern, performant, and maintainable foundation for the user interface. Server Actions simplify data flow and reduce the need for a separate API layer in the frontend.

### 2. Frontend Styling

- **Principle**: Tailwind CSS will be used for all styling.
- **Rationale**: Tailwind CSS provides a utility-first approach that enables rapid development and ensures a consistent design system without writing custom CSS.

### 3. Frontend Component Library

- **Principle**: The project will use shadcn/ui for UI components. New components can be added by running `npx shadcn-ui@latest add <component-name>`. A list of available components can be found on the shadcn/ui website.
- **Rationale**: shadcn/ui offers a set of accessible and customizable components that can be easily integrated into the project, accelerating development.

### 4. Frontend API Layer

- **Principle**: Server Actions are the primary method for client-server communication. Traditional API routes in the Next.js application should be avoided.
- **Rationale**: Using Server Actions centralizes server-side logic and reduces boilerplate, making the frontend codebase cleaner and more focused.

### 5. Frontend Testing Strategy

- **Principle**: Testing will focus on business logic within Server Actions and any helper functions. UI component testing is explicitly out of scope. Test-Driven Development (TDD) will not be used for frontend development.
- **Rationale**: This pragmatic approach to testing ensures that critical logic is reliable without the overhead of maintaining UI tests, which can be brittle and time-consuming.

### 6. Backend Language and Typing

- **Principle**: The backend will be written in Python 3.12, using modern type hints (e.g., `list[str]`, `str | None`) instead of imports from the `typing` module.
- **Rationale**: Using the latest Python version and modern typing syntax improves code readability and maintainability.

### 7. Backend Web Framework

- **Principle**: The backend API will be built using the FastAPI framework.
- **Rationale**: FastAPI is a high-performance web framework for Python that is easy to use and provides automatic interactive documentation.

### 8. Backend AI Integration

- **Principle**: The backend will use the OpenAI Agents SDK to build and serve AI-powered features.
- **Rationale**: This SDK provides the necessary tools to create sophisticated AI agents, which are a core part of the application's functionality.

### 9. Backend Testing Strategy

- **Principle**: A strict Test-Driven Development (TDD) approach is mandatory for all backend code. `pytest` will be used as the testing framework. Every new feature or bug fix must start with a failing test.
- **Rationale**: TDD ensures that the codebase is well-tested, and that functionality meets requirements from the start, leading to higher quality and more maintainable code.

### 10. Backend Dependency Management

- **Principle**: Project dependencies will be managed using `uv`. Production dependencies should be added with `uv add <package>`, and development dependencies with `uv add -d <package>`.
- **Rationale**: `uv` is a fast and modern package manager for Python that simplifies dependency management and improves reproducibility.

### 11. Backend Code Philosophy

- **Principle**: The backend code should prioritize simplicity and clarity. Avoid premature optimizations and unnecessary abstractions. Failures should be handled gracefully at the API level by returning appropriate HTTP status codes and error messages.
- **Rationale**: A simple and direct coding style makes the application easier to understand, debug, and maintain over time.
