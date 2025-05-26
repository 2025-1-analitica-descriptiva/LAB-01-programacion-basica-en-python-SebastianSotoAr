"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el file data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letter de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    ans = []
    url = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(url, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            letter = row[0]
            col4 = row[3].split(',') if row[3] else []
            col5 = row[4].split(',') if row[4] else []
            ans.append((letter, len(col4), len(col5)))

    return ans