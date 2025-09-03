from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
import datetime

app = FastAPI()

class Characteristics:
    max_speed: float
    max_fluel_capacity: float

class Cars:
    id: int
    brand: str
    model: str
    characteristics: Characteristics

carsList = List[Cars]

@app.get("/ping")
def root():
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.post("/cars")
def post_cars(cars: List[Cars]):
    for car in cars:
        carsList.append(car)
    return Response(status_code=201, content=carsList, type="application/json")

@app.get("/cars")
def get_cars():
    return Response(status_code=200, content=carsList.dump(), type="application/json")


@app.get("/car/{id}")
def get_car_by_id():
    id= Request.headers["id"]
    for car in carsList:
        if car.id == id:
            return Response(status_code=200, content=car.dump(), type="application/json")