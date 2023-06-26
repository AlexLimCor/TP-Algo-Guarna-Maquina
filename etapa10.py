#______________Funciones Complementarias_______________________

def write_csv(diccionario, archivo):
    for clave, valor in diccionario.items():
        archivo.write(f"{clave},{valor}\n")

def leer_linea(archivo,default):
    linea = archivo.readline()
    return linea if linea else default
def validar_int(cadena):
    if cadena.isnumeric():
        cadena = int(cadena)
    else:
        cadena = "Valor invalido"
    return cadena

#________________________Etapa 10______________________________
def definir_configuracion():
    lista_configuracion = ["LONGITUD_PALABRA_MINIMA","CANTIDAD_LETRAS_ROSCO","MAXIMO_PARTIDAS","PUNTAJE_ACIERTO","PUNTAJE_DESACIERTO"]
    dicc_configuracion = {}
    for clave in lista_configuracion:
        dicc_configuracion[clave] = validar_int(input(f"Ingrese {clave}: "))
    with open("definiciones_palabras\\configuracion.csv","w") as configuracion:
        write_csv(dicc_configuracion, configuracion)
    return 

def designar_configuracion(archivo= "definiciones_palabras\\configuracion.csv"):
    """
    """
    dicc_default = {
    "LONGITUD_PALABRA_MINIMA": 4,
    "CANTIDAD_LETRAS_ROSCO": 10,
    "MAXIMO_PARTIDAS": 5,
    "PUNTAJE_ACIERTO": 10,
    "PUNTAJE_DESACIERTO": 3,
    }
    dicc_configuracion = {}
    default = "####"
    test = True
    lineas = 0
    with open(archivo, "r") as configuracion:
        linea = leer_linea(configuracion,default)
        linea_config = linea.rstrip("\n").split(",")
        while linea != default and test:
            if linea_config[0] in dicc_default.keys() and linea_config[1].isnumeric():
                dicc_configuracion[linea_config[0]] = linea_config[1]
            else:
                dicc_configuracion[linea_config[0]] = dicc_default[linea_config[0]]
            linea = leer_linea(configuracion,default)
            linea_config = linea.rstrip("\n").split(",")
            lineas +=1
        test = False if lineas != len(dicc_default) else True

    return dicc_configuracion

'''if __name__ == "__main__":
    definir_configuracion()
    print(designar_configuracion())'''