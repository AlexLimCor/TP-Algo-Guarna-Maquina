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
def escribir_csv(diccionario, archivo):
    """
    Parametros: 
    diccionario y archivo(objeto de open)
    """
    for clave, valor in diccionario.items():
        archivo.write(f"{clave},{valor}\n")
    #CRUZ, ARIEL CARLOS LEONARDO​
def generar_diccionario(lista_clave,lista_valor):
    """
    Parametros: lista de claves y lista de valores
    return: diccionario con clave: lista_clave, valor: lista_valor
    """
    diccionario = {}
    for indice in range(len(lista_clave)):
        diccionario[lista_clave[indice]] = lista_valor[indice]
    return diccionario
    #CRUZ, ARIEL CARLOS LEONARDO​  
#________________________Etapa 10______________________________

def varidar_config(valores):
    """
    La funcion valida que los valores ingresados por el usuario sean validos
    Parametros: diccionario con la configuracion del usuario{config:valor}
    return: lista con los mensajes de error
    """
    etiquetas = ["LONGITUD_PALABRA_MINIMA","CANTIDAD_LETRAS_ROSCO","MAXIMO_PARTIDAS","PUNTAJE_ACIERTO","PUNTAJE_DESACIERTO"]
    dicc_config_usuario = generar_diccionario(etiquetas,valores)
    dicc_config_default = {
    "LONGITUD_PALABRA_MINIMA": 4,
    "CANTIDAD_LETRAS_ROSCO": 10,
    "MAXIMO_PARTIDAS": 5,
    "PUNTAJE_ACIERTO": 10,
    "PUNTAJE_DESACIERTO": 3,
    }
    dicc_confic_valido = {}
    error_mensajes = []
    for clave, valor in dicc_config_default.items():
        valor = dicc_config_usuario[clave]
        try:
            if valor < dicc_config_default[clave] or type(valor) != int:
                raise ValueError
        except ValueError:
            error_mensajes.append(clave)
    
    if error_mensajes:
        mensaje_error = ""
        for error in error_mensajes:
            mensaje_error += f"El valor de {error}, no es valido.\n Recuerda que el valor un numero entero mayor o igual a {dicc_config_default[error]}\n"
        messagebox.showerror("Error en la configuracion", mensaje_error)
    return dicc_config_usuario if not error_mensajes else dicc_config_default
    #CRUZ, ARIEL CARLOS LEONARDO​

def escribir_dicc_configuracion(longitud_palabra_minima,letras_en_el_rosco,maximo_partidas,puntaje_acierto,puntaje_desacierto):
    valores = [longitud_palabra_minima,letras_en_el_rosco,maximo_partidas,puntaje_acierto,puntaje_desacierto]
    """
    La funcion recibe como parametro un diccionario y un archivo y escribe en el archivo
    """
    diccionario_valido = varidar_config(valores)
    with open(configuracion_arc,"w") as configuracion:
        escribir_csv(diccionario_valido, configuracion)
    return 

def leer_configuracion():
    dicc_default = {
    "LONGITUD_PALABRA_MINIMA": 4,
    "CANTIDAD_LETRAS_ROSCO": 10,
    "MAXIMO_PARTIDAS": 5,
    "PUNTAJE_ACIERTO": 10,
    "PUNTAJE_DESACIERTO": 3,
    }
    CONFIGURACION = 0
    VALOR = 1
    diccionario_configuracion = {}
    with open(configuracion_arc,"r") as configuracion:
        linea = leer_linea(configuracion,"####")
        linea_dicc = linea.rstrip("\n").split(",")
        while linea != "####":
            if len(linea_dicc) == 2:
                diccionario_configuracion[linea_dicc[CONFIGURACION]] = int(linea_dicc[VALOR])
            linea = leer_linea(configuracion,"####")
            linea_dicc = linea.rstrip("\n").split(",")
    print(diccionario_configuracion)
    
    for clave, valor in dicc_default.items():
        try:
            print(clave,valor)
            if not clave in diccionario_configuracion.keys():
                raise KeyError
            elif type(diccionario_configuracion[clave]) != int:
                raise ValueError
        except KeyError:
            diccionario_configuracion[clave] = valor
        except ValueError:
            diccionario_configuracion[clave] = valor
    return diccionario_configuracion


print(leer_configuracion())