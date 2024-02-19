def ult_reporte_dato(soup, name):
    try:
        label = soup.find("div", class_="agro-label")

        # Separar al fecha que trae
        string = label.string
        date = re.findall(r"[0-9]+/[0-9]+", string)[0]

        data_display = label.find_next_sibling("span", class_="agro-display")

        string = data_display.string  # paso a string el dato de la hora

        # Se le saca el ultimo caracter del string ya que siempre se le agrega una "h"
        hour = string[:len(string) - 1]

        new_dict = {
            "nombre": label.string,
            "day": date,
            "hour": hour,
        }
        return print(new_dict)

    except:
        return print(f"Error en conseguir el dato {name}")

# Funcion para crear un diccionario de los datos en un div con clase "agro-unit-display"


def label_con_clase_agro_unit_display(soup, name):
    try:
        label = soup.find("div", class_="agro-label", string=name)
        data_display = label.find_next_sibling("span", class_="agro-display")
        unit_display = data_display.find_next_sibling(
            "span", class_="agro-unit-display")

        new_dict = {
            "nombre": label.string,
            "data": data_display.string,
            "unit_display": unit_display.string,
        }
        print(new_dict)
        return new_dict
    except:
        return print(f"Error en conseguir el dato {name}")

# Funcion para crear un diccionario de los datos en un div con doble "agro-display"


def label_display_unit(soup, name):

    try:
        label = soup.find("div", class_="agro-label", string=name)
        data_display = label.find_next_sibling("span", class_="agro-display")
        unit_display = data_display.find_next_sibling(
            "span", class_="agro-display")

        new_dict = {
            "nombre": label.string,
            "data": data_display.string,
            "unit_display": unit_display.string,
        }
        return new_dict
    except:
        return print(f"Error en conseguir el dato {name}")

# Funcion para crear un diccionario de los datos de "Dir. Viento"


def dir_viento_dato(soup, name):

    try:
        label = soup.find("div", class_="agro-label", string=name)
        data_display = label.find_next_sibling("span", class_="agro-display")
        data_display = label.find("span", class_="agro-display")

        new_dict = {
            "nombre": label.string,
            "data": data_display.string,
            "unit_display": "",
        }
        new_dict["data"] = new_dict["data"].strip()
        print(new_dict)

        return new_dict
    except:
        return print(f"Error en conseguir el dato {name}")


def prueba_data(estacion_id):
    import requests
    from bs4 import BeautifulSoup
    import json
    import re

    url = f"https://visual.agroclima.com/{estacion_id}"

    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html')

    datos_con_clase_agro_display = [
        "Sens. Térmica", "Temperatura", "Punto de Rocío"]
    datos_con_clase_agro_unit_display = [
        "Humedad", "Ráfagas", "Vel. Viento", "Presión Atm.", "Precipitaciones"]
    dato_direccion_viento = ["Dir. Viento"]

    dictionaries = []

    for i in dato_direccion_viento:
        new_dict = dir_viento_dato(soup, i)
        if new_dict == None:
            continue
        dictionaries.append(new_dict)
        print(dictionaries)

    for i in datos_con_clase_agro_display:
        new_dict = label_display_unit(soup, i)
        dictionaries.append(new_dict)

    for i in datos_con_clase_agro_unit_display:
        new_dict = label_con_clase_agro_unit_display(soup, i)
        dictionaries.append(new_dict)

    json_try = json.dumps(dictionaries, indent=4)

    json_try = json_try.strip("\n")

    return dictionaries
