from datos import obtener_lista_definiciones
import random

# ETAPA_1
# INTERACCION CON EL JUGADOR
# CREAMOS UNA FUNCION DONDE INVOLUCRA LA ETAPA 1 Y 5 
def main():
    # BUSCAMOS GENERAR UNA LISTA DE LETRAS ELEGIDAS Y OTRA LISTA CON LA PALABRA Y SU DEFINICION SELECCIONADA 
    palabras_deficiones = [] # LISTA PALABRA Y DEFINICION
    lista_caracter = []   # LISTA DE LETRAS ELEGIDAS
    lista_aciertos = []
    ACIERTOS = 0
    lista_informe = []
    lista_agre_usuario = []
    ERRORES = 0
    CARACTER = 0
    ACERTADO = "[a]"
    ERRADO = "[e]"
    PALABRA = 0
    INDICE =0
    PALABRA_UNO = 0
    DEFINICION = 1
    while INDICE < len(lista_caracter):
        for caracter in lista_caracter:
            print("["+caracter.upper()+"]",end="")   
        print()
        for agregar in lista_aciertos:
            print(agregar,end="")
        print(f"\nAciertos:", ACIERTOS)
        print(f"Errores:",ERRORES)
    # TURNO DE LA LETRA A ADIVINAR 
        print(f"Turno letra",lista_caracter[CARACTER].upper(),"- Palabra de",len(palabras_deficiones[PALABRA][PALABRA_UNO]),"letras")
        print(f"Definicion:",palabras_deficiones[PALABRA][DEFINICION])
        ing_palabra = input(f"Ingrese palabra:")
        if ing_palabra ==  palabras_deficiones[PALABRA][PALABRA_UNO]:
            lista_informe.append(palabras_deficiones[PALABRA][PALABRA_UNO])
            ACIERTOS +=1
            PALABRA +=1
            CARACTER +=1
            lista_aciertos.append(ACERTADO) 
        else:
            lista_informe.append(palabras_deficiones[PALABRA][PALABRA_UNO])
            lista_agre_usuario.append(ing_palabra)
            ERRORES +=1
            PALABRA+=1
            lista_aciertos.append(ERRADO)
            CARACTER +=1
        print("----------------------------------------------------------")
        INDICE += 1
    # ETAPA 5 , PUNTAJE Y RESUMEN
    print("*****RESUMEN *****")
    diccionario_resumen = dict(zip(lista_informe,lista_aciertos))
    INDICE_2 = 0
    PUNTAJE = 0
    for clave,valor in diccionario_resumen.items():
        if valor == ACERTADO:
            print("Turno letra:",clave[PALABRA_UNO][CARACTER].upper(),"- Palabra de",len(clave),"letras-",clave,"acierto")
            PUNTAJE +=10
        if valor == ERRADO:
            print("Turno letra:",clave[PALABRA_UNO][CARACTER].upper(),"- Palabra de",len(clave),"letras-",lista_agre_usuario[INDICE_2],"- error - Palabra correcta:",clave)
            INDICE_2 +=1
            PUNTAJE -= 3
    print(f"Puntaje final: {PUNTAJE}")
    pregunta = int(input("Desea volver a jugar?: \n1.Si \n2.No \n"))
    SI = 1
    volverajugar = "Gracias por jugar"
    if pregunta == SI:
        volverajugar = main()
    print("----------------------------------------------------------")
    return volverajugar

