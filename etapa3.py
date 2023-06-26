import random
from set_herramientas import orden_alfabetico
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
    lista_palabras_elegidas = obtener_lista_palabras(lista_palabras,letras_participantes)
    resultado = [letras_participantes,lista_palabras_elegidas]
    return resultado