# ETAPA_1
# INTERACCION CON EL JUGADOR

def tablero(lista_letras_a_jugar,lista_acierto,letra_errada,letra_adivinada):
    for element in lista_letras_a_jugar:
        print(f"["+element+"]",end="")
    print() 
    for acetado in lista_acierto:
        print(acetado,end="")
    print()
    print(f"Acierto: {letra_adivinada}")
    print(f"Errores: {letra_errada}")
tablero(["a","b"],[[]],0,1)





