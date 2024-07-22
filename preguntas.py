"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv
def pregunta_01():
    total = 0
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for fila in csv_reader:
            total += int(fila[1])
        return total
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

def pregunta_02():
    diccionario = {}
    cuenta = []
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for fila in csv_reader:
            if fila[0] not in diccionario:
                diccionario[fila[0]]=1
            else:
                diccionario[fila[0]]+=1
        diccionario = dict(sorted(diccionario.items()))
        for item in diccionario.items():
            cuenta.append(tuple(item))
    return cuenta

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    diccionario = {}
    cuenta = []
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for fila in csv_reader:
            if fila[0] not in diccionario:
                diccionario[fila[0]]=int(fila[1])
            else:
                diccionario[fila[0]]+=int(fila[1])
        diccionario = dict(sorted(diccionario.items()))
        for item in diccionario.items():
            cuenta.append(tuple(item))
    return cuenta


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    diccionario = {}
    cuenta = []
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for fila in csv_reader:
            if fila[2][5:7] not in diccionario:
                diccionario[fila[2][5:7]]=1
            else:
                diccionario[fila[2][5:7]]+=1
        diccionario = dict(sorted(diccionario.items()))
        for item in diccionario.items():
            cuenta.append(tuple(item))
    return cuenta



def pregunta_05():
    diccionario = {}
    cuenta = []
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            letra, valor_str = linea[0], linea[1]
            valor = int(valor_str)
            if letra in diccionario:
                diccionario[letra].append(valor)
            else:
                diccionario[letra] = [valor]
        for letra, valores_lista in diccionario.items():
            valores_min = min((valores_lista))
            valores_max = max((valores_lista))
            cuenta.append((letra, valores_max, valores_min))
        cuenta = sorted(cuenta)
    return cuenta


"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    diccionario = {}
    lista_letras = []
    nl = []
    cuenta = []
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            letras = linea[4].split(",")
            lista_letras.append(letras)
        for sublista in lista_letras:
            nl.extend(sublista)
        for elemento in nl:    
            if elemento[0:3] in diccionario:
                diccionario[elemento[0:3]].append(int(elemento[4:6]))
            else:
                diccionario[elemento[0:3]] = [int(elemento[4:6])]
        for letra, valores_lista in diccionario.items():
            valores_min = min((valores_lista))
            valores_max = max((valores_lista))
            cuenta.append((letra, valores_min, valores_max))
        cuenta = sorted(cuenta)

    return cuenta


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    diccionario = {}
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            if int(linea[1]) in diccionario:
                diccionario[int(linea[1])].append(linea[0])
            else:
                diccionario[int(linea[1])] = list(linea[0])
        lista = sorted(list(diccionario.items()))
        
        
    return lista


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    nl = []
    diccionario = {}
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            if int(linea[1]) in diccionario:
                diccionario[int(linea[1])].append(linea[0])
                
            else:
                diccionario[int(linea[1])] = [linea[0]]
        lista = sorted(list(diccionario.items()))
        for tupla in lista:
            nl.append((tupla[0], sorted(list(set(tupla[1])))))
            
        return nl
    

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista_letras = []
    nl = []
    diccionario = {}
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            letras = linea[4].split(",")
            lista_letras.append(letras)
        for sublista in lista_letras:
            nl.extend(sublista)
        for elemento in nl:
            if elemento[0:3] in diccionario:
                diccionario[elemento[0:3]]+=1
            else:
                diccionario[elemento[0:3]] = 1
        return dict(sorted(diccionario.items()))

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista = []
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            lista.append((linea[0],len(linea[3].split(",")),len(linea[4].split(","))))
    return lista




def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    diccionario = {}
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            letras = linea[3].split(",")
            for letra in letras:
                if letra not in diccionario:
                    diccionario[letra] = [int(linea[1])]
                else:
                    diccionario[letra].append(int(linea[1]))
        for letra in diccionario:
            diccionario[letra] = sum(diccionario[letra])
        return dict(sorted(diccionario.items()))

import re
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario = {}
    lista = []
    with open('data.csv', "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter='\t')
        for linea in csv_reader:
            partes = linea[4].split(",")
            numeros = [int(x.split(':')[1]) for x in partes if x.split(':')[1].isdigit()]
            if linea[0] in diccionario: 
                diccionario[linea[0]] += sum(numeros)
            else:
                diccionario[linea[0]] = sum(numeros)
    return dict(sorted(diccionario.items()))

