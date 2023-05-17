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




   