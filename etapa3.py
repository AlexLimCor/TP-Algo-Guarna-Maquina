import random
#Para probar las funciones de etapa3 se agrega la funcion etapa2()
#y la importacion de obtener_lista_definiciones
from datos import obtener_lista_definiciones

def etapa_2():
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

# ------ ETAPA 3 ------

# Creamos lista de letras participantes.
def letrasParticipantes():
    letras=['a','b','c','d','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    #Elegimos 10 letras aleatorias
    letrasElegidas=random.sample(letras,10)
    #Ordenamos las letras alfabeticamente
    letrasElegidas.sort(key=lambda letra: letra.replace("ñ","nzz"))
    return letrasElegidas
# Creamos lista de palabras participantes.    
def etapa3(dicc_pal_def,letrasElegidas):
    lista1=[] #Lista de palabras correspondiente a la 1° letra participante
    lista2=[] #Lista de palabras correspondiente a la 2° letra participante
    lista3=[] #Lista de palabras correspondiente a la 3° letra participante
    lista4=[] #Lista de palabras correspondiente a la 4° letra participante
    lista5=[] #Lista de palabras correspondiente a la 5° letra participante
    lista6=[] #Lista de palabras correspondiente a la 6° letra participante
    lista7=[] #Lista de palabras correspondiente a la 7° letra participante
    lista8=[] #Lista de palabras correspondiente a la 8° letra participante
    lista9=[] #Lista de palabras correspondiente a la 9° letra participante
    lista10=[] #Lista de palabras correspondiente a la 10° letra participante
    palabrasElegidas=[]
    #Creamos a partir del diccionario una lista de palabras ordenadas y contemplando los acentos y la ñ
    palabras= sorted(dicc_pal_def,key=lambda x: x.lower().
                     replace("á","a").replace("é","e").
                     replace("í","i").replace("ó","o").
                     replace("ú","u").replace("ñ","nzz"))
    #Obtenemos una palabra de la lista palabras para procesarlas
    for palabra in palabras:
        #verificamos que cumplan las condiciones de longitud y que su 1° letra sea de las participantes
        if palabra[0] in letrasElegidas and len(palabra)>=5:
            #creamos listas de palabras segun las letras participantes
            if letrasElegidas[0]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
               lista1.append(palabra)
            elif letrasElegidas[1]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista2.append(palabra)            
            elif letrasElegidas[2]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista3.append(palabra)
            elif letrasElegidas[3]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista4.append(palabra)
            elif letrasElegidas[4]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista5.append(palabra)
            elif letrasElegidas[5]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista6.append(palabra)
            elif letrasElegidas[6]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista7.append(palabra)
            elif letrasElegidas[7]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista8.append(palabra)
            elif letrasElegidas[8]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista9.append(palabra)
            elif letrasElegidas[9]==palabra[0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                lista10.append(palabra)
    #seleccionamos una palabra aleatoria de cada lista segun letra
    #y guardamos en la lista palabrasElegidas, la cual será retornada
    palabrasElegidas.extend(random.sample(lista1,1))
    palabrasElegidas.extend(random.sample(lista2,1))
    palabrasElegidas.extend(random.sample(lista3,1))
    palabrasElegidas.extend(random.sample(lista4,1))
    palabrasElegidas.extend(random.sample(lista5,1))
    palabrasElegidas.extend(random.sample(lista6,1))
    palabrasElegidas.extend(random.sample(lista7,1))
    palabrasElegidas.extend(random.sample(lista8,1))
    palabrasElegidas.extend(random.sample(lista9,1))
    palabrasElegidas.extend(random.sample(lista10,1))
    
    return palabrasElegidas

#Invocamos 100 veces las funciones letrasParticipantes y etapa3.
'''for i in range (101):      
    letrasElegidas = letrasParticipantes()
    print (letrasElegidas)
    print (etapa3(etapa_2(),letrasElegidas))'''
#------ ACA TERMINA ETAPA 3 ------

letrasElegidas = letrasParticipantes()
def definicion(lista):
    diccionario = etapa_2()
    lista_result = []
    ORDEN = 0
    for clave,valor in diccionario.items():
        if clave in lista:
            lista_result.append([clave,valor])
    lista_result.sort(key=lambda x:x[ORDEN])
    return lista_result




