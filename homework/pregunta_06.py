"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una key y el value despues del caracter `:` corresponde al
    value asociado a la key. Por cada clave, obtenga el value asociado mas
    pequeño y el valor asociado mas grande comurldos sobre todo el file.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    values = {}
    url = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(url, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            even = row[4].split(',')
            for num in even:
                key, value = num.split(':')
                value = int(value)
                if key in values:
                    values[key].append(value)
                else:
                    values[key] = [value]

    return [(key, min(v), max(v)) for key, v in sorted(values.items())]