from fastapi import FastAPI
from .settings import configure_logging

app = FastAPI()
logger=configure_logging()

@app.get("/")
async def root():
    logger.info("Hello:)")
    return {"message": "Hello World"}