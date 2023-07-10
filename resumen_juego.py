#______________________integracion de etapas______________________
from dinamica_juego_v1 import iniciar_juego
from gestor_diccionario import generar_dicc_palabras_def_elegidas, transformador_lista_a_dicc
from palabras_aleatorias import seleccionar_palabras_aleatoria
from datos import obtener_lista_definiciones
#___________________funciones complementarias_____________________
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
    #CRUZ, ARIEL CARLOS LEONARDO​


def imprimir_diccionario(diccionario):
    #___________Colores___________
    azul = '\033[94m'
    reset = '\033[0m'
    for clave , valor in diccionario.items():
        print(f"{azul}{clave}:{reset}{valor}")
    #CRUZ, ARIEL CARLOS LEONARDO​


def generar_dicc_juego(palabras_elegidas,respuestas):
    dicc_juego = {}
    INICIAL = 0
    for elemento in range(len(palabras_elegidas)):
        dicc_juego[palabras_elegidas[elemento][INICIAL]] = [palabras_elegidas[elemento],respuestas[elemento]]
    return dicc_juego
    #CRUZ, ARIEL CARLOS LEONARDO​
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
    #CRUZ, ARIEL CARLOS LEONARDO​

#______________________Etapas 4__________________________



def generar_resumen_partida(cantidad_letras):
    """
    La funcion recibe como parametro un numero entero y devuelve un diccionario con las respuestas del usuario
    parametros: cantidad_letras: int
    return: diccionario {letra:[palabra,respuesta]...}
    """

    diccionario = transformador_lista_a_dicc(obtener_lista_definiciones())
    palabras_elegidas = seleccionar_palabras_aleatoria(list(diccionario.keys()),cantidad_letras)
    dicc_palabras_definicion = generar_dicc_palabras_def_elegidas(diccionario,cantidad_letras)
    print("dicc_palabras_definicion",dicc_palabras_definicion)
    respuestas = iniciar_juego(dicc_palabras_definicion)
    diccionario_juego = generar_dicc_juego(palabras_elegidas,respuestas)
    return diccionario_juego
    #CRUZ, ARIEL CARLOS LEONARDO​

