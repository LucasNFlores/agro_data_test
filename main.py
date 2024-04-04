""" import mysql.connector """
import json
import urllib
import requests
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
    # Procesar la entradas
    res = prueba_data(estacion_id)

    # Crear la respuesta
    data = {
        estacion_id: res
    }
    # funcion base de datos
    
    """ enviar_datos_bd(estacion_id, data) """
    
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

""" def enviar_datos_bd(estacion_id, data):
  mydb = mysql.connector.connect(
  host="31.170.167.153",
  user="u945673076_admML",
  password="Idi20232024",
  database="945673076_MakerWeb2023"
  )
  mycursor = mydb.cursor()
  json_data = JSONResponse(data).content
nombre = json_data["data"]
data = json_data["data"]
unit_display = json_data["unit_display"]

sql = "INSERT INTO uploads (device, tempout, humout, rocio, press, vel, velprom,term, tlluvia) VALUES (%s, %s, %s, %s, NOW())"
val = (estacion_id, nombre, data, unit_display)
mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close() """

""" def enviar_datos_bd(estacion_id, data):
  print("ingreso a la funcion")

  # Convertir los datos a JSON (asumiendo que data ya es un diccionario)
  json_data = data
  print("jsondata")
  print(json_data)
  url_php = "http://localhost/estación/api/apibot.php"
  print("url")

  # Preparar la solicitud POST
  headers = {'Content-type': 'application/json'}
  print("header")
  payload = {'data': json_data, 'estacion_id': estacion_id}
  payload = json_data
  print("payload")

  # Enviar la solicitud POST
  try:
    print("try")
    response = requests.post(url_php, headers=headers, data=payload)
    print(response)
    if response.status_code == 200:
      print("¡Datos enviados al archivo PHP correctamente!")
    else:
      print("else")
      print(f"Error al enviar datos: {response.status_code} - {response.text}")
  except Exception as e:
    print("no try")
    print(f"Error al enviar datos: {e}") """