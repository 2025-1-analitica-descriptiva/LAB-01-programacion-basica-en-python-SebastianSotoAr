"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    conteo_meses = {}
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            fecha = fila[2]
            mes = fecha.split('-')[1]
            if mes in conteo_meses:
                conteo_meses[mes] += 1
            else:
                conteo_meses[mes] = 1

    resultado = sorted(conteo_meses.items())
    return resultado
