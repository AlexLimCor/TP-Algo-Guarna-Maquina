import doctest

# ---------------------- ETAPA 1 ---------------- #
# Crear las funciones necesarias para la interaccion con el jugador
# VARIABLES DE TEXTO
TEXTO_ACIERTO = "Aciertos"
TEXTO_ERRORES = "Errores"
TEXTO_TURNO = 'Turno de la letra'
TEXTO_PALABRA = 'Palabra de'
TEXTO_LETRAS = 'letras'
TEXTO_DEFINICION = 'Definicion'
TEXTO_INGRESAR_PALABRA = "Ingrese palabra"
TEXTO_ADVERTENCIA = "La longitud no es la indicada, Por favor vuelva a ingresar"
TEXTO_ERROR = "Error,La palabra contiene caracteres invalidos"
TEXTO_CORRECION = 'Palabra incorrecta , La palabra es'
MENSAJE_ACIERTO = "a"
MENSAJE_INCORRECTO = "e" 

#---------- TABLERO ----------- #
def tablero(lista_letras,lista_aciertos = []):
    tablero_letras = ""
    tablero_aciertos = ""
    #Creamos el tablero a partir de la cantidad de letras que se le introduce
    for element in range(len(lista_letras)):
        tablero_letras += "[" + lista_letras[element].upper() + "]"
        if len(lista_aciertos) > element :
            tablero_aciertos +=  "["+lista_aciertos[element]+"]" 
        else:
            tablero_aciertos += "[ ]"
    print(f"{tablero_letras}\n{tablero_aciertos}")
#Mostramos en pantalla la cantidad de aciertos y errores del jugador
def mostrar_aciertos_errores(aciertos = 0,errores = 0):
    print(f"{TEXTO_ACIERTO}: {aciertos}\n{TEXTO_ERRORES}: {errores}")

# Informacion de la palabra candidata a adivinar
def informacion_palabra(dicc_palabras,caracter = 0,definicion =1):
    lista_letras = list(dicc_palabras.keys())
    lista_palabras = list(dicc_palabras.values())
    print(f"{TEXTO_TURNO} {lista_letras[caracter].upper()} - {TEXTO_PALABRA} {len(lista_palabras[caracter][0])} {TEXTO_LETRAS}")
    print(f"{TEXTO_DEFINICION}: {lista_palabras[caracter][definicion]}")

def aplanar_palabra(palabra):
    '''
    >>> aplanar_palabra("JOSE")
    'jose'
    >>> aplanar_palabra("CANCIÓN")
    'cancion'
    >>> aplanar_palabra("EjEcuCióN")
    'ejecucion'
    '''
    #la palabra 
    minuscula = palabra.lower()
    termino = ""
    for i in range(len(minuscula)):
        caracter = minuscula[i]
        if caracter == "á":
            caracter = 'a'
        elif caracter == "é":
            caracter = 'e'
        elif caracter == "í":
            caracter = 'i'
        elif caracter == "ó":
            caracter = 'o'
        elif caracter == "ú":
            caracter = 'u'
        termino += caracter 
    return termino
    

# Validamos que sea una palabra correcta 
def validar_palabra_ingresada(palabra):
    '''
    >>> validar_palabra_ingresada("terminal")
    True
    >>> validar_palabra_ingresada("CANCIÓN")
    True
    >>> validar_palabra_ingresada("Ju#n")
    False
    >>> validar_palabra_ingresada("Ale123")
    False
    >>> validar_palabra_ingresada("ar bol")
    False
    '''
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
    return validar
    #LIMACHI CORDERO, ALEX​

# Solicitamos al usuario que ingrese una palabra alfabetica 
def ingresar_palabra():
    palabra = input(f"{TEXTO_INGRESAR_PALABRA}:")
    termino = aplanar_palabra(palabra)
    return termino
    #LIMACHI CORDERO, ALEX​

def comparar_palabras(palabra_adivinar):
    palabra = ingresar_palabra()
    validar = validar_palabra_ingresada(palabra)
    if validar:
        LONGITUD_PALABRA_ADIVINAR = len(palabra_adivinar)
        LONGITUD_PALABRA = len(palabra)
        while LONGITUD_PALABRA != LONGITUD_PALABRA_ADIVINAR and validar:
            print(f"----------------------------------------\n{TEXTO_ADVERTENCIA}")
            palabra = ingresar_palabra()
            validar = validar_palabra_ingresada(palabra)
            if validar:
                LONGITUD_PALABRA = len(palabra)
            else:
                print(f"--------------\n{TEXTO_ERROR}")
    else:
        print(f"--------------\n{TEXTO_ERROR}")
    return palabra        


#Interactuamos con el jugador 
def interactuar(dicc_palabras):
    lista_letras = list(dicc_palabras.keys())
    lista_palabras = list(dicc_palabras.values())
    resumen = []
    lista_aciertos = []
    acierto = 0
    errores = 0
    indice = 0
    DEFINICION = 1
    while indice < len(lista_letras):
        print("---------------------------------------------")
        tablero(lista_letras,lista_aciertos)
        mostrar_aciertos_errores(acierto,errores)
        informacion_palabra(lista_letras,lista_palabras,indice,DEFINICION)
        palabra = comparar_palabras(lista_palabras[indice][0])
        termino = aplanar_palabra(lista_palabras[indice][0])
        if palabra == termino:
            acierto += 1
            lista_aciertos.append(MENSAJE_ACIERTO)
        else:
            errores +=1
            lista_aciertos.append(MENSAJE_INCORRECTO)
            print("--------------------")
            print(f"{TEXTO_CORRECION}: {lista_palabras[indice][0]}")
        resumen.append(palabra)
        indice+=1
    '''Almacenamos todas las palabras en una lista para despues hacer el resumen'''
    tablero(lista_letras,lista_aciertos)
    return resumen
    #LIMACHI CORDERO, ALEX​


# Unimos todas las funciones para crear la  etapa 1 "Interracion con el Jugador"
def iniciar_juego(dicc_palabras):
    """
    letrasElegidas: lista de letras elegidas
    Palabras: lista de palabras candidatas
    return: lista de palabras ingresadas por el usuario
    """
    resumen = interactuar(dicc_palabras)
    return resumen
    #LIMACHI CORDERO, ALEX​

#print(aplanar_palabra("EjEcuCióN"))
print(doctest.testmod())





