
## Descripción
API para aprovechar los datos de https://visual.agroclima.com/ para un estudio climatico
Deploy hecho en [https://www.fl0.com/](FL0) con python y el framework fast API

## Instalacion y configuracion

En el .env configurar el puerto al que escuchara la aplicacion

- ```pip install virtualenv```
- ```.\Scripts\activate```
- ```pip install -r requirements.txt```
- ```uvicorn main:app --reload```

## Pagina web de acceso
https://agro-data-test-dev-fpea.4.us-1.fl0.io/

## EndPoints disponibles
Cambiar estacion_id por la estacion elegida de la cual extraer los ultimos datos disponible de la misma:

https://agro-data-test-dev-fpea.4.us-1.fl0.io//api/json/get_data/{estacion_id}