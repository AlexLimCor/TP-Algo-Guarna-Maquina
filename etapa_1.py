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
    # OBTENEMOS EL DICCIONARIO CON SU PALABRA Y DEFINICION (ETAPA 2) 
    LETRA_CAND = 0
    DEFINICION = 1
    print(f"Turno de letra {palabra_y_deficion[LETRA_CAND]} - Palabra de {len(palabra_y_deficion[LETRA_CAND])} letras")
    print(f"Definicion: {palabra_y_deficion[DEFINICION]}")

def ingre_palabra(palabras_candidatas):
    # ETAPA 5 , PUNTAJE 
    palabra = input("Ingrese palabra:")

        





            










