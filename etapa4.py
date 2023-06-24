#______________________integracion de etapas______________________
from etapa1 import Jugar
from etapa2 import integrar_etapa_2
from etapa3 import integrar_etapa_3
from etapa5 import integrar_etapa_5
from datos import obtener_lista_definiciones
from set_herramientas import extraer_claves_coincidentes

def integrar_juego(cantidad_letras,puntaje_inicial=0):

    diccionario = integrar_etapa_2(obtener_lista_definiciones())

    letras_elegidas,palabras_elegidas = integrar_etapa_3(diccionario,cantidad_letras)
    palabras_definicion = extraer_claves_coincidentes(diccionario,palabras_elegidas)
    respuestas = Jugar(letras_elegidas,palabras_definicion)
    diccionario_juego = {"letras_participantes" : letras_elegidas,
                         "respuestas": respuestas,
                         "palabras_correctas" : palabras_elegidas}
    puntaje, volver_a_jugar = integrar_etapa_5(diccionario_juego,puntaje_inicial)
    renaudar = integrar_juego(cantidad_letras,puntaje) if volver_a_jugar else print(f"Fin del juego, Puntaje final : {puntaje}")
    return renaudar


integrar_juego(10)
