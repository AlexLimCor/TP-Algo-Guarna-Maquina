from palabras_aleatorias import seleccionar_palabras_aleatoria, orden_alfabetico
from configuracion_juego import leer_configuracion
import doctest
import os

#_________________________Funciones complementarias___________________________

def extraer_claves_coincidentes(diccionario,lista_palabras):
    """
    La funcion recibe como parametro un diccionario y una lista de palabras 
    y devuelve una lista de listas con la palabra y su definicion en orden alfabetico
    
    >>> extraer_claves_coincidentes({"hola":"saludo","casa":"lugar donde se habita"},["hola","casa"])
    [['casa', 'lugar donde se habita'], ['hola', 'saludo']]
    >>> extraer_claves_coincidentes({"alcohol":"sustancia","casa":"lugar donde se habita"},["alcohol","casa"])
    [['alcohol', 'sustancia'], ['casa', 'lugar donde se habita']]
    >>> extraer_claves_coincidentes({"ceremonia":"ritual","raton":"dispositivo de entrada"},["ceremonia","raton"])
    [['ceremonia', 'ritual'], ['raton', 'dispositivo de entrada']]
    """
    lista_clave_valor = []
    for palabra, definicion in diccionario.items():
        if palabra in lista_palabras:
            lista_clave_valor.append([palabra,definicion])
        lista_clave_valor = sorted(lista_clave_valor, key=lambda x: orden_alfabetico(x[0]))
    return lista_clave_valor
    #CRUZ, ARIEL CARLOS LEONARDO​


def leer_archivo(archivo, default):
    """
    Parametros: archivo(objeto de open) y cadena
    return: linea del archivo o cadena default si se termino de leer el archivo
    """
    linea = archivo.readline()
    return linea if linea else default
    #CRUZ, ARIEL CARLOS LEONARDO​

def transformador_lista_a_dicc(datos):
    """
    Genera un diccionario con las palabras que cumplen con la condicion

    >>> transformador_lista_a_dicc([["hola","saludo"],["casa","lugar donde se habita"]])
    {'hola': 'saludo', 'casa': 'lugar donde se habita'}
    >>> transformador_lista_a_dicc([["manzana","fruta"],["pera","fruta"],["casa","lugar donde se habita"]])
    {'manzana': 'fruta', 'pera': 'fruta', 'casa': 'lugar donde se habita'}
    >>> transformador_lista_a_dicc([["arbol","planta"],["casa","lugar donde se habita"]])
    {'arbol': 'planta', 'casa': 'lugar donde se habita'}
    """
    palabras_candidatas = {}
    PALABRA = 0
    DEFINICION = 1
    for elemento in datos:
        #Armado del diccionario con la condicion
        palabras_candidatas[elemento[PALABRA]] = elemento[DEFINICION]
    return palabras_candidatas
    #CRUZ, ARIEL CARLOS LEONARDO​


def escribir_archivo(archivo, lista):
    """
    Parametros: archivo(objeto de open) y lista
    La funcion recibe como parametro un archivo y una lista y escribe en el archivo
    """
    for palabra,definicion in lista:
        archivo.write(f"{palabra},'{definicion}'\n")
    #CRUZ, ARIEL CARLOS LEONARDO​

#_________________________Rutas de archivos____________________________________
definiciones_arc = os.path.join("recursos","definiciones.txt")
palabras_arc = os.path.join("recursos","palabras.txt")
diccionario_arc = os.path.join("recursos","diccionario.csv")

def escribir_dicc_csv(longitud_minima_palabra):
    
    
    """
    Parametros: numero entero
    La funcion recibe como parametro un numero entero y escribe en un archivo csv las palabras y sus definiciones
    """
    palabras = open(palabras_arc,"r",encoding='utf-8')
    definiciones = open(definiciones_arc,"r",encoding='utf-8')
    diccionario = open(diccionario_arc,"w",encoding='utf-8')
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
    #CRUZ, ARIEL CARLOS LEONARDO​


def leer_diccionario():
    """
    La funcion lee el archivo csv y devuelve una lista de listas con las palabras y sus definiciones
    """
    lista_palabras = []
    with open(diccionario_arc,"r",encoding='utf-8') as diccionario:
        linea = leer_archivo(diccionario,"####")
        linea_dicc = linea.rstrip("\n").split(",")
        while linea != "####":
            lista_palabras.append(linea_dicc)
            linea = leer_archivo(diccionario,"####")
            linea_dicc = linea.rstrip("\n").split(",")
    return lista_palabras
    #CRUZ, ARIEL CARLOS LEONARDO​

 

def crear_dicc_palabras_candidatas(longitud_minima_palabra):
    """
    La funcion escribe un archivo csv con las palabras y sus definiciones y devuelve un diccionario con las palabras y sus definiciones
    Parametros: numero entero
    return: diccionario con clave: palabra, valor: definicion
    """
    escribir_dicc_csv(longitud_minima_palabra)
    lista_palabras_def_candidatas = leer_diccionario()
    dicc_palabras_def_candidatas = transformador_lista_a_dicc(lista_palabras_def_candidatas)
    return dicc_palabras_def_candidatas
    #CRUZ, ARIEL CARLOS LEONARDO​

def generar_dicc_palabras_def_elegidas(diccionario_palabras_definiciones,cantidad_letras_rosco):
    """
    La elige las palabras que van a participar en el juego
    Parametros: diccionario {palabra:definicion, ...}
                numero entero. Cantidad de letras que va a tener el rosco
    return: diccionario con clave: palabra, valor: definicion
    """
    palabras_elegidas = seleccionar_palabras_aleatoria(list(diccionario_palabras_definiciones.keys()),cantidad_letras_rosco)
    lista_palabras_def_elegidas = extraer_claves_coincidentes(diccionario_palabras_definiciones,palabras_elegidas)
    INICIAL = 0
    diccionario_palabras_def_elegidas = {}
    for i in range(len(palabras_elegidas)):
        diccionario_palabras_def_elegidas[palabras_elegidas[i][INICIAL]] = lista_palabras_def_elegidas[i]
    return diccionario_palabras_def_elegidas
    #CRUZ, ARIEL CARLOS LEONARDO​

def generar_dicc_segun_configuracion():
    """
    La funcion genera un diccionario con las palabras y sus definiciones segun la configuracion del juego
    return: diccionario con clave: Inicial de la palabra, valor: lista con [palabra , definicion]
    """
    diccionario_conf = leer_configuracion()
    longitud_minima_palabra = int(diccionario_conf["LONGITUD_PALABRA_MINIMA"])
    cantidad_letras_rosco = int(diccionario_conf["CANTIDAD_LETRAS_ROSCO"])
    dicc_palabras_candidates = crear_dicc_palabras_candidatas(longitud_minima_palabra)
    dicc_palabras_elegidas = generar_dicc_palabras_def_elegidas(dicc_palabras_candidates,cantidad_letras_rosco)
    return dicc_palabras_elegidas
    #CRUZ, ARIEL CARLOS LEONARDO​

print(doctest.testmod())