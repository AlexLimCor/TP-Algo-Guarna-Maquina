def write_csv(diccionario, archivo):
    for clave, valor in diccionario.items():
        archivo.write(f"{clave},{valor}\n")
def definir_configuracion():
    dicc_configuracion = {
        "LONGITUD_PALABRA_MINIMA": 4,
        "CANTIDAD_LETRAS_ROSCO": 10,
        "MAXIMO_PARTIDAS": 5,
        "PUNTAJE_ACIERTO": 10,
        "PUNTAJE_DESACIERTO": 3,
    }    
    with open("definiciones_palabras\\configuracion.csv","w") as configuracion:
        write_csv(dicc_configuracion, configuracion)
    
    return 

definir_configuracion()