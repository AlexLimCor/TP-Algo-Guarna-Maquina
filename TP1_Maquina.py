from etapa5 import *
"""
Reafactorizacion de la primera entrega.
"""
def jugar_pasapalabra():
    CANTIDAD_LETRAS = int(input("Ingrese cantidad de letras del rosco: "))
    diccionario = integrar_etapa4(CANTIDAD_LETRAS)
    integrar_etapa_5(diccionario,CANTIDAD_LETRAS)
jugar_pasapalabra()