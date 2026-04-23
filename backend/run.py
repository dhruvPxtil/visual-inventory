#!/usr/bin/env python
"""
Visual Inventory Backend - Application Entry Point

Starts the FastAPI server with all ML/CV models and services loaded.
"""

import os
import sys
import logging
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Start the FastAPI application server."""
    
    # Configuration
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    env = os.getenv("ENV", "development")
    debug = os.getenv("DEBUG", "False").lower() == "true"
    workers = int(os.getenv("WORKERS", 1))
    
    logger.info(f"Starting Visual Inventory Backend")
    logger.info(f"Environment: {env}")
    logger.info(f"Host: {host}:{port}")
    logger.info(f"Debug: {debug}")
    logger.info(f"Workers: {workers}")
    
    # Run server
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=debug,
        workers=workers if not debug else 1,
        log_level="info" if debug else "warning",
        access_log=True,
        lifespan="on"
    )


if __name__ == "__main__":
    main()
