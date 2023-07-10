from dinamica_juego_v1 import comparar_palabras,aplanar_palabra
from configuracion_juego import leer_configuracion
from gestor_diccionario import generar_dicc_segun_configuracion

'#--------------------------------ETAPA 9----------------------#'


#---------- VARIABLES DE TEXTO----------------
TEXTO_CANTIDAD_LETRAS_ROSCO = "CANTIDAD_LETRAS_ROSCO"
TEXTO_MAXIMO_PARTIDAS = "MAXIMO_PARTIDAS"
TEXTO_PUNTAJE_ACIERTO = "PUNTAJE_ACIERTO"
TEXTO_PUNTAJE_DESACIERTO = "PUNTAJE_DESACIERTO"
TEXTO_JUGADORES = "Jugadores"
TEXTO_ACIERTOS = "Acierto"
TEXTO_ERRORES = "Error"
TEXTO_TURNO_JUGADOR = "Turno jugador"
TEXTO_TURNO_LETRA = "Turno letra"
TEXTO_LETRA =  "letra" 
TEXTO_PALABRA = "Palabra de"
TEXTO_DEFINICION = "Definicion"
TEXTO_INCORRECTO = "Incorrecto"
TEXTO_JUGADOR = "Jugador"
TEXTO_PALABRA_CORRECTA = "Palabra Correcta"
TEXTO_PREGUNTA = 'Desea volver a jugar'
TEXTO_ERROR = "Error, Por favor vuelve a ingresar un numero valido"
TEXTO_REPORTE_FINAL = 'Reporte final'
TEXTO_PARTIDAS_JUGADAS = 'Partidas Jugadas'
TEXTO_PUNTOS = 'puntos'
TEXTO_PUNTAJE_PARTIDA = "Puntaje de la partida"
TEXTO_PUNTAJE_PARCIAL = "Puntaje parcial"
TEXTO_SI = '[Si/s]'
TEXTO_NO = '[No/n]'
MENSAJE_CORRECTO = "a"
MENSAJE_INCORRECTO = "e"

#---- MOSTRAR TABLERO --- #
def tablero(lista_letras,lista_turno=[],lista_aciertos =[]):
    tablero_letras = ""
    tablero_turno = ""
    tablero_aciertos = ""
    for element in range(len(lista_letras)):
        tablero_letras += "["+ lista_letras[element].upper() + "]"
        if len(lista_turno) > element:
            tablero_turno += "[" +lista_turno[element]+"]"
        else:
            tablero_turno += "[ ]"
        if len(lista_aciertos) > element:
            tablero_aciertos += "["+lista_aciertos[element]+"]"
        else:
            tablero_aciertos += "[ ]"
    print(f"{tablero_letras}\n{tablero_turno}\n{tablero_aciertos}\n")

# Creo un diccionario que almacena los valores de aciertos y errores de cada jugador
def diccionario_jugadores(lista_jugadores):
    '''
    Recibe un lista_jugadores y retorna un diccionario donde se almacena la posicion, la cantidad de aciertos y errores del jugador
    ejemplo: dicc_participantes = {"nombre":[posicion,ACIERTO,ERRORES]}
    '''
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
    print(f"{TEXTO_JUGADORES}:")
    for clave,valor in dicc_participantes.items():
        print(f"{valor[POSICION]}. {clave} - {TEXTO_ACIERTOS}: {valor[ACIERTO]} - {TEXTO_ERRORES}: {valor[ERRORES]}")
    print()

