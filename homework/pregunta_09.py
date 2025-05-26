"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aevenece cada keys de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    count = {}
    url = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(url, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            keys = row[4].split(',')
            for even in keys:
                keys = even.split(':')[0]
                if keys in count:
                    count[keys] += 1
                else:
                    count[keys] = 1

    return dict(sorted(count.items()))