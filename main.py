from app.data_recolection import prueba_data
from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Existo": "Luego pienso"}


@app.get("/api/json/get_data/{estacion_id}")
async def get_json(estacion_id):
    # Procesar la entrada
    res = prueba_data(estacion_id)

    # Crear la respuesta
    data = {
        estacion_id: res
    }

    print(data)
    # Devolver la respuesta como JSON

    return JSONResponse(data)


@app.get("/api/jsonprueba")
async def get_json():
    data = {
        "Esto es": "una prueba",
        "nombre": "Humedad",
        "data": "88",
        "unit_display": "%"
    }

    return JSONResponse(data)