# ETAPA 2
'''En esta etapa procesamos el diccionario de palabras con sus definiciones y
 lo convertimos a diccionario con los requisitos pedidos'''
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

    palabrasElegidas=[]
    #Convertimos el diccionario en lista para procesar las claves
    palabras = list(dicc_pal_def)
    #Mezclamos las palabras
    random.shuffle(palabras)
    # Indice que se incrementa con cada ciclo del while
    i = 0
    #Lista en la que se registra si se encontro la palabra segun las letras participantes
    encontradas = [False,False,False,False,False,False,False,False,False,False]
    while encontradas.count(False) > 0 and i < len(palabras):
        if len(palabras[i])>=5:
            #Se guardan las palabras segun las letras participantes, en la lista palabrasElegidas
            if not(encontradas[0]) and letrasElegidas[0]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[0] = True
            elif not(encontradas[1]) and letrasElegidas[1]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[1] = True            
            elif not(encontradas[2]) and letrasElegidas[2]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[2] = True
            elif not(encontradas[3]) and letrasElegidas[3]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[3] = True
            elif not(encontradas[4]) and letrasElegidas[4]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[4] = True
            elif not(encontradas[5]) and letrasElegidas[5]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[5] = True
            elif not(encontradas[6]) and letrasElegidas[6]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[6] = True
            elif not(encontradas[7]) and letrasElegidas[7]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[7] = True
            elif not(encontradas[8]) and letrasElegidas[8]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[8] = True
            elif not(encontradas[9]) and letrasElegidas[9]==palabras[i][0].replace("á","a").replace("é","e").\
                     replace("í","i").replace("ó","o").\
                     replace("ú","u"):
                palabrasElegidas.append(palabras[i])
                encontradas[9] = True
        i += 1
    #Ordenamos la lista de palabras teniendo en cuenta acentos y ñ
    palabrasElegidas.sort(key=lambda x: x.lower().
                     replace("á","a").replace("é","e").
                     replace("í","i").replace("ó","o").
                     replace("ú","u").replace("ñ","nzz"))
    return palabrasElegidas


#Invocamos 100 veces las funciones letrasParticipantes y etapa3.
'''for i in range (101):      
    letrasElegidas = letrasParticipantes()
    print (letrasElegidas)
    print (etapa3(etapa_2(),letrasElegidas))'''
def definicion(lista):
    # LO QUE SE BUSCA EN ESTA FUNCION ES OBTENER UNA LISTA(obtenida en la etapa3) 
    # ANIDADA CON LA FORMA : [[PALABRA,DEFINICION],[PALABRA2,DEFINICION2],ETC...]
    diccionario = etapa_2()
    lista_result = []
    ORDEN = 0
    for clave,valor in diccionario.items():
        if clave in lista:
            lista_result.append([clave,valor])
    lista_result.sort(key=lambda x:x[ORDEN].replace("ñ","nzz"))
    return lista_result
# --------------- ETAPA 4 --------------

def UnionEtapas(): 
    print("---------------------------------------------------")
    letrasElegidas = letrasParticipantes()
    palabras_deficiones = definicion(etapa3(etapa_2(),letrasElegidas))
    lista_aciertos = []
    ACIERTOS = 0
    lista_informe = []
    lista_agre_usuario = []
    ERRORES = 0
    CARACTER = 0
    ACERTADO = "[a]"
    ERRADO = "[e]"
    PALABRA = 0
    INDICE =0
    PALABRA_UNO = 0
    DEFINICION = 1
    while INDICE < len(letrasElegidas):
        for caracter in letrasElegidas:
            print("["+caracter.upper()+"]",end="")   
        print()
        for agregar in lista_aciertos:
            print(agregar,end="")
        print(f"\nAciertos:", ACIERTOS)
        print(f"Errores:",ERRORES)
    # TURNO DE LA LETRA A ADIVINAR 
        print(f"Turno letra",letrasElegidas[CARACTER].upper(),"- Palabra de",len(palabras_deficiones[PALABRA][PALABRA_UNO]),"letras")
        print(f"Definicion:",palabras_deficiones[PALABRA][DEFINICION])
        #print(palabras_deficiones[PALABRA])
        ing_palabra = input(f"Ingrese palabra:")
        if ing_palabra ==  palabras_deficiones[PALABRA][PALABRA_UNO]:
            lista_informe.append(palabras_deficiones[PALABRA][PALABRA_UNO])
            ACIERTOS +=1
            PALABRA +=1
            CARACTER +=1
            lista_aciertos.append(ACERTADO) 
        else:
            lista_informe.append(palabras_deficiones[PALABRA][PALABRA_UNO])
            lista_agre_usuario.append(ing_palabra)
            ERRORES +=1
            PALABRA+=1
            CARACTER +=1
            lista_aciertos.append(ERRADO)
        print("----------------------------------------------------------")
        INDICE += 1
    # ETAPA 5 , PUNTAJE Y RESUMEN
    print("*****RESUMEN *****")
    diccionario_resumen = dict(zip(lista_informe,lista_aciertos))
    INDICE_2 = 0
    PUNTAJE = 0
    for clave,valor in diccionario_resumen.items():
        if valor == ACERTADO:
            print("Turno letra:",clave[PALABRA_UNO].upper(),"- Palabra de",len(clave),"letras-",clave,"acierto")
            PUNTAJE +=10
        if valor == ERRADO:
            print("Turno letra:",clave[PALABRA_UNO].upper(),"- Palabra de",len(clave),"letras-",lista_agre_usuario[INDICE_2],"- error - Palabra correcta:",clave)
            INDICE_2 +=1
            PUNTAJE -= 3
    print(f"Puntaje final: {PUNTAJE}")
    pregunta = int(input("Desea volver a jugar?: \n1.Si \n2.No \n"))
    SI = 1
    volverajugar = "Gracias por jugar"
    if pregunta == SI:
        volverajugar = UnionEtapas()
    print("----------------------------------------------------------")
    return volverajugar
