from set_herramientas import orden_alfabetico

def leer_archivo(archivo, default):
    """
    La funcion recibe como parametro un archivo y una cadena y devuelve una linea del archivo
    """
    linea = archivo.readline()
    return linea if linea else default
def escribir_archivo(archivo, lista):
    """
    La funcion recibe como parametro un archivo y una lista y escribe en el archivo
    """
    for palabra,definicion in lista:
        archivo.write(f"{palabra},{definicion}\n")

def escribir_diccionario(longitud_minima_palabra):
    """
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
        #print(palabra,definicion,"\n")
        if len(palabra)<=longitud_minima_palabra and palabra.isalpha(): 
            palabras_candidatas.append([palabra,definicion])
        linea_palabra = leer_archivo(palabras,"####")
        linea_definicion = leer_archivo(definiciones,"####")
        palabra = linea_palabra.rstrip('\n')
        definicion = linea_definicion.rstrip('\n')
    palabras.close()
    definiciones.close()
    palabras_candidatas = sorted(palabras_candidatas, key=lambda x: orden_alfabetico(x[0]))
    escribir_archivo(diccionario,palabras_candidatas)
    diccionario.close()
escribir_diccionario(5)