#______________________integracion de etapas______________________
from dinamica_juego_v1 import iniciar_juego
from gestor_diccionario import generar_dicc_palabras_def_elegidas, transformador_lista_a_dicc
from palabras_aleatorias import seleccionar_palabras_aleatoria,orden_alfabetico
from recursos.datos import obtener_lista_definiciones
#___________________funciones complementarias_____________________


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

