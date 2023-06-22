from datos import obtener_lista_definiciones
from set_herramientas import orden_alfabetico
# ----------ETAPA 2---------
'''En esta etapa procesamos el diccionario de palabras con sus definiciones y
 lo convertimos a diccionario con los requisitos pedidos'''

def generador_diccionario():
    datos = obtener_lista_definiciones()
    dicc_pal_def = {}
    LONG_MIN = 5
    PALABRA = 0
    DEFINICION = 1
    for element in datos:
        clave = element[PALABRA]
        valor = element[DEFINICION]
        if len(clave) >= LONG_MIN:
            dicc_pal_def[clave] = valor
    return dicc_pal_def

{"a":[["argentina","asd"]
      ["argelia","asd"]]}


def genera_diccionario_resumen(diccionario):
    """
    la funcion recibe como parametro un diccionario y devuelve un diccionario
    """
    diccionario_resumen = {}
    for indice in range(len(diccionario["letra_participantes"])):

        letra = diccionario["letra_participantes"][indice]
        respuesta = diccionario["respuestas"][indice]
        palabra = diccionario["Palabra_definicion"][indice][0]

        if diccionario["es_correcto"][indice]:
            diccionario_resumen[letra] = f"Turno de letra {letra.upper()} - Palabra de {len(palabra)} letras - {palabra} - acierto"

        else:
            diccionario_resumen[letra] = f"Turno de letra {letra.upper()} - Palabra de {len(palabra)} letras - {respuesta} - error - Palabra correcta {palabra}"
        
    return(diccionario_resumen)

def contador_puntaje(palabra_definicion,lista,puntaje_inicial = 0):
    lista_acietos_errores = []
    INDICE = 0
    palabra_correcta = 0 
    PUNTAJE = 0 + puntaje_inicial

    for palabra in lista:
        if palabra == palabra_definicion[INDICE][palabra_correcta]:
            lista_acietos_errores.append(True)
            PUNTAJE +=10  
        else:
            lista_acietos_errores.append(False)
            PUNTAJE += -3 
    
    diccionario_puntaje = {"puntaje":PUNTAJE,"lista_acietos_errores":lista_acietos_errores} 
    return diccionario_puntaje
    
# -----------------ETAPA 8-------------------
def main(longitud_minima_palabra = 5):
    palabras = open("definiciones_palabras\\palabras.txt","r",encoding='utf-8')
    definiciones = open("definiciones_palabras\\definiciones.txt","r",encoding='utf-8')
    diccionario = open("definiciones_palabras\\definiciones.csv","w",encoding='utf-8')
    palabras_candidatas = []
    linea_palabra = leer_archivo(palabras,"####")
    linea_definicion = leer_archivo(definiciones,"####")
    palabra = linea_palabra.rstrip('\n')
    definicion = linea_definicion.rstrip("\n")
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
    palabras_candidatas = sorted(palabras_candidatas, key=orden_alfabetico)
    escribir_archivo(diccionario,palabras_candidatas)
    diccionario.close()
main()

