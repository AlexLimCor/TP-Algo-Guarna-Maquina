from datos import obtener_lista_definiciones

# ETAPA_1
# INTERACCION CON EL JUGADOR

def tablero(letras_candidatas):
    # CREO UNA FUNCION QUE OBTENGA LOS 10 CARACTERES A JUGAR (ETAPA 3)
    ACIERTOS = 0
    ERRORES = 0
    lista_aciertos = []
    for element in letras_candidatas:
        print(f"["+element+"]",end="")
    print() 
    for acertado in lista_aciertos:
        print(acertado,end="")
    print()
    print(f"Acierto: {ACIERTOS}")
    print(f"Errores: {ERRORES}")

def turno(palabra_y_deficion):
    # OBTENEMOS EL DICCIONARIO CON SU PALABRA Y DEFINICION 
    LETRA_CAND = 0
    DEFINICION = 1
    print(f"Turno de letra {palabra_y_deficion[LETRA_CAND]} - Palabra de {len(palabra_y_deficion[LETRA_CAND])} letras")
    print(f"Definicion: {palabra_y_deficion[DEFINICION]}")

def ingre_palabra(palabras_candidatas):
    # ETAPA 5 , PUNTAJE 
    palabra = input("Ingrese palabra:")

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
print(etapa_2())







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







        





            