print(UnionEtapas())

















'''def tablero(letras_candidatas):
    # CREO UNA FUNCION QUE OBTENGA LOS 10 CARACTERES A JUGAR (ETAPA 3)
    lista_aciertos = []
    for element in letras_candidatas:
        print(f"["+element.upper()+"]",end="")
    print() 
    for acertado in lista_aciertos:
        print(acertado,end="")
    print()

def turno(palabra_y_deficion):
    # OBTENEMOS EL DICCIONARIO CON SU PALABRA Y DEFINICION
    ACIERTO = 0
    ERRORES = 0
    print(f"\nAciertos: {ACIERTO}")
    print(f"Errores: {ERRORES}") 
    PALABRA = 0
    PALABRA_UNO = 0
    CARACTER = 0
    DEFINICION = 1
    print(f"Turno de letra {palabra_y_deficion[PALABRA][PALABRA_UNO][CARACTER].upper()} - Palabra de {len(palabra_y_deficion[PALABRA][PALABRA_UNO])} letras")
    print(f"Definicion: {palabra_y_deficion[PALABRA][DEFINICION]}")

def ingre_palabra(palabras_candidatas):
    # ETAPA 5 , PUNTAJE
    PALABRA = 0
    PALABRA_UNO = 0
    ACERTADO = "[a]"
    ERRADO = "[e]"
    lista_aciertos = []
     
    lista_informe = []
    lista_agre_usuario = []
    palabra = input("Ingrese palabra:")
    if palabra in palabras_candidatas[PALABRA][PALABRA_UNO]:
        lista_informe.append(palabras_candidatas[PALABRA][PALABRA_UNO])
        ACIERTOS +=1
        PALABRA += 1
        lista_aciertos.append(ACERTADO)
    else:
        lista_informe.append(palabras_candidatas[PALABRA][PALABRA_UNO])
        lista_agre_usuario.append(palabra)
        ERRORES +=1
        PALABRA+=1
        lista_aciertos.append(ERRADO)
    print("----------------------------------------")
def puntaje():
    #RESUMEN
    lista_informe = []
    lista_aciertos = []
    lista_agre_usuario = []
    diccionario_resumen = dict(zip(lista_informe,lista_aciertos))
    PALABRA_UNO = 0
    INDICE_2 = 0
    PUNTAJE = 0
    CARACTER = 0
    ACERTADO = "[a]"
    ERRADO = "[e]"
    for clave,valor in diccionario_resumen.items():
        if valor == ACERTADO:
            print("Turno letra:",clave[PALABRA_UNO][CARACTER].upper(),"- Palabra de",len(clave),"letras-",clave,"acierto")
            PUNTAJE +=10
        if valor == ERRADO:
            print("Turno letra:",clave[PALABRA_UNO][CARACTER].upper(),"- Palabra de",len(clave),"letras-",lista_agre_usuario[INDICE_2],"- error - Palabra correcta:",clave)
            INDICE_2 +=1
            PUNTAJE -= 3
    print(f"Puntaje final: {PUNTAJE}")
    pregunta = int(input("Desea volver a jugar?: \n1.Si \n2.No \n"))
    SI = 1
    volverajugar = "Gracias por jugar"
    if pregunta == SI:
        volverajugar = unionEtapas()
    print("----------------------------------------------------------")
    return volverajugar
'''












