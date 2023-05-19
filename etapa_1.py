from datos import obtener_lista_definiciones

# ETAPA_1
# INTERACCION CON EL JUGADOR

def tablero(letras_candidatas):
    # CREO UNA FUNCION QUE OBTENGA LOS 10 CARACTERES A JUGAR (ETAPA 3)
    ACIERTOS = 0
    ERRORES = 0
    lista_aciertos = []
    for element in letras_candidatas:
        print(f"["+element+"]",end="")
    print() 
    for acertado in lista_aciertos:
        print(acertado,end="")
    print()
    print(f"Acierto: {ACIERTOS}")
    print(f"Errores: {ERRORES}")

def turno(palabra_y_deficion):
    # OBTENEMOS EL DICCIONARIO CON SU PALABRA Y DEFINICION 
    LETRA_CAND = 0
    DEFINICION = 1
    print(f"Turno de letra {palabra_y_deficion[LETRA_CAND]} - Palabra de {len(palabra_y_deficion[LETRA_CAND])} letras")
    print(f"Definicion: {palabra_y_deficion[DEFINICION]}")

def ingre_palabra(palabras_candidatas):
    # ETAPA 5 , PUNTAJE 
    palabra = input("Ingrese palabra:")

# ETAPA 2
'''En esta etapa procesamos el diccionario de palabras con sus definiciones y lo convertimos a diccionario con los requisitos pedidos'''
def etapa_2():
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
print(etapa_2())







        





            










