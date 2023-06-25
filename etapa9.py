from etapa1 import Preguntar , Verificar
from datos  import obtener_lista_definiciones 
from etapa3 import integrar_etapa_3
from set_herramientas import extraer_claves_coincidentes
from etapa2 import integrar_etapa_2
from etapa7 import Interfaz

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
    print(f"{tablero_letras}\n{tablero_turno}\n{tablero_aciertos}\n")

# Creo un diccionario que almacena los valores de aciertos y errores de cada jugador
def Participantes(lista_jugadores):
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
    print("Jugadores:")
    for clave,valor in dicc_participantes.items():
        print(f"{valor[POSICION]}. {clave} - Aciertos: {valor[ACIERTO]} - Errores: {valor[ERRORES]}")
    print()

# Importamos de la etapa 1 la funcion preguntar() y verificar() para validar la palabra que ingresa el usuario
def Interactuar(dicc_participantes,lista_palabras,lista_letras):
    '''
    Recibe como parametro:
    dicc_participantes = {"nombre":[POSICION,ACIERTO,ERRORES]}
    lista_letras = ["a,"e",etc..] segun la cantidad que haya elegido el usuario
    lista_palabras = [["argentina","pais"],etc...] una lista anidada con las palabras y definiciones
    # Esta funcion devuelve un registro de cada usuario segun lo que haya ingresado
    ejemplo: dicc_resumen = {"nombre":["argentina",etc..],"nombre2:["argentina,etc..]...}
    '''
    indice = 0
    lista_jugadores = list(dicc_participantes.keys())
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
        jugador = f"{dicc_participantes[lista_jugadores[posicion]][0]}"
        continuar= True
        while continuar and indice < len(lista_letras):
            print("----------------------------------------")
            tablero(lista_letras,lista_turno,lista_aciertos)
            imprimir_jugadores(dicc_participantes)
            print(f"Turno Jugador {dicc_participantes[lista_jugadores[posicion]][0]}. {lista_jugadores[posicion]} - letra {lista_letras[indice].upper()} - Palabra de {len(lista_palabras[indice][0])} letras")
            print(f"Definicion: {lista_palabras[indice][DEFINICION]}")
            palabra = Preguntar()
            validar = Verificar(palabra)
            if validar and palabra == lista_palabras[indice][0]:
                # 'dicc_participantes[lista_jugadores[posicion]][1]'
                # busco primero el nombre en el diccionario(lista_jugadores[posicion]) y sumo el valor segun si
                # la palabra es acertada o errada 
                dicc_participantes[lista_jugadores[posicion]][1] += ACIERTOS
                lista_turno.append(jugador)
                lista_aciertos.append(A)
            else:
                dicc_participantes[lista_jugadores[posicion]][2] += ERRORES
                lista_turno.append(jugador)
                lista_aciertos.append(E)
                print("-----------------------------------")
                print(f"Palabra incorrecta, la palabra es: {lista_palabras[indice][0]}")
                continuar = False
            if lista_jugadores[posicion] in dicc_registro:
                dicc_registro[lista_jugadores[posicion]].append(palabra)
            else:
                dicc_registro[lista_jugadores[posicion]] = [palabra]
            indice +=1
        posicion += 1
    tablero(lista_letras,lista_turno,lista_aciertos)
    return dicc_registro

def Resumen(dicc_resumen,letras,palabras,dicc_participantes,dicc_puntaje ={}):
    '''
    Verificamos que el usuario haya ingresado las palabras correspondientes a adivinar
    Parametros:
    dicc_resumen, es el diccionario que viene de la funcion Interactuar()

    letras, la lista de letras candidatas 

    palabras, lista de palabras junto a sus definiciones a adivinar

    dicc_participantes, un diccionario donde obtenemos la POSICION del jugador

    dicc_puntaje, un paramaetro por default que se almacena los puntos de cada jugador 
    ejemplo: dicc_puntos = {"nombre":[INICIAL,PARCIAL]},
    INICIAL =0 porque empieza recien la partida
    PARCIAL = Segun los puntos que se haya obtenido por cada palabra adivinada o errada
    '''
    indice = 0
    INICIAL =0
    PARCIAL =0
    PUNTAJE_ACIERTO = 10
    PUNTAJE_DESACIERTO = -3
    for clave,valor in dicc_resumen.items():
        if clave not in dicc_puntaje:
            dicc_puntaje[clave] = [INICIAL,PARCIAL]
        for i in range(len(valor)):
            palabra = valor[i]
            if palabra == palabras[indice][0]:
                print(f"Turno letra {letras[indice].upper()} - Jugador {dicc_participantes[clave][0]} {clave} - Palabra de {len(palabras[indice][0])} letras - acierto - {palabra}")
                dicc_puntaje[clave][1] += PUNTAJE_ACIERTO
            else:
                print(f"Turno de la letra {letras[indice].upper()} - Jugador {dicc_participantes[clave][0]} {clave} - Palabra de {len(palabras[indice][0])} letras - {palabra} - error - Palabra Correcta: {palabras[indice][0]}")
                dicc_puntaje[clave][1] += PUNTAJE_DESACIERTO
            indice+=1
        
