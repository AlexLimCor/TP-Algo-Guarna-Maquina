from datos import obtener_lista_definiciones

# ----------ETAPA 2---------
'''En esta etapa procesamos el diccionario de palabras con sus definiciones y
 lo convertimos a diccionario con los requisitos pedidos'''

def generador_diccionario():
    datos = obtener_lista_definiciones()
    dicc_pal_def = {}
    LONG_MIN = 5
    PALABRA = 0
    DEFINICION = 1
    for element in datos:
        clave = element[PALABRA]
        valor = element[DEFINICION]
        if len(clave) >= LONG_MIN:
            dicc_pal_def[clave] = valor
    return dicc_pal_def



def genera_diccionario_resumen(diccionario):
    """
    la funcion recibe como parametro un diccionario y devuelve un diccionario
    """
    diccionario_resumen = {}
    for indice in range(len(diccionario["letra_participantes"])):

        letra = diccionario["letra_participantes"][indice]
        respuesta = diccionario["respuestas"][indice]
        palabra = diccionario["Palabra_definicion"][indice][0]

        if diccionario["es_correcto"][indice]:
            diccionario_resumen[letra] = f"Turno de letra {letra.upper()} - Palabra de {len(palabra)} letras - {palabra} - acierto"

        else:
            diccionario_resumen[letra] = f"Turno de letra {letra.upper()} - Palabra de {len(palabra)} letras - {respuesta} - error - Palabra correcta {palabra}"
        
    return(diccionario_resumen)

def contador_puntaje(palabra_definicion,lista,puntaje_inicial = 0):
    lista_acietos_errores = []
    INDICE = 0
    palabra_correcta = 0 
    PUNTAJE = 0 + puntaje_inicial

    for palabra in lista:
        if palabra == palabra_definicion[INDICE][palabra_correcta]:
            lista_acietos_errores.append(True)
            PUNTAJE +=10  
        else:
            lista_acietos_errores.append(False)
            PUNTAJE += -3 
    
    diccionario_puntaje = {"puntaje":PUNTAJE,"lista_acietos_errores":lista_acietos_errores} 
    return diccionario_puntaje
    


