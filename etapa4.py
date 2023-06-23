#______________________integracion de etapas______________________
from etapa1 import Jugar
from etapa2 import integrar_etapa_2
from etapa3 import integrar_etapa_3
from etapa5 import integrar_etapa_5
from datos import obtener_lista_definiciones
def integrar_juego(cantidad_letras):
    diccionario = integrar_etapa_2(obtener_lista_definiciones())
    letras_elegidas,palabras_elegidas = integrar_etapa_3(diccionario,cantidad_letras)
    respuestas = Jugar(letras_elegidas,palabras_elegidas)
    diccionario_juego = {"letras_participantes" : letras_elegidas,
                         "respuestas": respuestas,
                         "palabras_correctas" : palabras_elegidas,
                         "puntaje_inicial" : 0}
    puntaje, volver_a_jugar = integrar_etapa_5(diccionario_juego)
    renaudar = integrar_juego(cantidad_letras) if volver_a_jugar else print(f"Fin del juego, Puntaje final : {puntaje}")
    return renaudar


print(integrar_juego(10))