#______________Funciones Complementarias_______________________

def write_csv(diccionario, archivo):
    """
    Parametros: 
    diccionario y archivo(objeto de open)
    """
    for clave, valor in diccionario.items():
        archivo.write(f"{clave},{valor}\n")

def leer_linea(archivo,default):
    """
    Parametros: archivo(objeto de open) y cadena
    return: linea del archivo o cadena default si se termino de leer el archivo
    """
    linea = archivo.readline()
    return linea if linea else default
def validar_int(cadena):
    """
    parametros:
        cadena: cadena de caracteres
        return: cadena convertida a entero o cadena "Valor invalido" si no se puede convertir

    """
    if cadena.isnumeric():
        cadena = int(cadena)
    else:
        cadena = "Valor invalido"
    return cadena

def definir_configuracion():
    """
    La funcion escribe en un archivo csv la configuracion del juego segun los parametros que ingrese el usuario
    """
    lista_configuracion = ["LONGITUD_PALABRA_MINIMA","CANTIDAD_LETRAS_ROSCO","MAXIMO_PARTIDAS","PUNTAJE_ACIERTO","PUNTAJE_DESACIERTO"]
    dicc_configuracion = {}
    for clave in lista_configuracion:
        dicc_configuracion[clave] = validar_int(input(f"Ingrese {clave}: "))
    with open("definiciones_palabras\\configuracion.csv","w") as configuracion:
        write_csv(dicc_configuracion, configuracion)
    return 
#________________________Etapa 10______________________________


def designar_configuracion(archivo= "definiciones_palabras\\configuracion.csv"):
    """
    Parametros: ruta del archivo de configuracion
    return: diccionario con la configuracion del juego
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