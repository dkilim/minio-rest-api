import uvicorn
from fastapi import FastAPI
from minio_rest_api.routes.client import cl

app = FastAPI()
app.include_router(cl)

