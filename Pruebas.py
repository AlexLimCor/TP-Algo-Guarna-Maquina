#-----------ETAPA 1 ---------------#
import doctest
# Validamos que sea una palabra correcta 
def Verificar(palabra):
    '''
    >>> Verificar('Manzana')
    True
    >>> Verificar('Per@#@')
    False
    >>> Verificar("1234")
    False
    >>> Verificar("AnAná")
    True
    '''
    vocales_acentuadas = ["á","é","í","ó","ú"]
    validar = True
    indice = 0
    while indice < len(palabra) and validar:
        caracter = palabra[indice]
        if caracter.isnumeric():
            validar = False
        if not caracter.isalnum():
            validar = False
            if caracter in vocales_acentuadas:
                validar = True
        indice +=1
    # Aplanamos la palabra para que no distinga la mayuscula
    return validar
print(doctest.testmod())
# --------- Etapa 2-----------#



from valor_aleatorio import generar_letras_aleatorias,seleccionar_clave_aleatoria_por_letra
from etapa8 import generador_diccionario
from set_herramientas import jugar_de_nuevo,contador_puntaje
def test_generar_letras_aleatorias():
    lista_test = []
    for i in range(10):
        test = True if len(generar_letras_aleatorias(i)) == i else False
        lista_test.append(test)
    return lista_test

print(test_generar_letras_aleatorias())

def test_seleccionar_clave_aleatoria_por_letra():
    lista_test = []
    diccionario = generador_diccionario()
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for letra in letras:
        palabra = seleccionar_clave_aleatoria_por_letra(diccionario, letra)
        test = True if palabra[0] == letra else False
        lista_test.append(test)
    return lista_test

print(test_seleccionar_clave_aleatoria_por_letra())

def test_jugar_de_nuevo():
    lista_test = []
    

    