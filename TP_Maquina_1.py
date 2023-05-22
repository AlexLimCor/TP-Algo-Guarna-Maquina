from etapa3 import definicion, etapa_2, etapa3 , letrasElegidas
import random
# UNIMOS TODAS LAS ETAPAS CREADAS ETAPA 4
# ETAPA 1
def main():
    # MOSTRAMOS EL TABLERO DE LAS LETRAS PARTICIPANTES
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

letrasElegidas = letrasParticipantes()
print(letrasElegidas)
print(etapa3(etapa_2(),letrasElegidas))
#------ ACA TERMINA ETAPA 3 ------

        


   