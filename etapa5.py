from etapa4 import integrar_etapa4

#___________________funciones complementarias_____________________
#______________Colores______________
rojo = '\033[91m'
azul = '\033[94m'
reset = '\033[0m'
def imprimir_diccionario_valores(diccionario):
    for valor in diccionario.values():
        print(valor)
    #CRUZ, ARIEL CARLOS LEONARDO​


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

def generar_resumen(diccionario):
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


def jugar_de_nuevo(cantidad_letras,puntaje_inicial):
    diccionario = integrar_etapa4(cantidad_letras)
    return integrar_etapa_5(diccionario,cantidad_letras,puntaje_inicial)
    #CRUZ, ARIEL CARLOS LEONARDO​

def integrar_etapa_5(diccionario,cantidad_letras,puntaje_inicial=0):
    """
    Parametros:
        diccionario: clave: letra, valor: lista con [palabra , respuesta]
        cantidad_letras: numero entero
        punaje_inicial: numero entero
    return: 
        volver_jugar: Funcion recursiva que permite volver a jugar o mostrar el puntaje final 
    """
    diccionario_puntaje = generar_resumen(diccionario)
    puntaje = contador_puntaje(diccionario_puntaje) + puntaje_inicial
    print(f"Su puntaje es {puntaje}")


    volver_jugar = int(input("Desea volver a jugar? 1:si 2:no"))
    volver_jugar = jugar_de_nuevo(cantidad_letras,puntaje) if volver_jugar == 1 else print(f"\n\n\n{azul}Gracias por jugar.{reset}\nSu puntaje final es {puntaje}")
    return volver_jugar
    #CRUZ, ARIEL CARLOS LEONARDO​
