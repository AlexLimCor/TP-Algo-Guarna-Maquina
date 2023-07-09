# ---------- ETAPA 7 ----------------- 
from tkinter import messagebox
import doctest

# VARIABLES TEXTO
ERROR_NOMBRE_CLAVE_INVALIDO = "Usuario o clave no valido"
ERROR_NOMBRE_EXISTENTE = "Por favor ingrese otro nombre"
ERROR_CLAVE_NO_COINCIDENTE = "Las claves no coinciden"
ERROR_NOMBRE_INVALIDO = "Por favor ingrese un nombre que sea de longitud mayor o igual a 4 caracteres y un maximo de 20, estar formado solo por letras,numeros y el guion medio '-' "
ERROR_CLAVE_INVALIDO = "Recuerda que debe tener por lo menos una mayuscula,una minuscula,un numero y alguno de los siguientes caracteres especiales: #, !"
REGISTRO_EXITO = "Se registro con exito"
#---- NOMBRE ---- 
def crear_nombre(nombre):
    '''
    >>> crear_nombre("alex")
    'alex'
    >>> crear_nombre("Juan1")
    'Juan1'
    >>> crear_nombre('marcelo-3')
    'marcelo-3'
    >>> crear_nombre('ADRIAN')
    'ADRIAN'
    >>> crear_nombre('@lex')
    False
    >>> crear_nombre('ale')
    False
    >>> crear_nombre('alexissanchezdelgados')
    False
    '''
    MIN = 4
    MAX = 20
    caracter_especial = ["-"]
    indice = 0
    Usuario = True
    if len(nombre) >= MIN and len(nombre) <= MAX:
        while indice < len(nombre) and Usuario:
            caracter = nombre[indice]
            if caracter.isalnum() or caracter in caracter_especial:
                Usuario = True
            else:
                Usuario = False
            indice +=1
    else:
        Usuario = False
    if Usuario:
        Usuario = nombre
    return Usuario
    #LIMACHI CORDERO, ALEX​

#----CLAVE----#
def crear_clave(clave):
    '''
    >>> crear_clave('Japon2#')
    'Japon2#'
    >>> crear_clave('master')
    False
    >>> crear_clave('123456')
    False
    >>> crear_clave('maquina#')
    False
    >>> crear_clave('Maquina12#!13')
    False
    >>> crear_clave('Canción!#1')
    'Canción!#1'
    >>> crear_clave('hola')
    False
    '''
    LONG_MIN = 6
    LONG_MAX = 12
    lista_especial = ["#","!"]
    vocales_acent = ["á","é","í","ó","ú"]
    mayus = 0
    mins = 0
    numero = 0
    especial = 0
    vocal = 0
    error= 0
    VALIDO = 1
    indice = 0
    validar_clave = False
    if len(clave) >= LONG_MIN and len(clave) <= LONG_MAX:
        while error == 0 and indice < len(clave):
            if clave[indice] in lista_especial:
                especial +=1
            elif clave[indice].isupper():
                mayus+=1
            elif clave[indice].islower():
                mins +=1
            elif clave[indice].isnumeric():
                numero +=1
            elif clave[indice] in vocales_acent:
                vocal +=1
            else:
                error +=1
            indice +=1
        if especial and mayus and mins and numero >= VALIDO and vocal >= 0 and error == 0:
            validar_clave = clave

    return validar_clave
    #LIMACHI CORDERO, ALEX​


# ---------------- Manejo de archivos ------------------- #

#Leemos el archivo 
def leer_archivo(arUser):
    linea = arUser.readline().rstrip()
    if not linea:
        linea = ","
    Registro = linea.split(",")
    return Registro


#Escribimos en el archivo el usuario y clave 
def grabar_usuario(arUser,nombre,clave):
    arUser.write(f"{nombre},{clave}\n")


def iniciar_sesion(arUser,nombre,clave):
    validacion = False
    with open(arUser,"r") as linea:
        usuario,contrasenia = leer_archivo(linea)
        while usuario and contrasenia and not validacion:
            if nombre == usuario and contrasenia == clave:
                validacion = True
            usuario,contrasenia = leer_archivo(linea)
    if not validacion:
        messagebox.showerror("",ERROR_NOMBRE_CLAVE_INVALIDO)
    return validacion

#Registrar al usuario y validamos todos los pasos
def registro_usuario(arUser,usuario,clave1,clave2):
    nombre = crear_nombre(usuario)
    contrasenia = crear_clave(clave1)
    repet_contrasenia = crear_clave(clave2)
    if nombre:
        if contrasenia and repet_contrasenia:
            if repet_contrasenia == contrasenia:
                with open(arUser,"r+") as linea:
                    username,clave = leer_archivo(linea)
                    validar = True
                    if not username:
                        linea.seek(0,0)
                    while username and clave:
                        if username == nombre:
                            validar = False
                        username,clave = leer_archivo(linea)                 
                    if validar:       
                        grabar_usuario(linea,nombre,contrasenia)
                        messagebox.showinfo("",REGISTRO_EXITO)
                    else:
                        messagebox.showerror("",ERROR_NOMBRE_EXISTENTE)
            else:
                messagebox.showerror("",ERROR_CLAVE_NO_COINCIDENTE)
        else:
            messagebox.showerror("",ERROR_CLAVE_INVALIDO)      
    else:
        messagebox.showerror("",ERROR_NOMBRE_INVALIDO)  


print(doctest.testmod())
