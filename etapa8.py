from etapa10 import designar_configuracion
from etapa3 import integrar_etapa_3

#_________________________Funciones complementarias___________________________
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

def extraer_claves_coincidentes(diccionario,lista_palabras):
    """
    La funcion recibe como parametro un diccionario y una lista de palabras 
    y devuelve una lista de listas con la palabra y su definicion
    """
    lista_definiciones = []
    for palabra, definicion in diccionario.items():
        if palabra in lista_palabras:
            lista_definiciones.append([palabra,definicion])
        lista_definiciones = sorted(lista_definiciones, key=lambda x: orden_alfabetico(x[0]))
    return lista_definiciones

excepciones = ["á","é","í","ó","ú","ñ"]

def leer_archivo(archivo, default):
    """
    Parametros: archivo(objeto de open) y cadena
    return: linea del archivo o cadena default si se termino de leer el archivo
    """
    linea = archivo.readline()
    return linea if linea else default

def generador_diccionario(diccionario_datos):
    """
    Genera un diccionario con las palabras que cumplen con la condicion
    """
    palabras_candidatas = {}
    PALABRA = 0
    DEFINICION = 1
    for elemento in diccionario_datos:
        #Armado del diccionario con la condicion
        palabras_candidatas[elemento[PALABRA]] = elemento[DEFINICION]
    return palabras_candidatas


def escribir_archivo(archivo, lista):
    """
    Parametros: archivo(objeto de open) y lista
    La funcion recibe como parametro un archivo y una lista y escribe en el archivo
    """
    for palabra,definicion in lista:
        archivo.write(f"{palabra},'{definicion}'\n")

def escribir_diccionario(longitud_minima_palabra):
    """
    Parametros: numero entero
    La funcion recibe como parametro un numero entero y escribe en un archivo csv las palabras y sus definiciones
    """
    palabras = open("definiciones_palabras\\palabras.txt","r",encoding='utf-8')
    definiciones = open("definiciones_palabras\\definiciones.txt","r",encoding='utf-8')
    diccionario = open("definiciones_palabras\\definiciones.csv","w",encoding='utf-8')
    palabras_candidatas = []
    linea_palabra = leer_archivo(palabras,"####")
    linea_definicion = leer_archivo(definiciones,"####")
    palabra = linea_palabra.rstrip('\n')
    definicion = linea_definicion.rstrip("\n")
    """
    Se fucionan los archivos que contiene las palabra y las definiciones en un solo archivo. 
    Se consideran que se termino de leer el archivo cuando se encuentra la cadena "####"
    """

    while palabra != "####" and definicion != "####":
        #print(definicion,"\n")
        if len(palabra) >= longitud_minima_palabra and palabra.isalpha(): 
            palabras_candidatas.append([palabra,definicion])
        linea_palabra = leer_archivo(palabras,"####")
        linea_definicion = leer_archivo(definiciones,"####")
        palabra = linea_palabra.rstrip('\n')
        definicion = linea_definicion.rstrip('\n')
    palabras.close()
    definiciones.close()
    #print(palabras_candidatas)
    palabras_candidatas = sorted(palabras_candidatas, key=lambda x:orden_alfabetico(x[0]))
    #print(diccionario)
    diccionario.write("palabra,definicion\n")
    escribir_archivo(diccionario,palabras_candidatas)
    diccionario.close()
escribir_diccionario(100)


def leer_diccionario():
    """
    La funcion lee el archivo csv y devuelve una lista de listas con las palabras y sus definiciones
    """
    lista_palabras = []
    with open("definiciones_palabras\\definiciones.csv","r",encoding='utf-8') as diccionario:
        linea = leer_archivo(diccionario,"####")
        linea_dicc = linea.rstrip("\n").split(",")
        while linea != "####":
            lista_palabras.append(linea_dicc)
            linea = leer_archivo(diccionario,"####")
            linea_dicc = linea.rstrip("\n").split(",")
    return lista_palabras


palabras_candidatas = [['árbol', 'definición1'], ['zorro', 'definición2'], ['ópera', 'definición3'], ['éxito', 'definición4'], ['ñandú', 'definición5']]
excepciones = {'á', 'é', 'í', 'ó', 'ú', 'ñ'}

sorted_palabras = sorted(palabras_candidatas, key=lambda x: correccion_alfabetica(x[0]) if x[0][0] not in excepciones else correccion_alfabetica(x[0]))
print(sorted_palabras)
