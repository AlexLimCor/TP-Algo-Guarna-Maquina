from etapa3 import definicion, etapa_2, etapa3 , letrasElegidas
# UNIMOS TODAS LAS ETAPAS CREADAS 

def invocar():
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
    while INDICE < len(palabras_deficiones):
        for caracter in palabras_deficiones:
            print("["+caracter[PALABRA_UNO][CARACTER].upper()+"]",end="")   
        print()
        for agregar in lista_aciertos:
            print(agregar,end="")
        print(f"\nAciertos:", ACIERTOS)
        print(f"Errores:",ERRORES)
        print(f"Turno letra",palabras_deficiones[PALABRA][PALABRA_UNO][CARACTER].upper(),"- Palabra de",len(palabras_deficiones[PALABRA][PALABRA_UNO]),"letras")
        print(f"Definicion:",palabras_deficiones[PALABRA][DEFINICION])
        ing_palabra = input(f"Ingrese palabra:")
        if ing_palabra ==  palabras_deficiones[PALABRA][PALABRA_UNO]:
            lista_informe.append(palabras_deficiones[PALABRA][PALABRA_UNO])
            ACIERTOS +=1
            PALABRA +=1
            lista_aciertos.append(ACERTADO) 
        else:
            lista_informe.append(palabras_deficiones[PALABRA][PALABRA_UNO])
            lista_agre_usuario.append(ing_palabra)
            ERRORES +=1
            PALABRA+=1
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
            print("Turno letra:",clave[PALABRA_UNO][CARACTER].upper(),"- Palabra de",len(clave),"letras-",clave,"acierto")
            PUNTAJE +=10
        if valor == ERRADO:
            print("Turno letra:",clave[PALABRA_UNO][CARACTER].upper(),"- Palabra de",len(clave),"letras-",lista_agre_usuario[INDICE_2],"- error - Palabra correcta:",clave)
            INDICE_2 +=1
            PUNTAJE -= 3
    print(f"Puntaje final: {PUNTAJE}")
invocar()


   