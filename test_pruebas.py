#-----------ETAPA 1 y ETAPA 9 ---------------#
from etapa1 import Verificar
from etapa7 import crear_clave,crear_usuario
# Validamos que sea una palabra correcta 
def test_palabra():
    # Prueba 1 = Si se ingresa un numero 
    resultado = Verificar("argent2")
    assert resultado == False

    # Prueba 2 =  Si se ingresa un caracter especial    
    resultado = Verificar("@rgent")
    assert resultado == False

    # Prueba 3 = Si se ingresa mayuscula , 
    resultado = Verificar("ARGENT")
    assert resultado == True

    # Prueba 4 = Si se ingresa alguna vocal acentuada
    resultado = Verificar("canción")
    assert resultado == True

    print("Exito")

test_palabra()


# --------- Etapa 7-----------#
# Crear usuario
def test_usuario():
    '''
    El nombre que se ingresa debe tener como minimo un largo de 4 caracteres,y un maximo de 20, puede estar formado solo por
    letras,numeros, y el guion medio "-" 
    
    '''
    # Prueba 1 = Si se ingresa una long de 3 caracteres 
    resultado = crear_usuario("Ale")
    assert resultado == False

    # Prueba 2 = Si se ingresa una long mas de 20 caracteres 
    resultado = crear_usuario("alexismaldonadosanchez")
    assert resultado == False

    # Prueba 3 = Si se ingresa algun caracter especial 
    resultado =  crear_usuario("@lex")
    assert resultado == False

    # Prueba 4 = Un usuario que contenga todo lo solicitado
    resultado = crear_usuario("Alex-1")
    assert resultado == "Alex-1"

    print("Exito")
test_usuario()


# Crear clave
def test_clave():
    '''
    Debemos validar si lo que ingresa cumple con las siguientes condiciones:
    1. Longitud  entre 6 y 12 caracteres
    2. Debe estar formado por caracteres alfanumericos,a excepcion de las letras acentuadas y los caracteres "#" "!"
    3. Debe contener al menos una mayuscula, una minuscula, un numero y alguno de los siguientes caracteres "#" "!"
    '''
    # Prueba 1 = No cumple la condicion de la longitud
    respuesta = crear_clave("messi")
    assert respuesta == False

    # Prueba 2 = no esta formado por lo que pide
    respuesta = crear_clave("@lexmessi")
    assert respuesta == False

    # Prueba 3 = Cumple con todas las condiciones
    respuesta = crear_clave("Alex123#")
    assert respuesta == "Alex123#"

    # Prueba 3 = Cumple con las condiciones y tiene una letra acentuada
    respuesta = crear_clave("Aléx123#")
    assert respuesta == "Aléx123#"

    print("Exito")

test_clave()