def interactuar_usuario(dicc_participantes,dicc_palabras):
    indice = 0
    lista_jugadores = list(dicc_participantes.keys())
    lista_letras = list(dicc_palabras.keys())
    lista_palabras = list(dicc_palabras.values())
    lista_turno = []
    lista_aciertos = []
    posicion = 0
    DEFINICION =1
    ACIERTOS = 1
    ERRORES = 1
    lista_registro = []
    cant_jugadores = len(lista_jugadores)
    while indice < len(lista_letras):
        if cant_jugadores <= posicion:
            posicion = 0
        jugador = f"{dicc_participantes[lista_jugadores[posicion]][0]}"
        continuar= True
        while continuar and indice < len(lista_letras):
            print("----------------------------------------")
            tablero(lista_letras,lista_turno,lista_aciertos)
            imprimir_jugadores(dicc_participantes)
            print(f"{TEXTO_TURNO_JUGADOR} {dicc_participantes[lista_jugadores[posicion]][0]}. {lista_jugadores[posicion]} - {TEXTO_LETRA} {lista_letras[indice].upper()} - {TEXTO_PALABRA} {len(lista_palabras[indice][0])} {TEXTO_LETRA}")
            print(f"{TEXTO_DEFINICION}: {lista_palabras[indice][DEFINICION]}")
            #soluciones
            #print(f"{lista_palabras[indice][0]}")
            palabra = comparar_palabras(lista_palabras[indice][0])
            termino = aplanar_palabra(lista_palabras[indice][0])
            if palabra == termino:
                dicc_participantes[lista_jugadores[posicion]][1] += ACIERTOS
                lista_turno.append(jugador)
                lista_aciertos.append(MENSAJE_CORRECTO)
            else:
                dicc_participantes[lista_jugadores[posicion]][2] += ERRORES
                lista_turno.append(jugador)
                lista_aciertos.append(MENSAJE_INCORRECTO)
                print("-----------------------------------")
                print(f"{TEXTO_INCORRECTO},{TEXTO_PALABRA_CORRECTA}: {lista_palabras[indice][0]}")
                continuar = False
            lista_registro.append([jugador,lista_jugadores[posicion],lista_letras[indice],palabra])
            indice +=1
        posicion += 1
    tablero(lista_letras,lista_turno,lista_aciertos)
    return lista_registro

def resumen_partida(dicc_palabras,dicc_participantes,dicc_puntaje ={}):
    lista_resumen = interactuar_usuario(dicc_participantes,dicc_palabras)
    lista_palabras = list(dicc_palabras.values())
    INICIAL =0
    PARCIAL =0
    PUNTAJE_ACIERTO = int(leer_configuracion()[TEXTO_PUNTAJE_ACIERTO])
    PUNTAJE_DESACIERTO = -int(leer_configuracion()[TEXTO_PUNTAJE_DESACIERTO])
    for j in range(len(lista_resumen)):
        posicion = lista_resumen[j][0]
        nombre = lista_resumen[j][1]
        letra = lista_resumen[j][2]
        palabra = lista_resumen[j][3]
        if nombre not in dicc_puntaje:
            dicc_puntaje[nombre] = [INICIAL,PARCIAL]
        if palabra == lista_palabras[j][0]:
            print(f"{TEXTO_TURNO_LETRA} {letra.upper()} - {TEXTO_JUGADOR} {posicion}.{nombre} - {TEXTO_PALABRA} {len(palabra)} {TEXTO_LETRA} - {TEXTO_ACIERTOS} - {palabra}")
            dicc_puntaje[nombre][1] += PUNTAJE_ACIERTO
        else:
            print(f"{TEXTO_TURNO_LETRA} {letra.upper()} - {TEXTO_JUGADOR} {posicion}.{nombre} - {TEXTO_PALABRA} {len(lista_palabras[j][0])} {TEXTO_LETRA} - {palabra} - {TEXTO_ERRORES} - {TEXTO_PALABRA_CORRECTA}: {lista_palabras[j][0]}")
            dicc_puntaje[nombre][1] += PUNTAJE_DESACIERTO

        
def imprimir_puntaje(dicc_puntaje,dicc_participantes):
    '''
    Imprimimos en pantalla los puntajes de la partida que se juega
    Parametros:
    #dicc_puntaje = es lo que utilizaremos en la funcion resumen_partida()
    '''
    print(f"\n\n{TEXTO_PUNTAJE_PARTIDA}:")
    for clave,valor in dicc_puntaje.items():   
        print(f"{dicc_participantes[clave][0]} {clave} - ({valor[1]}) {TEXTO_PUNTOS}")
    print(f"\n\n{TEXTO_PUNTAJE_PARCIAL}:")
    for clave,valor in dicc_puntaje.items():     
        print(f"{dicc_participantes[clave][0]}. {clave} - ({valor[0]}) {TEXTO_PUNTOS}")
    print()
    #Sumo los puntajes de la partida en el valor de INICIO y reseteo el parcial
    for clave,valor in dicc_puntaje.items():
        valor[0] += valor[1]
        valor[1] = 0
    #LIMACHI CORDERO, ALEX​

