from set_herramientas import orden_alfabetico
from etapa10 import designar_configuracion
from etapa3 import integrar_etapa_3
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
escribir_diccionario(4)


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

def integrar_etapa_8():
    LONGITUD_PALABRA_MINIMA = designar_configuracion()["LONGITUD_PALABRA_MINIMA"]
    CANTIDAD_LETRAS_ROSCO = designar_configuracion()["CANTIDAD_LETRAS_ROSCO"]
    escribir_archivo(LONGITUD_PALABRA_MINIMA)
    lista_palabras = leer_diccionario()
    dicc = generador_diccionario(lista_palabras)
    letras,palabras = integrar_etapa_3(dicc.keys(),CANTIDAD_LETRAS_ROSCO)
    return letras,palabras    
