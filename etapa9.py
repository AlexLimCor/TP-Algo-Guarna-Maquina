from etapa1 import Preguntar , Verificar


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
# Creo un diccionario que almacena los valores de aciertos y errores de cada jugador
def dicc_jugadores(lista_jugadores):
    ACIERTO = 0
    ERRORES = 0
    posicion = 1
    dicc_participantes = {}
    for element in lista_jugadores:
        if not element in dicc_participantes:
            dicc_participantes[element] = [posicion,ACIERTO,ERRORES]
            posicion +=1
    return dicc_participantes
# Mostrar en pantalla la cantidad de aciertos y errores de cada jugador
def imprimir_jugadores(dicc_participantes):
    ACIERTO =1 
    ERRORES = 2
    POSICION = 0
    print("Jugadores:")
    for clave,valor in dicc_participantes.items():
        print(f"{valor[POSICION]}. {clave} - Aciertos: {valor[ACIERTO]} - Errores: {valor[ERRORES]}")


# Informa la palabra candidata a adivinar
def Informacion(lista_jugadores,lista_letras,lista_palabras,definicion=1,posicion=0,indice=0):
    print(f"Turno Jugador {posicion+1}. {lista_jugadores[posicion]} - letra {lista_letras[indice].upper()} - Palabra de {len(lista_palabras[indice][0])} letras")
    print(f"Definicion: {lista_palabras[indice][definicion]}")



# Importamos de la etapa 1 la funcion preguntar() y verificar() para validar la palabra que ingresa el usuario
def Interactuar(lista_jugadores,lista_palabras,lista_letras):
    indice = 0
    dicc_participantes = dicc_jugadores(lista_jugadores)
    lista_turno = []
    lista_aciertos = []
    posicion = 0
    DEFINICION =1
    ACIERTOS = 1
    ERRORES = 1
    dicc_registro = {}
    cant_jugadores = len(lista_jugadores)
    while indice < len(lista_letras):
        A = "a"
        E = "e"
        if cant_jugadores <= posicion:
            posicion = 0
        jugador = f"{posicion+1}"
        continuar= True
        while continuar and indice < len(lista_letras):
            print("----------------------------------------")
            tablero(lista_letras,lista_turno,lista_aciertos)
            imprimir_jugadores(dicc_participantes)
            Informacion(lista_jugadores,lista_letras,lista_palabras,DEFINICION,posicion,indice)
            palabra = Preguntar()
            validar = Verificar(palabra)
            if validar and palabra == lista_palabras[indice][0]:
                dicc_participantes[lista_jugadores[posicion]][1] += ACIERTOS
                lista_turno.append(jugador)
                lista_aciertos.append(A)
            else:
                dicc_participantes[lista_jugadores[posicion]][2] += ERRORES
                lista_turno.append(jugador)
                lista_aciertos.append(E)
                continuar = False
            if lista_jugadores[posicion] in dicc_registro:
                dicc_registro[lista_jugadores[posicion]].append(palabra)
            else:
                dicc_registro[lista_jugadores[posicion]] = [palabra]
            indice +=1
        posicion += 1
    tablero(lista_letras,lista_turno,lista_aciertos)
    return dicc_registro






# ---- Por ultimo esta funcion recibe como parametro una lista de jugadores
# una lista de palabras anidadas junto con su definicion
# una lista de letras seleccionadas
def Prueba(jugadores,palabras,letras):
    resumen = Interactuar(jugadores,palabras,letras)
    return resumen




#print(Prueba(["alex","admin"],[["argentina","pais"],["brasil","pais"],["camerun","pais"]],["a","b","c"]))





#tablero(["a","e","i"],["1","2","3"],["a","e","a"])