def imprimir_puntaje_final(dicc_puntos,dicc_participantes,contador = 1):
    '''
    Imprime los puntos finales de cada usuario segun la cantidad de partidas que se haya jugado
    '''
    print(f"\n\n{TEXTO_REPORTE_FINAL}: ")
    print(f"{TEXTO_PARTIDAS_JUGADAS}: {contador}")
    for nombre,puntos in dicc_puntos.items():
        print(f"{dicc_participantes[nombre][0]}. {nombre} - ({puntos[0]}) {TEXTO_PUNTOS}")
    print()
    #LIMACHI CORDERO, ALEX​

def orden_alfab_breve(palabra):
    alfabeto={
        "s": 1, "S": 1,
        "n": 2, "N": 2,
        "i": 3, "I": 3, "í": 3, "Í": 3,
        "o": 4, "O": 4, "ó": 4, "Ó": 4,
    }
    indice = 0
    equivalencia_numerica = []
    while indice < len(palabra):
        if palabra[indice] in alfabeto.keys():
            equivalencia_numerica.append(alfabeto[palabra[indice]])
        else:
            equivalencia_numerica.append(100)
        indice +=1
    return equivalencia_numerica


def validar_jugar_de_nuevo():
    respuesta = input(f"{TEXTO_PREGUNTA}?:\n{TEXTO_SI}\n{TEXTO_NO}\n")
    if  orden_alfab_breve(respuesta) == orden_alfab_breve("si") or orden_alfab_breve(respuesta) == orden_alfab_breve("s"):
        respuesta = 1
    elif orden_alfab_breve(respuesta) == orden_alfab_breve("no") or orden_alfab_breve(respuesta) == orden_alfab_breve("n"):
        respuesta = 2
    else:
        print(f"-------------------\n{TEXTO_ERROR}\n------------------------")
        print("Por favor ingrese si o no")
        validar_jugar_de_nuevo()
    return respuesta

def iniciar_partida(lista_jugadores,dicc_puntaje = {},contador_partidas=1):
    '''
    Iniciamos el juego con los datos obtenidos y unimos todas las funciones anteriores
    Parametro:
    #Lista_jugadores = una lista que contiene los jugadores, esta lista se obtiene de la etapa 7 Ejecutar_Juego()
    Retorna la respuesta que haya ingresado el usuario si desea volver a jugar o no
    '''
    diccionario_palabras = generar_dicc_segun_configuracion()
    dicc_participantes = diccionario_jugadores(lista_jugadores)
    resumen_partida(diccionario_palabras,dicc_participantes,dicc_puntaje)
    imprimir_puntaje(dicc_puntaje,dicc_participantes)
    MAXIMO_PARTIDAS = int(leer_configuracion()[TEXTO_MAXIMO_PARTIDAS])
    if contador_partidas <= MAXIMO_PARTIDAS:
        SI = 1
        NO = 2
        respuesta = validar_jugar_de_nuevo() if contador_partidas < MAXIMO_PARTIDAS else NO
        if respuesta == SI:
            contador_partidas +=1
            respuesta = iniciar_partida(lista_jugadores,dicc_puntaje,contador_partidas)
        elif respuesta == NO and contador_partidas < MAXIMO_PARTIDAS:
            imprimir_puntaje_final(dicc_puntaje,dicc_participantes,contador_partidas)
    else:
        imprimir_puntaje_final(dicc_puntaje,dicc_participantes,contador_partidas)    
    return respuesta

#iniciar_partida(["alex","usuario"])

#LIMACHI CORDERO, ALEX​
