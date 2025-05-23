"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    conteo = {}

    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')  # ajusta a ',' si no son tabulaciones
        for fila in lector:
            letra = fila[0]
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1

    resultado = sorted(conteo.items())
    return resultado