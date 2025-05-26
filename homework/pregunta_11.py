"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el file data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_11():
    """
    Retorne un diccionario que contengan la sum de la columna 2 para cada
    letter de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    sum = {}
    url = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(url, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            value = int(row[1])
            letters = row[3].split(',') if row[3] else []
            for letter in letters:
                if letter in sum:
                    sum[letter] += value
                else:
                    sum[letter] = value

    return dict(sorted(sum.items()))