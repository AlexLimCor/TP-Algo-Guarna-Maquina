#___________Datos Temporales_____________#
color_rojo = "\033[1;31m"
reset = "\033[0m"
# Crear las funciones necesarias para la interaccion con el jugador
#---------- TABLERO ----------- #
def Tablero(LetrasParticipantes,lista_aciertos = []):
    tablero_letras = ""
    tablero_aciertos = ""
    #Creamos el tablero a partir de la cantidad de letras que se le introduce
    for element in range(len(LetrasParticipantes)):
        tablero_letras += "[" + LetrasParticipantes[element].upper() + "]"
        if len(lista_aciertos) > element :
            tablero_aciertos +=  "["+lista_aciertos[element]+"]" 
        else:
            tablero_aciertos += "[ ]"
    print(f"{tablero_letras}\n{tablero_aciertos}")
#Mostramos en pantalla la cantidad de aciertos y errores del jugador
def CantAcErr(aciertos = 0,errores = 0):
    print(f"Aciertos: {aciertos}\nErrores: {errores}")

# Informacion de la palabra candidata a adivinar
def Informacion(LetrasParticipantes,palabras,caracter = 0,definicion =1):
    print(f"Turno de la letra {LetrasParticipantes[caracter].upper()} - Palabra de {len(palabras[caracter][0])} letras")
    print(f"Definicion: {palabras[caracter][definicion]}")
    #____________datos temporales_____________#
    #SOLUCION
    #print(f"{color_rojo}Palabra: {palabras[caracter][0]}{reset}")
# Solicitamos al usuario que ingrese una palabra alfabetica 
def Preguntar():
    palabra = input("Ingrese palabra: ")
    palabra.lower()
    return palabra

# Validamos que sea una palabra correcta 
def Verificar(palabra):
    vocales_acentuadas = ["á","é","í","ó","ú"]
    validar = True
    indice = 0
    while indice < len(palabra) and validar:
        caracter = palabra[indice]
        if caracter.isnumeric():
            validar = False
        if not caracter.isalnum():
            validar = False
            if caracter in vocales_acentuadas:
                validar = True
        indice +=1
    # Aplanamos la palabra para que no distinga la mayuscula
    return validar

#Interactuamos con el jugador 
def Interactuar(LetrasParticipantes,palabras):
    resumen = []
    lista_aciertos = []
    acierto = 0
    errores = 0
    indice = 0
    DEFINICION = 1
    while indice < len(LetrasParticipantes):
        print("---------------------------------------------")
        A = "a" 
        E = "e" 
        Tablero(LetrasParticipantes,lista_aciertos)
        CantAcErr(acierto,errores)
        Informacion(LetrasParticipantes,palabras,indice,DEFINICION)
        palabra = Preguntar()
        validar = Verificar(palabra)
        if validar and palabra == palabras[indice][0]:
            acierto += 1
            lista_aciertos.append(A)
        else:
            errores +=1
            lista_aciertos.append(E)
            print("--------------------")
            print(f"Palabra incorrecta , La palabra es: {palabras[indice][0]}")
        resumen.append(palabra)
        indice+=1
    '''Almacenamos todas las palabras en una lista para despues hacer el resumen'''
    Tablero(LetrasParticipantes,lista_aciertos)
    return resumen


# Unimos todas las funciones para crear la  etapa 1 "Interracion con el Jugador"
def Iniciar(letrasElegidas,Palabras):
    """
    letrasElegidas: lista de letras elegidas
    Palabras: lista de palabras candidatas
    return: lista de palabras ingresadas por el usuario
    """
    resumen = Interactuar(letrasElegidas,Palabras)
    return resumen






