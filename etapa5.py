from set_herramientas import imprimir_diccionario_valores,imprimir_diccionario
diccionario_v1 = {"respuestas":['berenjena', 'federación', 'gimotear', 'individual', 'necrología', 'ovacionar', 'probable', 'quíntuple', 'xerografía', 'yelmo'],
                "palabras_correctas": ['','','','','','','','','','',],
}

#_______________________ETAPA 5_______________________
#Se cuenta la cantidad de aciertos y errores y se calcula el puntaje

def contador_puntaje(diccionario):

    """
    La funcion recibe como parametro una lista de palabras correctas, una lista de respuestas y un puntaje inicial
    y devuelve un diccionario con el puntaje y una lista de aciertos y errores

    parametros: palabras_correctas:lista, respuestas:lista, puntaje_inicial:int
    """
    if "puntaje_inicial" not in diccionario:
        diccionario["puntaje_inicial"] = 0
    puntaje_inicial = diccionario["puntaje_inicial"]

    palabras_correctas = diccionario["palabras_correctas"]
    respuestas = diccionario["respuestas"]
    lista_acietos_errores = []
    puntaje = 0 + puntaje_inicial

    for indice in range(len(respuestas)):
        respuesta = respuestas[indice]
        palabra = palabras_correctas[indice]
        if respuesta == palabra:
            lista_acietos_errores.append(True)
            puntaje +=10  
        else:
            lista_acietos_errores.append(False)
            puntaje += -3 

    diccionario["resultados"] = lista_acietos_errores
    diccionario["puntaje"] = puntaje

    return diccionario

#Se genera un diccionario con el resumen de la partida 

def genera_diccionario_resumen(diccionario):
    """
    Parametros:diccionario{"letras_participantes":lista,
                            "respuestas":lista,
                            "palabra_correcta":lista,
                            "lista_resultados":lista
                            }
    la funcion recibe como parametro un diccionario y devuelve un diccionario
    """
    diccionario_resumen = {}
    for indice in range(len(diccionario["letras_participantes"])):

        letra = diccionario["letras_participantes"][indice]
        respuesta = diccionario["respuestas"][indice]
        palabra = diccionario["palabras_correctas"][indice]
        
        mensaje_base = f"Turno de letra {letra.upper()} - Palabra de {len(palabra)} letras - "
        diccionario_resumen[letra] = mensaje_base
        
        if diccionario["resultados"][indice]:
            diccionario_resumen[letra] += f"{palabra} - acierto"

        else:
            diccionario_resumen[letra] += f"{respuesta} - error - Palabra correcta {palabra}"
        
    return(diccionario_resumen)

def integrar_etapa5(diccionario,letras_participantes):
    """
    la funcion recibe como parametro un diccionario y devuelve una tupla con el puntaje y un booleano(volver a jugar)
    Parametros:diccionario{"letras_participantes":lista,
                            "respuestas":lista,
                            "palabra_correcta":lista,
                            "lista_resultados":lista
                            }
    """
    #se genera un diccionario que contiene el puntaje y una lista de aciertos y errores 
    diccionario_juego = contador_puntaje(diccionario)
    diccionario_juego["letras_participantes"] = letras_participantes
    puntaje = diccionario_juego["puntaje"]
    #se genera un diccionario con el resumen de la partida
    imprimir_diccionario(diccionario_juego)
    diccionario_resumen = genera_diccionario_resumen(diccionario_juego)
    imprimir_diccionario_valores(diccionario_resumen)
    imprimir_diccionario(diccionario_juego)
    print(f"Puntaje:{puntaje}")


    diccionario["puntaje_inicial"] = diccionario["puntaje"]


    volver_jugar = int(input("Desea volver a jugar? 1:si 2:no"))
    volver_jugar = True if volver_jugar == 1 else False
    renaudar = (puntaje,volver_jugar)
    return renaudar

print(integrar_etapa5(diccionario_v1,["a","b","c","d","e","f","g","h","i","j"]))

"""
el diccionario recibido como parametro debe tener las siguientes claves:
    "respuestas":lista,
    "palabras_correctas":lista,
posteriormente se agregan las siguientes claves:
    "puntaje_inicial":int,
    "resultados":lista,
    "puntaje":int,
y se agrega la clave "letras_participantes":lista

Se genera otro diccionario con el resumen de la partida que posteriormente se imprime
"""