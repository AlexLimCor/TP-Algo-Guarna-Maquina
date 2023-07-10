from resumen_puntaje import *
from resumen_juego import *
"""
Reafactorizacion de la primera entrega.
"""
def jugar_pasapalabra():
    CANTIDAD_LETRAS = int(input("Ingrese cantidad de letras del rosco: "))
    diccionario = generar_resumen_partida(CANTIDAD_LETRAS)
    jugar_pasapalabras(diccionario,CANTIDAD_LETRAS)
jugar_pasapalabra()

