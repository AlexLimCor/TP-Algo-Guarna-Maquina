#______________________integracion de etapas______________________
from etapa1 import Iniciar
from etapa2 import integrar_etapa_2
from etapa3 import integrar_etapa_3
from datos import obtener_lista_definiciones
from etapa8 import leer_diccionario
from set_herramientas import extraer_claves_coincidentes,imprimir_diccionario
#___________________funciones complementarias_____________________
def generar_dicc_juego(palabras_elegidas,respuestas):
    dicc_juego = {}
    INICIAL = 0
    for elemento in range(len(palabras_elegidas)):
        dicc_juego[palabras_elegidas[elemento][INICIAL]] = [palabras_elegidas[elemento],respuestas[elemento]]
    return dicc_juego

#______________________Etapas 4__________________________



def integrar_juego(cantidad_letras,puntaje_inicial=0):

    diccionario = integrar_etapa_2(obtener_lista_definiciones())

    letras_elegidas,palabras_elegidas = integrar_etapa_3(diccionario,cantidad_letras)
    palabras_definicion = extraer_claves_coincidentes(diccionario,palabras_elegidas)
    respuestas = Iniciar(letras_elegidas,palabras_definicion)
    diccionario_juego = generar_dicc_juego(palabras_elegidas,respuestas)
    return diccionario_juego

#______________________Etapas 4 con csv__________________________

def intregrar_juego_csv(cantidad_letras):
    """
    Parametros:
        cantidad_letras: numero entero
    return: diccionario con clave: letra, valor: lista con [palabra , respuesta]
    """
    diccionario = integrar_etapa_2(leer_diccionario())
    lista_palabras = diccionario.keys()
    letras_elegidas,palabras_elegidas = integrar_etapa_3(lista_palabras,cantidad_letras)
    palabras_definicion = extraer_claves_coincidentes(diccionario,palabras_elegidas)
    respuestas = Iniciar(letras_elegidas,palabras_definicion)
    diccionario_juego = generar_dicc_juego(palabras_elegidas,respuestas)
    return diccionario_juego