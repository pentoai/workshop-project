import sys
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from baseball_backend.api.endpoints.query import router as query_router

load_dotenv()

# Remove default handler
logger.remove()

# Add a new handler for structured logging
logger.add(
    sys.stdout,
    serialize=True,
    enqueue=True,
    level="INFO",
    format="{level} {message}",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application lifespan events.

    This context manager handles startup and shutdown events for the FastAPI application.
    """
    # Startup
    logger.info("Baseball Backend API startup")
    yield
    # Shutdown (if needed in the future)


app = FastAPI(
    title="Baseball Backend API",
    description="API for querying baseball player information using AI agents.",
    version="1.0.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(query_router)


@app.get("/")
async def read_root():
    """Root endpoint returning basic API information.

    Returns:
        dict: Basic information about the API including status message and version.
    """
    return {"message": "Baseball Backend API is running", "version": "1.0.0"}
