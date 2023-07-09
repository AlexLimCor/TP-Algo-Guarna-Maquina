import os
from tkinter import messagebox 
import doctest
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
def generar_diccionario(lista_clave,lista_valor,transf_int=False):
    """
    La funcion recibe como parametro dos listas y devuelve un diccionario con las claves y valores de las listas
    Si el parametro transf_int es True, los valores de la lista_valor se convierten a enteros
    Parametros: lista de claves, lista de valores y booleano
    return: diccionario con clave: lista_clave, valor: lista_valor
    >>> generar_diccionario(["a","b","c"],[1,2,3])
    {'a': 1, 'b': 2, 'c': 3}
    >>> generar_diccionario(["a","b","c"],["1","2","3"],True)
    {'a': 1, 'b': 2, 'c': 3}
    >>> generar_diccionario(["a","b","c"],["1","2","3"])
    {'a': '1', 'b': '2', 'c': '3'}
    """
    diccionario = {}
    for indice in range(len(lista_clave)):
        if transf_int:
            diccionario[lista_clave[indice]] = int(lista_valor[indice])
        else:
            diccionario[lista_clave[indice]] = lista_valor[indice]
    return diccionario
    #CRUZ, ARIEL CARLOS LEONARDO​  

#_________________________Validar Configuracion del usuario____________________________________

def validar_config(valores):
    """
    La funcion valida que los valores ingresados por el usuario sean validos
    Parametros: diccionario con la configuracion del usuario{config:valor}
    return: lista con los mensajes de error
    >>> validar_config(['4','10','5','10','3'])
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    >>> validar_config(['4','10','5','10','3.5'])
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    >>> validar_config(['4','10','5','10','m'])
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    >>> validar_config(['d','10','5','10','3'])
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    >>> validar_config(['5','5','10','5','10'])
    {'LONGITUD_PALABRA_MINIMA': 5, 'CANTIDAD_LETRAS_ROSCO': 5, 'MAXIMO_PARTIDAS': 10, 'PUNTAJE_ACIERTO': 5, 'PUNTAJE_DESACIERTO': 10}

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
    MAX_LONGITUD_PALABRA = 15
    error_mensajes = []
    for clave, valor_def in dicc_config_usuario.items():
        if valor_def.isnumeric():
            if len(valor_def.split(".")) != 1:
                error_mensajes.append(clave)
            elif clave == "LONGITUD_PALABRA_MINIMA" and (int(valor_def) < dicc_config_default[clave] or int(valor_def) > MAX_LONGITUD_PALABRA):
                error_mensajes.append(clave)
            elif int(valor_def) < 0:
                error_mensajes.append(clave)
        else:
            error_mensajes.append(clave)
    
    if error_mensajes:
        mensaje_error = ""
        for error in error_mensajes:
            if error == "LONGITUD_PALABRA_MINIMA":
                mensaje_error += f"La longitud minima de la palabra debe ser mayor a {dicc_config_default[error] -1} y menor a {MAX_LONGITUD_PALABRA + 1}\n"
            else:
                mensaje_error += f"{error} debe ser un numero entero mayor a 0\n"
        if not __name__ == "__main__":
            messagebox.showerror("Error", mensaje_error)
    else:
        messagebox.showinfo("Configuracion", "Configuracion guardada correctamente") if not __name__ == "__main__" else None
            
    return generar_diccionario(etiquetas,valores,True) if not error_mensajes else dicc_config_default
    #CRUZ, ARIEL CARLOS LEONARDO​

#_________________________Escribir Archivo Configuracion____________________________________

def escribir_dicc_configuracion(longitud_palabra_minima,letras_en_el_rosco,maximo_partidas,puntaje_acierto,puntaje_desacierto):
    """
    La funcion recibe como parametro un diccionario y un archivo y escribe en configuracion.csv.
    """
    valores = [longitud_palabra_minima,letras_en_el_rosco,maximo_partidas,puntaje_acierto,puntaje_desacierto]
    diccionario_valido = validar_config(valores)

    with open(configuracion_arc,"w") as configuracion:
        escribir_csv(diccionario_valido, configuracion)

    return 
    #CRUZ, ARIEL CARLOS LEONARDO​
#_________________________Leer Archivo Configuracion____________________________________

def obtener_confi_valida(dicc_configuracion):
    """
    La funcion recibe como parametro un diccionario y en caso de que no tenga las claves 
    necesarias o los valores no sean enteros, se le asigna un valor por defecto
    Parametros: diccionario
    return: diccionario con las claves y valores validos
    >>> obtener_confi_valida({"LONGITUD_PALABRA_MINIMA": 4, "CANTIDAD_LETRAS_ROSCO": 10, "MAXIMO_PARTIDAS": 5, "PUNTAJE_ACIERTO": 10, "PUNTAJE_DESACIERTO": 3})
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    >>> obtener_confi_valida({'######'})
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    >>> obtener_confi_valida("")
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    >>> obtener_confi_valida({"LONGITUD_PALABRA_MINIMA": 6, "CANTIDAD_LETRAS_ROSCO": 6, "MAXIMO_PARTIDAS": 6, "PUNTAJE_ACIERTO": 6, "PUNTAJE_DESACIERTO": 6})
    {'LONGITUD_PALABRA_MINIMA': 6, 'CANTIDAD_LETRAS_ROSCO': 6, 'MAXIMO_PARTIDAS': 6, 'PUNTAJE_ACIERTO': 6, 'PUNTAJE_DESACIERTO': 6}
    >>> obtener_confi_valida({"LONGITUD_PALABRA_MINIMA": '5', "CANTIDAD_LETRAS_ROSCO": '5', "MAXIMO_PARTIDAS": '5', "PUNTAJE_ACIERTO": '5', "PUNTAJE_DESACIERTO": '5'})
    {'LONGITUD_PALABRA_MINIMA': 4, 'CANTIDAD_LETRAS_ROSCO': 10, 'MAXIMO_PARTIDAS': 5, 'PUNTAJE_ACIERTO': 10, 'PUNTAJE_DESACIERTO': 3}
    """
    dicc_default = {
    "LONGITUD_PALABRA_MINIMA": 4,
    "CANTIDAD_LETRAS_ROSCO": 10,
    "MAXIMO_PARTIDAS": 5,
    "PUNTAJE_ACIERTO": 10,
    "PUNTAJE_DESACIERTO": 3,
    }
    if type(dicc_configuracion) == dict and len(dicc_configuracion):
        for clave, valor in dicc_default.items():
            if not clave in dicc_configuracion.keys():
                dicc_configuracion[clave] = valor
            elif type(dicc_configuracion[clave]) != int:
                dicc_configuracion[clave] = valor
    else:
        dicc_configuracion = dicc_default
    return dicc_configuracion
    #CRUZ, ARIEL CARLOS LEONARDO​


def leer_configuracion():
    """
    La funcion lee el archivo csv y devuelve un diccionario con la configuracion del usuario
    Sin parametros
    return: diccionario con la configuracion del usuario
    """
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
    diccionario_configuracion = obtener_confi_valida(diccionario_configuracion)
    return diccionario_configuracion
    #CRUZ, ARIEL CARLOS LEONARDO​
print(doctest.testmod())

