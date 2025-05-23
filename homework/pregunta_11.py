"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    suma = {}
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            valor = int(fila[1])
            letras = fila[3].split(',') if fila[3] else []
            for letra in letras:
                if letra in suma:
                    suma[letra] += valor
                else:
                    suma[letra] = valor

    resultado = dict(sorted(suma.items()))
    return resultado