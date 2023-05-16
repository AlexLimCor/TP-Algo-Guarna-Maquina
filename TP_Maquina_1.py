from datos import obtener_lista_definiciones
import random

def invocar():
    deficion_lista = obtener_lista_definiciones()
    lista_aciertos = []
    ACIERTOS = 0
    lista_informe = []
    lista_agre_usuario = []
    ERRORES = 0
    CARACTER = 0
    ACERTADO = "[a]"
    ERRADO = "[e]"
    CARACTER_A_JUGAR = 0
    INDICE =0
    DEFINICION_JUGAR = 1
    DEFINICION = 0
    lista_jugar = random.sample(deficion_lista,10)
    while INDICE < len(lista_jugar):
        for caracter in lista_jugar:
            print("["+caracter[CARACTER_A_JUGAR][CARACTER_A_JUGAR].upper()+"]",end="")   
        print()
        for agregar in lista_aciertos:
            print(agregar,end="")
        print(f"\nAciertos:", ACIERTOS)
        print(f"Errores:",ERRORES)
        print(f"Turno letra",lista_jugar[CARACTER][CARACTER_A_JUGAR][CARACTER_A_JUGAR].upper(),"- Palabra de",len(lista_jugar[CARACTER][CARACTER_A_JUGAR]),"letras")
        print(f"Definicion:",lista_jugar[DEFINICION][DEFINICION_JUGAR])
        ing_palabra = input(f"Ingrese palabra:")
        ing_palabra = ing_palabra.lower()
        if ing_palabra ==  lista_jugar[CARACTER][CARACTER_A_JUGAR]:
            lista_informe.append(lista_jugar[CARACTER][CARACTER_A_JUGAR])
            ACIERTOS +=1
            CARACTER +=1
            DEFINICION += 1
            lista_aciertos.append(ACERTADO) 
        else:
            lista_informe.append(lista_jugar[CARACTER][CARACTER_A_JUGAR])
            lista_agre_usuario.append(ing_palabra)
            ERRORES +=1
            CARACTER +=1
            DEFINICION +=1
            lista_aciertos.append(ERRADO)
        print("----------------------------------------------------------")
        INDICE += 1
    print("*****RESUMEN *****")
    diccionario_resumen = dict(zip(lista_informe,lista_aciertos))
    INDICE_2 = 0
    PUNTAJE = 0
    for clave,valor in diccionario_resumen.items():
        if valor == ACERTADO:
            print("Turno letra:",clave[CARACTER_A_JUGAR][CARACTER_A_JUGAR].upper(),"- Palabra de",len(clave),"letras-",clave,"acierto")
            PUNTAJE +=10
        if valor == ERRADO:
            print("Turno letra:",clave[CARACTER_A_JUGAR][CARACTER_A_JUGAR].upper(),"- Palabra de",len(clave),"letras-",lista_agre_usuario[INDICE_2],"- error - Palabra correcta:",clave)
            INDICE_2 +=1
            PUNTAJE -= 3
    print(f"Puntaje final: {PUNTAJE}")
invocar()

definiciones = obtener_lista_definiciones()

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
print("La cantidad de palabras en total que hay en el diccionario son:",contador)

   