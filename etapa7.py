from tkinter import *
from tkinter import messagebox 
import random
#Leemos el archivo 
def leer(arUser):
    linea = arUser.readline()
    linea = linea.rstrip("\n")
    if not linea:
        linea = ","
    Registro = linea.split(",")
    return Registro

#Escribimos en el archivo el usuario y clave 
def grabarUsuarioClave(arUser,User,clave):
    arUser.write(User + "," + clave + "\n")

#Solo tomamos el nombre del usuario en el registro para despues buscar si hay usuarios con el mismo nombre 
def Usuario(arUser):
    USUARIO = 0
    nombre = leer(arUser)
    return nombre[USUARIO]
#---- USUARIO ---- 
def crear_usuario(nombre):
    '''
    Verificamos que el nombre que ingrese cumpla con las condiciones
    Y este devuelve el nombre si la condicion es valida sino un valor booleano en este caso False
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
#----Crear Clave----
def crear_clave(clave):
    '''
    Validamos si el usuario ingresa una clave
    y retorna la clave si es verdadero y en en caso contrario un False
    
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
    validarClave = False
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
            validarClave = clave

    return validarClave

#Buscamos si el usuario se encuentra en el archivo
def Buscar(arUser,usuario):
    INICIO = 0
    nombre = crear_usuario(usuario)
    with open(arUser,"r") as linea:
        user = Usuario(linea)
        if nombre:
            while user:
                if user == nombre:
                    nombre = False
                user = Usuario(linea)
    return nombre

#Registrar al usuario y validamos todos los pasos
def Registrarse(arUser,usuario,clave1,clave2):
    nombre = Buscar(arUser,usuario)
    contrasenia = crear_clave(clave1)
    repet_contrasenia = crear_clave(clave2)
    if nombre:
        if contrasenia and repet_contrasenia:
            if repet_contrasenia == contrasenia:
                with open(arUser,"a") as linea:
                    grabarUsuarioClave(linea,nombre,contrasenia)
                messagebox.showinfo("","Exito")
            else:
                messagebox.showerror("","Las claves no coinciden")
        else:
            messagebox.showerror("Clave no valido","Recuerda que debe tener por lo menos una mayuscula,una minuscula,un numero y alguno de los siguientes caracteres especiales: #, !")
    else:
        messagebox.showerror("Usuario no valido o Existente","Por favor ingrese otro nombre")  
    
#Iniciar sesion
def IniciarSesion(arUser,usuario,clave):
    with open(arUser,"r") as linea:
        nombre,contrasenia = leer(linea)
        validacion = False
        while nombre and contrasenia and not validacion:
            if nombre == usuario and contrasenia == clave:
                validacion = True
            nombre,contrasenia = leer(linea)
        if not validacion:
            messagebox.showerror("","Usuario o clave no valido")
    #Colocamos el puntero al inicio para poder usar a futuro el archivo
    #arUser.seek(INICIO)
    return validacion


#----------------------- INTERFAZ GRAFICA ----------------------------- #
# Creamos un Ventana principal de "Bienvenido al juego"
def ventana_principal(arUser):
    # Esta funcion me devuelve los usuarios ingresados en forma de lista #
    #------Ventanas----
    ventana = Tk()
    ventana.title("PasaPalabra-Maquina")
    ventana.geometry("400x300")
    ventana.iconbitmap("pasapalabra.ico")
    #---frame---
    login = Frame(ventana,width=200,height=300)
    login.pack()
    #----- TEXTO
    titulo = Label(login,text="Bienvenido",font=("Arial",15))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)
    # ---- Texto para el Entry -- 
    nombreLabel = Label(login,text="Usuario:")
    nombreLabel.grid(column=0,row=1,sticky="w")

    claveLabel = Label(login,text="Clave:")
    claveLabel.grid(column=0,row=2,sticky="w")

    Label(ventana,text="Solo pueden jugar hasta 4 personas",fg="red").pack()
    Label(ventana,text="Usuarios conectados :").pack()

    ConectadosLabel = Label(ventana,text="")
    ConectadosLabel.pack()
    # Cuadros de texto en el frame
    nombreEntry = Entry(login)
    nombreEntry.grid(column=1,row=1)

    claveEntry = Entry(login)
    claveEntry.grid(column=1,row=2)
    claveEntry.config(show="*")

    #---- Button del frame  ---
    botonVisual = Button(login,text="ver",command=lambda: Visualizar())
    botonVisual.grid(column=2,row=2,padx=3)

    botonIngresar = Button(login,text="Acceder",command=lambda: Verificar())
    botonIngresar.grid(column=0,row=3)

    botonRegistrarse = Button(login,text="Registrarse",command=lambda: ventana_secundaria(arUser))
    botonRegistrarse.grid(column=1,row=3)

    botonJugar = Button(ventana,text="Jugar",command=lambda: BorrarVentana())
    botonJugar.pack()
    botonJugar.pack_forget()

    # Funcion para ver/ocultar clave:
    def Visualizar():
        if claveEntry["show"] == "*":
            claveEntry["show"] = ""
            botonVisual["text"] = "Ocultar"
        else:
            claveEntry["show"] = "*"
            botonVisual["text"] = "Ver"
    #--- Acceso a jugar y Mostrar en pantalla los usuarios conectados, Tiene como maximo 4 jugadores para ingresar 
    def Verificar():
        user = nombreEntry.get()
        clave = claveEntry.get()
        #Buscamos si la clave y el usuario se haya escrito correctamente
        valido = IniciarSesion(arUser,user,clave)
        MAX_USER = 4

        if valido:
            if len(Usuarios) < MAX_USER:
                Usuarios.append(user)
                botonJugar.pack()
                mostrar_estado()
            else:
                messagebox.showerror("","Haz llegado al tope maximo de jugadores")



    def mostrar_estado():
        #Mostramos el estado de cada usuario, si esta conectado se muestra en pantalla
        estados_texto = "\n".join(Usuarios)
        ConectadosLabel.config(text=estados_texto)

    # --- Cerrar ventana y jugar
    def BorrarVentana():
        ventana.destroy()


    # Se almacena los usuarios que vayan ingresando 
    Usuarios = []
    ventana.mainloop()
    return Usuarios

