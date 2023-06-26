import random

#______________________Funciones complementarias_______________________
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

def generar_letras_aleatorias(cantidad_letras):
    """
    La funcion recibe como parametro un numero entero y devuelve una lista de letras aleatorias 
    con longitud igual al numero recibido
    """
    letras=['a','b','c','d','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    #Elegimos 10 letras aleatorias
    letras_elegidas=random.sample(letras,cantidad_letras)
    #Ordenamos las letras alfabeticamente
    letras_elegidas = sorted(letras_elegidas, key=orden_alfabetico)
    return letras_elegidas

def seleccionar_clave_aleatoria_por_letra(lista_palabras,letra):
    """
    La funcion recibe como parametro un lista_palabras y una letra y retorna una clave(palabra) aleatoria 
    que empieza con la letra recibida
    """
    inicial = 0
    letra = orden_alfabetico(letra)
    listas_claves_candidatas = [clave for clave in lista_palabras if orden_alfabetico(clave)[inicial] in letra]
    palabra_aleatoria_elegida = random.choice(listas_claves_candidatas)
    return palabra_aleatoria_elegida


def obtener_lista_palabras(lista_palabras,letras_participantes):
    """
    la funcion recibe como parametro un lista_palabras y una lista de letras
    y devuelve una lista de palabras aleatorias que empiezan con cada letra participante
    """
    lista_palabras_elegidas = []
    for letra in letras_participantes:
        letra_elegida = seleccionar_clave_aleatoria_por_letra(lista_palabras,letra)
        lista_palabras_elegidas.append(letra_elegida)
    return lista_palabras_elegidas


def integrar_etapa_3(lista_palabras,cantidad_letras):
    """
    Parametros:
            lista_palabras:{"palabra":definicion,"palabra":definicion,...}
            cantidad_letras:numero entero
    return: una lista de listas [[letras_participantes,lista_palabras_elegidas]]

    La funcion recibe como parametro un lista_palabras y un numero entero y devuelve una lista de palabras
    aleatorias que empiezan con cada letra participante
    """
    letras_participantes = generar_letras_aleatorias(cantidad_letras)
    lista_palabras_elegidas = obtener_lista_palabras(diccionario,letras_participantes)
    resultado = [letras_participantes,lista_palabras_elegidas]
    return resultado