def ImprimirPuntaje(dicc_puntaje,dicc_participantes):
    '''
    Imprimimos en pantalla los puntajes de la partida que se juega
    Parametros:
    #dicc_puntaje = es lo que utilizaremos en la funcion Resumen()
    '''
    print("\n\nPuntaje de la partida:")
    for clave,valor in dicc_puntaje.items():   
        print(f"{dicc_participantes[clave][0]} {clave} - ({valor[1]}) puntos")
    print("\n\nPuntaje parcial:")
    for clave,valor in dicc_puntaje.items():     
        print(f"{dicc_participantes[clave][0]}. {clave} - ({valor[0]}) puntos")
    print()
    #Sumo los puntajes de la partida en el valor de INICIO y reseteo el parcial
    for clave,valor in dicc_puntaje.items():
        valor[0] += valor[1]
        valor[1] = 0

def ImprimirFinal(dicc_puntos,dicc_participantes,contador = 1):
    '''
    Imprime los puntos finales de cada usuario segun la cantidad de partidas que se haya jugado
    '''
    print("\n\nReporte final: ")
    print(f"Partidas Jugadas: {contador}")
    for nombre,puntos in dicc_puntos.items():
        print(f"{dicc_participantes[nombre][0]}. {nombre} - ({puntos[0]}) puntos")
    print()

def Datos():
    '''
    Extreamos los datos de las anteriores etapas.
    Retorna una lista de Letras a Jugar, y la Lista de palabras junto a sus definciones
    
    '''
    datos = obtener_lista_definiciones()
    diccionario = integrar_etapa_2(datos)
    letras,palabra = integrar_etapa_3(diccionario,10)
    palabra_definicion = extraer_claves_coincidentes(diccionario,palabra)                                            
    return letras,palabra_definicion

def Partida(lista_jugadores,dicc_puntaje = {}):
    '''
    Iniciamos el juego con los datos obtenidos y unimos todas las funciones anteriores
    Parametro:
    #Lista_jugadores = una lista que contiene los jugadores, esta lista se obtiene de la etapa 7 Ejecutar_Juego()
    Retorna la respuesta que haya ingresado el usuario si desea volver a jugar o no
    '''
    letras,palabra_definicion = Datos()
    dicc_participantes = Participantes(lista_jugadores)
    dicc_resumen = Interactuar(dicc_participantes,palabra_definicion,letras)
    Resumen(dicc_resumen,letras,palabra_definicion,dicc_participantes,dicc_puntaje)
    ImprimirPuntaje(dicc_puntaje,dicc_participantes)
    contador_partidas = 1
    respuesta = int(input(f"Desea volver a jugar?:\n1.si\n2.no\n"))
    SI =1
    if respuesta == SI:
        respuesta = Partida(lista_jugadores,dicc_puntaje)
        contador_partidas +=1
    else:
        respuesta = ImprimirFinal(dicc_puntaje,dicc_participantes,contador_partidas)
    return respuesta
    
def Jugar(arUser):
    '''
    Integramos todo lo obtenido e iniciamos el juego
    Parametro: Recibe un archivo.csv que contenga los usuarios registrados 
    '''
    lista_jugadores = Interfaz(arUser)
    if lista_jugadores:
        Partida(lista_jugadores)

archivo = "usuarios.csv"   
print(Jugar(archivo))






