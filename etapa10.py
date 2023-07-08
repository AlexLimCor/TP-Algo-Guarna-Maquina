import os
from tkinter import messagebox 
#______________Rutas de archivos_______________________
configuracion_arc = os.path.join("definiciones_palabras","configuracion.csv")
#______________Funciones Complementarias_______________________
def leer_linea(archivo,default):
    """
    Parametros: archivo(objeto de open) y cadena
    return: linea del archivo o cadena default si se termino de leer el archivo
    """
    linea = archivo.readline()
    return linea if linea else default
    #CRUZ, ARIEL CARLOS LEONARDO​
    
#________________________Etapa 10______________________________

def designar_configuracion():
    """
    Parametros: ruta del archivo de configuracion
    return: diccionario con la configuracion del juego
    """
    archivo = configuracion_arc
    dicc_config_default = {
    "LONGITUD_PALABRA_MINIMA": 4,
    "CANTIDAD_LETRAS_ROSCO": 10,
    "MAXIMO_PARTIDAS": 5,
    "PUNTAJE_ACIERTO": 10,
    "PUNTAJE_DESACIERTO": 3,
    }
    dicc_configuracion = {}
    default = "####,####"
    with open(archivo, "r") as configuracion:
        linea = leer_linea(configuracion,default)
        config, valor = linea.rstrip("\n").split(",")
        while config != "####":
            if config in dicc_config_default and valor.isnumeric():
                dicc_configuracion[config] = int(valor)
            linea = leer_linea(configuracion,default)
            config, valor = linea.rstrip("\n").split(",")
    #Completamos el diccionario con los valores por defecto si no estan en el archivo
    for clave, valor in dicc_config_default.items():
        if clave not in dicc_configuracion:
            #print(f"La configuracion {clave} no es valida, asignando valor por defecto {valor}")
            dicc_configuracion[clave] = valor
    return dicc_configuracion
    #CRUZ, ARIEL CARLOS LEONARDO​

    
def varidar_config(diccionario_config_usuario):
    """
    La funcion valida que los valores ingresados por el usuario sean validos
    Parametros: diccionario con la configuracion del usuario{config:valor}
    return: lista con los mensajes de error
    """
    dicc_config_default = {
    "LONGITUD_PALABRA_MINIMA": 4,
    "CANTIDAD_LETRAS_ROSCO": 10,
    "MAXIMO_PARTIDAS": 5,
    "PUNTAJE_ACIERTO": 10,
    "PUNTAJE_DESACIERTO": 3,
    }
    etiquetas = list(diccionario_config_usuario.keys())
    valores = list(diccionario_config_usuario.values())
    error_mensajes = []
    for indice in range(len(valores)):
        valor = valores[indice]
        try:
            valor = int(valor)
            if valor < dicc_config_default[etiquetas[indice]]:
                raise ValueError
        except ValueError:
            error_mensajes.append(f"El valor {etiquetas[indice]} debe ser un numero entero mayor {dicc_config_default[etiquetas[indice]]}")
    
    if error_mensajes:
        mensaje_error = ""
        for error in error_mensajes:
            mensaje_error += error + "\n"
        messagebox.showerror("Error", mensaje_error)
    return error_mensajes
    #CRUZ, ARIEL CARLOS LEONARDO​