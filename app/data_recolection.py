import requests
from bs4 import BeautifulSoup
import re

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
    
        label.string: data_display.string,
        "unit_display": unit_display.string
    
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
   
        label.string: data_display.string,
        "unit_display": unit_display.string
    
}
        return new_dict
    except:
        return print(f"Error en conseguir el dato {name}")

# Funcion para crear un diccionario de los datos de "Dir. Viento"


""" def dir_viento_dato(soup, name):
    try:
        label = soup.find("div", class_="agro-label", string=name)
        labels = label.find_next_sibling("span", class_="agro-display")
        print(soup.find("div", class_="agro-label", string=name))
        print(label.find_next_sibling("span", class_="agro-display"))
        print(labels.find_next_sibling("span", class_="agro-display"))
        
        if not label:
            print(f"Etiqueta con el nombre '{name}' no encontrada.")
            return None

        # Función para buscar el elemento `span` anidado con la clase "agro-display":
        def find_nested_span(element, class_):
            print("ingreso a la funcion")
            for child in element.find_all("span", class_=class_):
                print("ingreso al for")
                if child.text:  # Verifica si contiene texto
                    print("texto enconctrado")
                    return child
                else:
                    nested_span = find_nested_span(child, class_)
                    if nested_span:
                        print("span encontrado")
                        print(nested_span)
                        return nested_span
            return None

        data_display = find_nested_span(labels, "agro-display")
        

        if not data_display:
            print(f"Datos para '{name}' no encontrados.")
            return None

        new_dict = {
            "nombre": label.string,
            "data": data_display.string.strip(),
            "unit_display": "",
        }

        print(new_dict)
        return new_dict

    except Exception as e:
        print(f"Error inesperado: {e}")
        return None  # Indica error """

""" try:
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
        return print(f"Error en conseguir el dato {name}") """

""" def dir_viento_dato(soup, name):
  try:
    label = soup.find("div", class_="agro-label", string=name)

    if not label:
      print(f"Etiqueta con el nombre '{name}' no encontrada.")
      return None

    # Search for next sibling containing wind direction data (assuming it's not in a span)
    next_sibling = label.find_next_sibling()
    if not next_sibling:
      print(f"Datos para '{name}' no encontrados.")
      return None

    # Extract wind direction (assuming it's the first sibling's text)
    wind_direction = next_sibling.text.strip()

    # Create the dictionary with extracted data
    new_dict = {
      "nombre": label.string,
      "data": wind_direction,
      "unit_display": "",  # Assuming unit is not provided in this case
    }

    print(new_dict)
    return new_dict

  except Exception as e:
    print(f"Error inesperado: {e}")
    return None """
def dir_viento_dato(soup, name):
    table = soup.find(id="table-items")

    print("sdasd")

    for row in table.find_all("tr"):
        th_text = row.find("th").text
        if th_text == "Dirección":
            fila = row
            break

    ultimo_td = fila.find_all("td")[-1]

    content = ultimo_td.text

    print(obtener_numero(content))
    return obtener_numero(content)
            



def obtener_numero(cadena):
    match = re.search(r"[0-9.]+", cadena)  # Find numbers using regex
    if match:
         new_dict = {
   
        "Dirección": float(match.group()),
            }
    return new_dict
    """ else:
        return None """




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
    dato_direccion_viento = ["Dirección"]

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
