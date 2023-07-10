from palabras_aleatorias import seleccionar_palabras_aleatoria, orden_alfabetico
from configuracion_juego import leer_configuracion
import doctest
import os

#_________________________Funciones complementarias___________________________

def extraer_claves_coincidentes(diccionario,lista_palabras):
    """
    La funcion recibe como parametro un diccionario y una lista de palabras 
    y devuelve una lista de listas con la palabra y su definicion en orden alfabetico
    
    >>> extraer_claves_coincidentes({"hola":"saludo","casa":"lugar donde se habita"},["hola","casa"])
    [['casa', 'lugar donde se habita'], ['hola', 'saludo']]
    >>> extraer_claves_coincidentes({"alcohol":"sustancia","casa":"lugar donde se habita"},["alcohol","casa"])
    [['alcohol', 'sustancia'], ['casa', 'lugar donde se habita']]
    >>> extraer_claves_coincidentes({"ceremonia":"ritual","raton":"dispositivo de entrada"},["ceremonia","raton"])
    [['ceremonia', 'ritual'], ['raton', 'dispositivo de entrada']]
    """
    lista_clave_valor = []
    for palabra, definicion in diccionario.items():
        if palabra in lista_palabras:
            lista_clave_valor.append([palabra,definicion])
        lista_clave_valor = sorted(lista_clave_valor, key=lambda x: orden_alfabetico(x[0]))
    return lista_clave_valor
    #CRUZ, ARIEL CARLOS LEONARDO​


def leer_archivo(archivo, default):
    """
    Parametros: archivo(objeto de open) y cadena
    return: linea del archivo o cadena default si se termino de leer el archivo
    """
    linea = archivo.readline()
    return linea if linea else default
    #CRUZ, ARIEL CARLOS LEONARDO​

def transformador_lista_a_dicc(datos):
    """
    Genera un diccionario con las palabras que cumplen con la condicion

    >>> transformador_lista_a_dicc([["hola","saludo"],["casa","lugar donde se habita"]])
    {'hola': 'saludo', 'casa': 'lugar donde se habita'}
    >>> transformador_lista_a_dicc([["manzana","fruta"],["pera","fruta"],["casa","lugar donde se habita"]])
    {'manzana': 'fruta', 'pera': 'fruta', 'casa': 'lugar donde se habita'}
    >>> transformador_lista_a_dicc([["arbol","planta"],["casa","lugar donde se habita"]])
    {'arbol': 'planta', 'casa': 'lugar donde se habita'}
    """
    palabras_candidatas = {}
    PALABRA = 0
    DEFINICION = 1
    for elemento in datos:
        #Armado del diccionario con la condicion
        palabras_candidatas[elemento[PALABRA]] = elemento[DEFINICION]
    return palabras_candidatas
    #CRUZ, ARIEL CARLOS LEONARDO​



#_________________________Rutas de archivos____________________________________


def generar_dicc_palabras_def_elegidas(diccionario_palabras_definiciones,cantidad_letras_rosco):
    """
    La elige las palabras que van a participar en el juego
    Parametros: diccionario {palabra:definicion, ...}
                numero entero. Cantidad de letras que va a tener el rosco
    return: diccionario con clave: palabra, valor: definicion
    """
    palabras_elegidas = seleccionar_palabras_aleatoria(list(diccionario_palabras_definiciones.keys()),cantidad_letras_rosco)
    lista_palabras_def_elegidas = extraer_claves_coincidentes(diccionario_palabras_definiciones,palabras_elegidas)
    INICIAL = 0
    diccionario_palabras_def_elegidas = {}
    for i in range(len(palabras_elegidas)):
        diccionario_palabras_def_elegidas[palabras_elegidas[i][INICIAL]] = lista_palabras_def_elegidas[i]
    return diccionario_palabras_def_elegidas
    #CRUZ, ARIEL CARLOS LEONARDO​

print(doctest.testmod())