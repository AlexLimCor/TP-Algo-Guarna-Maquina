from set_herramientas import orden_alfabetico, correccion_alfabetica
import cProfile
import pstats
excepciones = ["á","é","í","ó","ú","ñ"]
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
        archivo.write(f"{palabra},'{definicion}'\n")

def escribir_diccionario(longitud_minima_palabra):
    """
    """
    palabras = open("definiciones_palabras\\palabras.txt","r"),#encoding='utf-8')
    definiciones = open("definiciones_palabras\\definiciones.txt","r")#,encoding='utf-8')
    diccionario = open("definiciones_palabras\\definiciones.csv_v2","w")#,encoding='utf-8')
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
        if len(palabra)<=longitud_minima_palabra and palabra.isalpha(): 
            palabras_candidatas.append([palabra,definicion])
        linea_palabra = leer_archivo(palabras,"####")
        linea_definicion = leer_archivo(definiciones,"####")
        palabra = linea_palabra.rstrip('\n')
        definicion = linea_definicion.rstrip('\n')
    palabras.close()
    definiciones.close()
    #print(palabras_candidatas)
    palabras_candidatas = sorted(palabras_candidatas, key=lambda x:orden_alfabetico(x[0]))
    print(diccionario)
    diccionario.write("palabra,definicion\n")
    escribir_archivo(diccionario,palabras_candidatas)
    diccionario.close()
escribir_diccionario(100)


#sorted_palabras = sorted(palabras_candidatas, key=lambda x: correccion_alfabetica(x[0]) if x[0][0] not in excepciones else x[0])


palabras_candidatas = [['árbol', 'definición1'], ['zorro', 'definición2'], ['ópera', 'definición3'], ['éxito', 'definición4'], ['ñandú', 'definición5']]
excepciones = {'á', 'é', 'í', 'ó', 'ú', 'ñ'}

sorted_palabras = sorted(palabras_candidatas, key=lambda x: correccion_alfabetica(x[0]) if x[0][0] not in excepciones else correccion_alfabetica(x[0]))
print(sorted_palabras)
