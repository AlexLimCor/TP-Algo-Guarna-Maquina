from datos import obtener_lista_definiciones
from set_herramientas import orden_alfabetico,imprimir_diccionario
import doctest

#_______________________Funciones complementarias_______________________
datos = obtener_lista_definiciones()
def quitar_tilde(vocal_tildada):
    """
    Reemplaza una vocal con tilde por su equivalente sin tilde.
    >>> quitar_tilde('á')
    'a'
    >>> quitar_tilde('é')
    'e'
    >>> quitar_tilde('í')
    'i'
    >>> quitar_tilde('ó')
    'o'
    >>> quitar_tilde('ú')
    'u'
    
    """
    vocales_tildadas = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'
    }
    vocal_sin_tilde = vocales_tildadas[vocal_tildada]

    return vocal_sin_tilde


print(doctest.testmod())




def ordenar_diccionario(diccionario):
    """
    La funcion recibe como parametro un diccionario y devuelve un diccionario ordenado alfabeticamente
    """
    diccionario_ordenado = {}
    #Se genera una lista de tuplas ordenadas alfabeticamente
    lista_items = sorted(diccionario.items(), key=lambda x:orden_alfabetico(x[0]))
    for elemento in lista_items:
        diccionario_ordenado[elemento[0]] = elemento[1]
    return diccionario_ordenado

#_______________________ETAPA 2_______________________

#Se genera un diccionario con las palabras que cumplen con la condicion establecida

def generador_diccionario(diccionario_datos):
    """
    Genera un diccionario con las palabras que cumplen con la condicion
    """
    palabras_candidatas = {}
    LONG_MIN = 5
    PALABRA = 0
    DEFINICION = 1
    for elemento in diccionario_datos:
        if len(elemento[PALABRA]) >= LONG_MIN:
            #Armado del diccionario con la condicion
            palabras_candidatas[elemento[PALABRA]] = elemento[DEFINICION]
    print(f"Total de palabras {len(palabras_candidatas)}")
    return palabras_candidatas


#Se genera un diccionario con la cantidad de palabras que hay por cada letra

def contador_letras(diccionario):
    """
    La funcion recibe como parametro un diccionario y devuelve un diccionario con la 
    cantidad de palabras que hay por cada letra
    """
    VOCALES_TILDE = ['á', 'é', 'í', 'ó', 'ú']
    PALABRA = 0
    INICIAL = 0
    resumen_diccionario = {}

    for elemento in diccionario:
        letra_inicial = elemento[PALABRA][INICIAL]
        if letra_inicial in VOCALES_TILDE: 
            #Si la letra inicial tiene tilde se le quita 
            letra_inicial = quitar_tilde(letra_inicial)
        if letra_inicial in resumen_diccionario.keys():
            resumen_diccionario[letra_inicial] +=1
        else:
            resumen_diccionario[letra_inicial] = 1
    resumen_diccionario = ordenar_diccionario(resumen_diccionario)
    return resumen_diccionario

def integrar_etapa_2(datos):
    """
    datos:lista de listas [[palabra,definicion],[palabra,definicion],...]
    retorna un diccionario {"palabra":definicion,"palabra":definicion,...}
    La funcion integra las funciones de la etapa 2
    """
    diccionario = generador_diccionario(datos)
    resumen_diccionario = contador_letras(datos)
    #imprimir_diccionario(resumen_diccionario)
    return diccionario