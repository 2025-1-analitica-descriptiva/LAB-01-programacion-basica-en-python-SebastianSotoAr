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

    count = {}

    url = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')
    with open(url, newline='', encoding='utf-8') as archivo:
        reader = csv.reader(archivo, delimiter='\t')
        for fila in reader:
            letter = fila[0]
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

    return sorted(count.items())