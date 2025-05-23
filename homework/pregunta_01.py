"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    total = 0
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')  # cambia a ',' si usa comas
        for fila in lector:
            total += int(fila[1])
    return total