from datos import obtener_lista_definiciones
import random

# Etapa 2
datos = obtener_lista_definiciones()
def quitar_tilde(vocal_tildada):
    """
    Reemplaza una vocal con tilde por su equivalente sin tilde.
    """
    if vocal_tildada == 'á':
        return 'a'
    elif vocal_tildada == 'é':
        return 'e'
    elif vocal_tildada == 'í':
        return 'i'
    elif vocal_tildada == 'ó':
        return 'o'
    elif vocal_tildada == 'ú':
        return 'u'
    else:
        return vocal_tildada


def imprimir_diccionario(diccionario):
    for clave , valor in diccionario.items():
        print(f"{clave} : {valor} ")


def ordenar_diccionario(diccionario):
    diccionario_ordenado = {}
    lista_items = sorted(diccionario.items(), key=lambda x:x[0])
    for elemento in lista_items:
        diccionario_ordenado[elemento[0]] = elemento[1]
    return diccionario_ordenado

def generador_diccionario(diccionario_datos):
    """
    Genera un diccionario con las palabras que cumplen con la condicion de tener mas de 5 letras y 
    otro diccionario con la cantidad de palabras que hay por cada letra. 
    """
    palabras_candidatas = {}
    VOCALES_TILDE = ['á', 'é', 'í', 'ó', 'ú']
    LONG_MIN = 5
    PALABRA = 0
    DEFINICION = 1
    INICIAL = 0
    resumen_diccionario = {}

    for elemento in diccionario_datos:
        if len(elemento[PALABRA]) >= LONG_MIN:
            #Armado del diccionario con la condicion
            palabras_candidatas[elemento[PALABRA]] = elemento[DEFINICION]
            letra_inicial = elemento[PALABRA][INICIAL]
            #Armado del diccionario para mostrar el total de palabras que hay por cada letra
            if letra_inicial in VOCALES_TILDE: 
                #Si la letra inicial tiene tilde se le quita
                letra_inicial = quitar_tilde(letra_inicial)
            if letra_inicial in resumen_diccionario.keys():
                resumen_diccionario[letra_inicial] +=1
            else:
                resumen_diccionario[letra_inicial] = 1

    resumen_diccionario = ordenar_diccionario(resumen_diccionario)
    imprimir_diccionario(resumen_diccionario)
    print(f"Total de palabras {len(palabras_candidatas)}")
    ordenar_diccionario(resumen_diccionario)
    return palabras_candidatas

print(generador_diccionario(datos))