# --- Nueva ventana de registro -- 
def ventana_secundaria(arUser):
    ventana_secundaria = Tk()
    ventana_secundaria.title("Registro de usuario")
    ventana_secundaria.geometry("300x150")
    ventana_secundaria.resizable(False,False)

    miFrame = Frame(ventana_secundaria)
    miFrame.pack()
    # Texto
    titulo_secundario = Label(miFrame,text="Registro",font=("Arial",13))
    titulo_secundario.grid(column=0,row=0)
    # Label 
    CrearUsuarioLabel = Label(miFrame,text="Ingrese un nombre:")
    CrearUsuarioLabel.grid(column=0,row=1,sticky="e")

    CrearClaveLabel = Label(miFrame,text="Ingrese Clave:")
    CrearClaveLabel.grid(column=0,row=2,sticky="e")

    RepetirClave = Label(miFrame,text="Repite la Clave:")
    RepetirClave.grid(column=0,row=3,sticky="e")
    # CuadroDe Texto  ENTRY
    CuadroUsuario = Entry(miFrame)
    CuadroUsuario.grid(column=1,row=1)

    CuadroClave = Entry(miFrame)
    CuadroClave.grid(column=1,row=2)
    CuadroClave.config(show="*")

    CuadroClave2 = Entry(miFrame)
    CuadroClave2.grid(column=1,row=3)
    CuadroClave2.config(show="*")

    # Boton 
    botonAcceder = Button(ventana_secundaria,text="Acceder",command=lambda: Validacion(arUser))
    botonAcceder.pack()

    def Validacion(arUser):
        #Usamos la funcion creada anteriormente para validar lo que ingresa el usuario
        nombre = CuadroUsuario.get()
        clave1 = CuadroClave.get()
        clave2 = CuadroClave2.get()
        Registrarse(arUser,nombre,clave1,clave2)
        ventana_secundaria.destroy()
    ventana_secundaria.mainloop()

#----------- Seleccionamos al azar los nombres para dar comienzo al turno
def Eleccion(arUser):
    usuarios = ventana_principal(arUser)
    seleccion = random.sample(usuarios,len(usuarios))
    return seleccion

#---- Mostramos en ventana los turnos de los usuarios que ingresan 
def mostrar_eleccion(arUser):
    MIN = 0
    MAX = 4
    seleccion = Eleccion(arUser)
    ventana = Tk()
    ventana.geometry("300x200")
    ventana.resizable(False,False)
    ventana.title("Lista de Turnos")

    Titulo = Label(ventana,text="Turnos:",font=("Arial",10))
    Titulo.pack()
    contador = 1
    for element in seleccion:
        etiqueta = Label(ventana,text=f"{contador} {element}")
        etiqueta.pack()
        contador +=1
    # Se ejecuta cuando la cantidad de usuarios sea la indicada 
    if len(seleccion) > MIN and len(seleccion) <= MAX:
        ventana.mainloop()
    return seleccion


#---- Empezar juego---#
def Interfaz(arUser):
    lista_usuarios = mostrar_eleccion(arUser)
    return lista_usuarios

#usuarios_csv = "usuarios.csv"
#print(Interfaz(usuarios_csv))



