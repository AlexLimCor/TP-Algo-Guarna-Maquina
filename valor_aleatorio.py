from set_herramientas import orden_alfabetico
import random
def generar_letras_aleatorias(cantidad_letras):
    """
    """
    letras=['a','b','c','d','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    #Elegimos 10 letras aleatorias
    letras_elegidas=random.sample(letras,cantidad_letras)
    #Ordenamos las letras alfabeticamente
    letras_elegidas = sorted(letras_elegidas, key=orden_alfabetico)
    return letras_elegidas

def seleccionar_clave_aleatoria_por_letra(diccionario,letra):
    inicial = 0
    letra = orden_alfabetico(letra)
    listas_claves_candidatas = [clave for clave in diccionario.keys() if orden_alfabetico(clave)[inicial] in letra]
    palabra_aleatoria_elegida = random.choice(listas_claves_candidatas)
    return palabra_aleatoria_elegida

