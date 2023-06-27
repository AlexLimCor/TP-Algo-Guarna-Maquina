from datos import obtener_lista_definiciones
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
    #CRUZ, ARIEL CARLOS LEONARDO​

print(doctest.testmod())

def orden_alfabetico(elemento):
    """
    la funcion recibe como parametro una elemento de caracteres y 
    devuelve una lista con la equivalencia numerica de cada letra. 
    Si la elemento es una lista, se toma el primer elemento.
    >>> orden_alfabetico("hola")
    [8, 16, 12, 1]
    >>> orden_alfabetico("manzana")
    [13, 1, 14, 27, 1, 14, 1]
    >>> orden_alfabetico("árbol")
    [1, 19, 2, 16, 12]
    >>> orden_alfabetico("último")
    [22, 12, 21, 9, 13, 16]
    """
    abecedario = {
    'a': 1, 'á': 1, 
    'b': 2, 
    'c': 3, 
    'd': 4, 
    'e': 5, 'é': 5, 
    'f': 6, 
    'g': 7, 
    'h': 8, 
    'i': 9, 'í': 9,
    'j': 10, 
    'k': 11, 
    'l': 12, 
    'm': 13, 
    'n': 14, 
    'ñ': 15, 
    'o': 16, 'ó': 16, 
    'p': 17, 
    'q': 18, 
    'r': 19,
    's': 20, 
    't': 21, 
    'u': 22, 'ú': 22,  'ü': 22,
    'v': 23, 
    'w': 24, 
    'x': 25, 
    'y': 26, 
    'z': 27
    }
    equivalencia_numerica = []
    for letra in elemento:
        equivalencia_numerica.append(abecedario[letra])
    return equivalencia_numerica
    #CRUZ, ARIEL CARLOS LEONARDO​



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
    #CRUZ, ARIEL CARLOS LEONARDO​




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
    #CRUZ, ARIEL CARLOS LEONARDO​


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
    #CRUZ, ARIEL CARLOS LEONARDO​

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
    #CRUZ, ARIEL CARLOS LEONARDO​ 