from etapa1 import Preguntar , Verificar
from datos  import obtener_lista_definiciones 
from etapa3 import integrar_etapa_3
from set_herramientas import extraer_claves_coincidentes
from etapa2 import integrar_etapa_2





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
    print()


# Importamos de la etapa 1 la funcion preguntar() y verificar() para validar la palabra que ingresa el usuario
def Interactuar(dicc_participantes,lista_palabras,lista_letras):
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


def Prueba(jugadores,palabras,letras):
    '''
    Por ultimo esta funcion recibe como parametro una lista de jugadores
    una lista de palabras anidadas junto con su definicion,
    una lista de letras seleccionadas,
    y retorna un diccionario que contiene como clave el jugador y como valor una 
    lista de palabras ingresadas por el usuario
    ej: dicc = {"alex":["argentina","brasil",etc....],"admin":["francia",etc...]
    '''
    dicc = dicc_jugadores(jugadores)
    resumen = Interactuar(dicc,palabras,letras)

    return resumen

def Resumen(dicc_resumen,letras,palabras,dicc_jugadores):
    indice = 0
    INICIAL =0
    PARCIAL =0
    PUNTAJE_ACIERTO = 10
    PUNTAJE_DESACIERTO = -3
    dicc_puntaje = {}
    for clave,valor in dicc_resumen.items():
        if clave not in dicc_puntaje:
            dicc_puntaje[clave] = [INICIAL,PARCIAL]
        for i in range(len(valor)):
            palabra = valor[i]
            if palabra == palabras[indice][0]:
                print(f"Turno letra {letras[indice].upper()} - Jugador {dicc_jugadores[clave][0]} {clave} - Palabra de {len(palabras[indice][0])} letras - acierto - {palabra}")
                dicc_puntaje[clave][1] += PUNTAJE_ACIERTO
            else:
                print(f"Turno de la letra {letras[indice].upper()} - Jugador {dicc_jugadores[clave][0]} {clave} - Palabra de {len(palabras[indice][0])} letras - {palabra} - error - Palabra Correcta: {palabras[indice][0]}")
                dicc_puntaje[clave][1] += PUNTAJE_DESACIERTO
            indice+=1
        
    return dicc_puntaje


def ImprimirPuntaje(dicc_puntaje,dicc2):
    print("\n\nPuntaje de la partida:")
    for clave,valor in dicc_puntaje.items():   
        print(f"{dicc2[clave][0]} {clave} - {valor[1]} puntos")
    print("\n\nPuntaje parcial:")
    for clave,valor in dicc_puntaje.items():     
        print(f"{dicc2[clave][0]}. {clave} - {valor[0]} puntos")
    print()

def ActPuntaje(dicc_puntaje):
    '''
    Invierto el diccionario para usarlo despues, el resultado seria lo siguiente dicc = {"clave1":[Final,Parcial]}
    '''
    dicc_actualizado = {}
    for clave,valor in dicc_puntaje.items():
        if clave not in dicc_actualizado:
            dicc_actualizado[clave] = [valor[1],valor[0]]
    return dicc_actualizado

def VolverJugar():
    respuesta = int(input(f"Desea volver a jugar?:\n1.si\n2.no\n"))    
    return respuesta


def Reunir(lista_jugadores):
    datos = obtener_lista_definiciones()
    diccionario = integrar_etapa_2(datos)
    letras,palabra = integrar_etapa_3(diccionario,10)
    palabra_definicion = extraer_claves_coincidentes(diccionario,palabra)
    dicc_participantes = dicc_jugadores(lista_jugadores)
    dicc_resumen = Interactuar(dicc_participantes,palabra_definicion,letras)
    dicc_puntaje = Resumen(dicc_resumen,letras,palabra_definicion,dicc_participantes)
    return dicc_puntaje


def Imprimir_Final(dicc,dicc_participantes,contador = 1):
    print("\n\nReporte final: ")
    print(f"Partidas Jugadas: {contador}")
    for nombre,puntos in dicc.items():
        print(f"{dicc_participantes[nombre][0]}. {nombre} - {puntos[0]} puntos")
    print()





def integrar(lista_jugadores,dicc_puntaje = {}):
    dicc_participantes = dicc_jugadores(lista_jugadores)
    dicc_puntaje = Reunir(lista_jugadores)
    ImprimirPuntaje(dicc_puntaje,dicc_participantes)
    contador_partidas = 1
    respuesta = VolverJugar()
    SI =1
    if respuesta == SI:
        respuesta = integrar(lista_jugadores,dicc_puntaje)
        contador_partidas +=1
    else:
        respuesta = Imprimir_Final(dicc_puntaje,dicc_participantes,contador_partidas)
    return respuesta
    
print(integrar(["alex","admin"]))






