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


