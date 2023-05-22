from datos import obtener_lista_definiciones
import random

# ETAPA_1
# INTERACCION CON EL JUGADOR
def main():
    # MOSTRAMOS EL TABLERO DE LAS LETRAS PARTICIPANTES
    palabras_deficiones = []
    lista_caracter = []
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
'''En esta etapa procesamos el diccionario de palabras con sus definiciones y lo convertimos a diccionario con los requisitos pedidos'''
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
def definicion(lista):
    diccionario = etapa_2()
    lista_result = []
    ORDEN = 0
    for clave,valor in diccionario.items():
        if clave in lista:
            lista_result.append([clave,valor])
    lista_result.sort(key=lambda x:x[ORDEN])
    return lista_result
#------ ACA TERMINA ETAPA 3 ------

# ---------- ETAPA 4 ----------
# UNIMOS TODAS LAS ETAPAS 
letrasElegidas = letrasParticipantes()

def main():
    # MOSTRAMOS EL TABLERO DE LAS LETRAS PARTICIPANTES
    print("----------------------------------------------------------")
    palabras_deficiones = definicion(etapa3(etapa_2(),letrasElegidas))
    lista_caracter = letrasElegidas
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
        '''print(palabras_deficiones[PALABRA])'''
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
    CARACTER_2 =0
    for clave,valor in diccionario_resumen.items():
        if valor == ACERTADO:
            print("Turno letra:",lista_caracter[CARACTER_2].upper(),"- Palabra de",len(clave),"letras-",clave,"acierto")
            PUNTAJE +=10
            CARACTER_2 +=1
        if valor == ERRADO:
            print("Turno letra:",lista_caracter[CARACTER_2].upper(),"- Palabra de",len(clave),"letras-",lista_agre_usuario[INDICE_2],"- error - Palabra correcta:",clave)
            INDICE_2 +=1
            PUNTAJE -= 3
            CARACTER_2 +=1
    print(f"Puntaje final: {PUNTAJE}")
    pregunta = int(input("Desea volver a jugar?: \n1.Si \n2.No \n"))
    SI = 1
    volverajugar = "Gracias por jugar"
    if pregunta == SI:
        volverajugar = main()
        
    print("----------------------------------------------------------")
    return volverajugar

print(main())








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







        





            










