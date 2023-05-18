# ETAPA_1
# INTERACCION CON EL JUGADOR

def tablero(letra,lista_acierto,letra_errada,letra_adivinada):

    for element in letra:
        print(f"["+element+"]",end="")
    print() 
    for acetado in lista_acierto:
        print(acetado,end="")
    print()
    print(f"Acierto: {letra_adivinada}")
    print(f"Errores: {letra_errada}")

def turno(letra,long_palabra,deficion):
    LETRA_CAND = 0
    print(f"Turno de letra {letra[LETRA_CAND]} - Palabra de {long_palabra} letras")
    print(f"Definicion: {deficion}")


def ingresar_palabra(palabra_cand):
    palabra = input("Ingrese palabra:")
    lista_vocal_acent = ["á", "é", "í", "ó", "ú"]

            










