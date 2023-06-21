#---- MOSTRAR TABLERO --- #

def tablero(letrasParticipantes,lista_turno=[],lista_aciertos =[]):
    tablero_letras = ""
    tablero_turno = ""
    tablero_aciertos = ""
    for element in range(len(letrasParticipantes)):
        tablero_letras += "["+ letrasParticipantes[element].upper() + "]"
        if len(lista_turno) > element:
            tablero_turno += "[" +lista_turno[element]+"]"
        else:
            tablero_turno += "[ ]"
        if len(lista_aciertos) > element:
            tablero_aciertos += "["+lista_aciertos[element]+"]"
        else:
            tablero_aciertos += "[ ]"
    print(f"{tablero_letras}\n{tablero_turno}\n{tablero_aciertos}")

'''def Jugadores(lista_jugadores):'''



#tablero(["a","e","i"],["1","2","3"],["a","e","a"])

