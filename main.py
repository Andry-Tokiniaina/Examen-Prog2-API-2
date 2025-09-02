from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
import datetime

app = FastAPI()

@app.get("/ping")
def root():
    return Response(content="pong", status_code=200, media_type="text/plain")