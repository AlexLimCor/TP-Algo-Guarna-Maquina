import random
import doctest
def orden_alfabetico(elemento):
    """
    la funcion recibe como parametro una elemento de caracteres y 
    devuelve una lista con la equivalencia numerica de cada letra. 
    Si la elemento es una lista, se toma el primer elemento.
    >>> orden_alfabetico("hola")
    [8, 16, 12, 1]
    >>> orden_alfabetico("manzana")
    [13, 1, 14, 27, 1, 14, 1]
    >>> orden_alfabetico("árbol")
    [1, 19, 2, 16, 12]
    >>> orden_alfabetico("último")
    [22, 12, 21, 9, 13, 16]
    """
    abecedario = {
    'a': 1, 'á': 1, 
    'b': 2, 
    'c': 3, 
    'd': 4, 
    'e': 5, 'é': 5, 
    'f': 6, 
    'g': 7, 
    'h': 8, 
    'i': 9, 'í': 9,
    'j': 10, 
    'k': 11, 
    'l': 12, 
    'm': 13, 
    'n': 14, 
    'ñ': 15, 
    'o': 16, 'ó': 16, 
    'p': 17, 
    'q': 18, 
    'r': 19,
    's': 20, 
    't': 21, 
    'u': 22, 'ú': 22,  'ü': 22,
    'v': 23, 
    'w': 24, 
    'x': 25, 
    'y': 26, 
    'z': 27
    }
    equivalencia_numerica = []
    for letra in elemento:
        equivalencia_numerica.append(abecedario[letra])
    return equivalencia_numerica

def extraer_claves_coincidentes(diccionario,lista_palabras):
    """
    La funcion recibe como parametro un diccionario y una lista de palabras 
    y devuelve una lista de listas con la palabra y su definicion
    """
    lista_definiciones = []
    for palabra, definicion in diccionario.items():
        if palabra in lista_palabras:
            lista_definiciones.append([palabra,definicion])
        lista_definiciones = sorted(lista_definiciones, key=lambda x: orden_alfabetico(x[0]))
    return lista_definiciones


print(doctest.testmod())


def imprimir_diccionario_valores(diccionario):
    for valor in diccionario.values():
        print(valor)


def imprimir_diccionario(diccionario):
    #___________Colores___________
    azul = '\033[94m'
    reset = '\033[0m'
    for clave , valor in diccionario.items():
        print(f"{azul}{clave}:{reset}{valor}")


def correccion_alfabetica(cadena):
    """
    alternativa a la funcion orden_alfabetico
    """
    equivalencia_alfabetica = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'ñ': 'nz',
    }
    cadena_eq =""
    for caracter in cadena:
        if caracter in equivalencia_alfabetica.keys():
            cadena_eq += equivalencia_alfabetica[caracter]
        else:
            cadena_eq += caracter
    return cadena_eq
"""
print(correccion_alfabetica("árbol"))
print(correccion_alfabetica("ñandú"))
"""
print(correccion_alfabetica("ñu"))