'''def unionEtapas():
    lista = definicion(etapa3(etapa_2(),letrasElegidas))
    INDICE = 0
    while INDICE < len(letrasElegidas):
        tablero(letrasElegidas)
        turno(lista)
        ingre_palabra(lista)
    puntaje()

print(unionEtapas())'''


























'''definiciones = obtener_lista_definiciones()

palabras = list()
lista_a = list()
lista_b = list()
lista_c = list()
lista_d = list()
lista_e = list()
lista_f = list()
lista_g = list()
lista_h = list()
lista_i = list()
lista_j = list()
lista_k = list()
lista_l = list()
lista_m = list()
lista_n = list()
lista_o = list()
lista_p = list()
lista_q = list()
lista_r = list()
lista_s = list()
lista_t = list()
lista_u = list()
lista_v = list()
lista_w = list()
lista_x = list()
lista_y = list()
lista_z = list()

for i in range(len(definiciones)):
    if len(definiciones[i][0]) >= 5:
        palabras.append(definiciones[i])
        palabras.sort()
for i in range(len(palabras)):
    if palabras[i][0][0] == "a" or palabras[i][0][0] == "á":
        lista_a.append(palabras[i])
    elif palabras[i][0][0] == "b":
        lista_b.append(palabras[i])
    elif palabras[i][0][0] == "c":
        lista_c.append(palabras[i])
    elif palabras[i][0][0] == "d":
        lista_d.append(palabras[i])
    elif palabras[i][0][0] == "e" or palabras[i][0][0] == "é":
        lista_e.append(palabras[i])
    elif palabras[i][0][0] == "f":
        lista_f.append(palabras[i])
    elif palabras[i][0][0] == "g":
        lista_g.append(palabras[i])
    elif palabras[i][0][0] == "h":
        lista_h.append(palabras[i])
    elif palabras[i][0][0] == "i" or palabras[i][0][0] == "í":
        lista_i.append(palabras[i])
    elif palabras[i][0][0] == "j":
        lista_j.append(palabras[i])
    elif palabras[i][0][0] == "k":
        lista_k.append(palabras[i])
    elif palabras[i][0][0] == "l":
        lista_l.append(palabras[i])
    elif palabras[i][0][0] == "m":
        lista_m.append(palabras[i])
    elif palabras[i][0][0] == "n":
        lista_n.append(palabras[i])
    elif palabras[i][0][0] == "o" or palabras[i][0][0] == "ó":
        lista_o.append(palabras[i])
    elif palabras[i][0][0] == "p":
        lista_p.append(palabras[i])
    elif palabras[i][0][0] == "q":
        lista_q.append(palabras[i])
    elif palabras[i][0][0] == "r":
        lista_r.append(palabras[i])
    elif palabras[i][0][0] == "s":
        lista_s.append(palabras[i])
    elif palabras[i][0][0] == "t":
        lista_t.append(palabras[i])
    elif palabras[i][0][0] == "u" or palabras[i][0][0] == "ú":
        lista_u.append(palabras[i])
    elif palabras[i][0][0] == "v":
        lista_v.append(palabras[i])
    elif palabras[i][0][0] == "w":
        lista_w.append(palabras[i])
    elif palabras[i][0][0] == "x":
        lista_x.append(palabras[i])
    elif palabras[i][0][0] == "y":
        lista_y.append(palabras[i])
    elif palabras[i][0][0] == "z":
        lista_z.append(palabras[i])
        
listas_de_palabras = [lista_a] + [lista_b] + [lista_c] + [lista_d] + [lista_e] + [lista_f] + [lista_g] + [lista_h] + [lista_i] + [lista_j] + [lista_k] + [lista_l] + [lista_m] + [lista_n] + [lista_o] + [lista_p] + [lista_q] + [lista_r] + [lista_s] + [lista_t] + [lista_u] + [lista_v] + [lista_w] + [lista_x] + [lista_y] +[lista_z]

abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
dicc_de_palabras = dict()
for j in range(len(listas_de_palabras)):
    dicc_de_palabras[abecedario[j]] = listas_de_palabras[j]

contador = 0
for clave, valor in dicc_de_palabras.items():
    print("La letra",clave,"tiene",len(valor),"palabras")
    contador += len(valor)
print("La cantidad de palabras en total que hay en el diccionario son:",contador)'''







        





            










