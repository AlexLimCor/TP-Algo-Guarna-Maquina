from resumen_juego import generar_resumen_partida

#___________________funciones complementarias_____________________
#______________Colores______________
rojo = '\033[91m'
azul = '\033[94m'
reset = '\033[0m'
def imprimir_diccionario_valores(diccionario):
    for valor in diccionario.values():
        print(valor)
    #CRUZ, ARIEL CARLOS LEONARDO​
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

#_______________________________Etapa 5_______________________________________
def contador_puntaje(diccionario_puntaje,PUNTAJE_ACIERTO = 10,PUNTAJE_DESACIERTO = 3):
    
    """
    Parametros:
            diccionario_puntaje: diccionario con las claves "aciertos" y "errores" y sus respectivos valores
    return: puntaje total intg
        
    """
    puntaje = diccionario_puntaje["aciertos"]*PUNTAJE_ACIERTO - diccionario_puntaje["errores"]*PUNTAJE_DESACIERTO
    return puntaje  
    #CRUZ, ARIEL CARLOS LEONARDO​

def generar_resumen_puntaje(diccionario):
    """
    Parametros:
            diccionario: clave: letra, valor: lista con [palabra , respuesta]
    return: diccionario con clave aciertos y errores y sus respectivos valores
    """
    diccionario_puntaje = {
    "aciertos":0,
    "errores":0
    }
    diccionario_resumen = {}
    for letra in diccionario.keys():
        palabra = diccionario[letra][0]
        respuesta = diccionario[letra][1]
        mensaje_base = f"Turno de letra {letra.upper()} - Palabra de {len(palabra)} letras - "
        diccionario_resumen[letra] = mensaje_base
        
        if respuesta == palabra:
            diccionario_resumen[letra] += f"{palabra} - acierto"
            diccionario_puntaje["aciertos"] += 1

        else:
            diccionario_resumen[letra] += f"{respuesta} - error - Palabra correcta {palabra}"
            diccionario_puntaje["errores"] += 1

        imprimir_diccionario_valores(diccionario_resumen)
    return diccionario_puntaje
    #CRUZ, ARIEL CARLOS LEONARDO​

def validar_jugar_de_nuevo():
    """
    La funcion valida si el usuario quiere volver a jugar o no
    return: 1 si quiere volver a jugar, 2 si no quiere volver a jugar
    """
    respuesta = input("Desea volver a jugar? \n[si/s]\n[no/n]\n")
    if  orden_alfab_breve(respuesta) == orden_alfab_breve("si") or orden_alfab_breve(respuesta) == orden_alfab_breve("s"):
        respuesta = 1
    elif orden_alfab_breve(respuesta) == orden_alfab_breve("no") or orden_alfab_breve(respuesta) == orden_alfab_breve("n"):
        respuesta = 2
    else:
        print(f"{rojo}Respuesta invalida{reset}\n")
        print("Por favor ingrese si o no")
        validar_jugar_de_nuevo()
    return respuesta
    #CRUZ, ARIEL CARLOS LEONARDO​
    
def jugar_de_nuevo(cantidad_letras,puntaje_inicial):
    diccionario = generar_resumen_partida(cantidad_letras)
    return jugar_pasapalabras(diccionario,cantidad_letras,puntaje_inicial)
    #CRUZ, ARIEL CARLOS LEONARDO​


def jugar_pasapalabras(diccionario_juego,cantidad_letras,puntaje_inicial=0):
    """
    Parametros:
        diccionario: clave: letra, valor: lista con [palabra , respuesta]
        cantidad_letras: numero entero
        punaje_inicial: numero entero
    return: 
        volver_jugar: Funcion recursiva que permite volver a jugar o mostrar el puntaje final 
    """
    diccionario_puntaje = generar_resumen_puntaje(diccionario_juego)
    puntaje = contador_puntaje(diccionario_puntaje) + puntaje_inicial
    print(f"Su puntaje es {puntaje}")

    volver_jugar = validar_jugar_de_nuevo()

    volver_jugar = jugar_de_nuevo(cantidad_letras,puntaje) if volver_jugar == 1 else print(f"\n\n\n{azul}Gracias por jugar.{reset}\nSu puntaje final es {puntaje}")
    return volver_jugar
    #CRUZ, ARIEL CARLOS LEONARDO​

