from fastapi import FastAPI
from llm_app.api import router

app = FastAPI()

# Include routers for different endpoints
app.include_router(router, prefix="/api/v1")