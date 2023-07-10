from tkinter import Tk,messagebox,Frame,Label,Entry,Button
from registro_usuario import iniciar_sesion,registro_usuario
from configuracion_juego import escribir_dicc_configuracion,leer_configuracion
import os,random

#-----------------------ETAPA 7 ---------------------------------------#
# MENSAJES
TEXTO_LONGITUD_PALABRA_MINIMA = "LONGITUD_PALABRA_MINIMA"
TEXTO_CANTIDAD_LETRAS_ROSCO = "CANTIDAD_LETRAS_ROSCO"
TEXTO_MAXIMO_PARTIDAS = "MAXIMO_PARTIDAS"
TEXTO_PUNTAJE_ACIERTO = "PUNTAJE_ACIERTO"
TEXTO_PUNTAJE_DESACIERTO = "PUNTAJE_DESACIERTO"

# VENTANA USUARIO
TITULO_VENTANA_USUARIO = "PasaPalabra-Maquina"
ICONO = os.path.join("recursos","pasapalabra.ico")
TAMANIO_VENTANA_USUARIO = "400x300"
TEXTO_BIENVENIDO = "Bienvenido"
TEXTO_USUARIO = "Usuario"
TEXTO_CLAVE = "Clave"
TEXTO_USUARIOS_CONECTADOS = "Usuarios conectados"
TEXTO_RESTRICCION = "Solo pueden jugar hasta 4 personas"
TEXTO_VER = "ver"
TEXTO_ACCEDER = "Acceder"
TEXTO_REGISTRO = "Registrarse"
TEXTO_CONFIG = "Config"
TEXTO_JUGAR = "Jugar"
TEXTO_OCULTAR = "Ocultar"
TEXTO_MAX_JUGADORES = "Haz llegado al tope maximo de jugadores"

# VENTANA REGISTRO
TITULO_VENTANA_REGISTRO = "Registro de usuario"
TAMANIO_VENTANA_REGISTRO = "300x150"
TEXTO_NOMBRE = "Ingrese un nombre"
TEXTO_INGRESE_CLAVE = "Ingrese Clave"
TEXTO_REPETIR_CLAVE = "Repite la Clave"

# VENTANA CONFIGURACION
TAMANIO_VENTANA_CONFIG = "350x150"
TEXTO_RESTRICCION_CONFIG = "Recuerda poner valores positivos"
TEXTO_BOTON_ACEPTAR = "Aceptar"
TITULO_VENTANA_CONFIG = "Ventana de configuracion"

# VENTANA TURNOS
TITULO_VENTANA_TURNOS = "Lista de Turnos"
TEXTO_TURNO = "Turnos"
TEXTO_BOTON_EMPEZAR = "Empezar"
TAMANIO_VENTANA_TURNOS = "300x200"


#----------------------- INTERFAZ GRAFICA ----------------------------- #
# Ventana principal 
def ventana_usuario(arUser):
    #------Ventanas----
    ventana = Tk()
    ventana.title(TITULO_VENTANA_USUARIO)
    ventana.geometry(TAMANIO_VENTANA_USUARIO)
    ventana.iconbitmap(ICONO)
    ventana.resizable(False,False)
    #---frame---
    login = Frame(ventana,width=200,height=300)
    login.pack()
    #----- TEXTO
    titulo = Label(login,text=TEXTO_BIENVENIDO,font=("Arial",15))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)
    # ---- Texto para el Entry -- 
    nombre_label = Label(login,text=f"{TEXTO_USUARIO}:")
    nombre_label.grid(column=0,row=1,sticky="w")

    clave_label = Label(login,text=f"{TEXTO_CLAVE:}")
    clave_label.grid(column=0,row=2,sticky="w")

    Label(ventana,text=f"{TEXTO_RESTRICCION}.",fg="red").pack()
    Label(ventana,text=f"{TEXTO_USUARIOS_CONECTADOS}:").pack()

    conectados_label = Label(ventana,text="")
    conectados_label.pack()
    # Cuadros de texto en el frame
    nombre_entry = Entry(login)
    nombre_entry.grid(column=1,row=1)

    clave_entry = Entry(login)
    clave_entry.grid(column=1,row=2)
    clave_entry.config(show="*")

    #---- Button del frame  ---
    boton_visual = Button(login,text=f"{TEXTO_VER}",command=lambda: ver_ocultar_clave())
    boton_visual.grid(column=2,row=2,padx=3)

    boton_ingresar = Button(login,text=TEXTO_ACCEDER,command=lambda: mostrar_usuarios_conectados())
    boton_ingresar.grid(column=0,row=3)

    boton_registrarse = Button(login,text=TEXTO_REGISTRO,command=lambda: ventana_registro(arUser))
    boton_registrarse.grid(column=1,row=3)

    boton_configuracion = Button(login,text=f"{TEXTO_CONFIG}.",command=lambda: ventana_configuracion())
    boton_configuracion.grid(column=2,row=3)

    boton_jugar = Button(ventana,text=TEXTO_JUGAR,command=lambda: eliminar_ventana_usuario())
    boton_jugar.pack()

    boton_jugar.pack_forget()

    # Funcion para ver/ocultar clave:
    def ver_ocultar_clave():
        if clave_entry["show"] == "*":
            clave_entry["show"] = ""
            boton_visual["text"] = TEXTO_OCULTAR
        else:
            clave_entry["show"] = "*"
            boton_visual["text"] = TEXTO_VER
    #--- Acceso a jugar y Mostrar en pantalla los usuarios conectados, Tiene como maximo 4 jugadores para ingresar 
    def mostrar_usuarios_conectados():
        nombre = nombre_entry.get()
        clave = clave_entry.get()
        #Buscamos si la clave y el usuario se haya escrito correctamente
        valido = iniciar_sesion(arUser,nombre,clave)
        MAX_USER = 4
        if valido:
            if len(lista_usuarios) < MAX_USER:
                lista_usuarios.append(nombre)
                boton_jugar.pack()
                listar_usuario()
            else:
                messagebox.showerror("",TEXTO_MAX_JUGADORES)



    def listar_usuario():
        #Mostramos el nombre en pantalla del usuario que ingresa 
        estados_texto = "\n".join(lista_usuarios)
        conectados_label.config(text=estados_texto)

    # --- Cerrar ventana y jugar
    def eliminar_ventana_usuario():
        ventana.destroy()


    # Se almacena los usuarios que vayan ingresando 
    lista_usuarios = []
    ventana.mainloop()
    return lista_usuarios
    #LIMACHI CORDERO, ALEX​

# --- Nueva ventana de registro -- 
def ventana_registro(arUser):
    ventana_secundaria = Tk()
    ventana_secundaria.title(TITULO_VENTANA_REGISTRO)
    ventana_secundaria.geometry(TAMANIO_VENTANA_REGISTRO)
    ventana_secundaria.resizable(False,False)

    mi_frame = Frame(ventana_secundaria)
    mi_frame.pack()
    # Texto
    titulo_secundario = Label(mi_frame,text=TEXTO_REGISTRO,font=("Arial",13))
    titulo_secundario.grid(column=0,row=0)
    # Label 
    crear_usuario_label = Label(mi_frame,text=f"{TEXTO_NOMBRE}:")
    crear_usuario_label.grid(column=0,row=1,sticky="e")

    crear_clave_label = Label(mi_frame,text=f"{TEXTO_INGRESE_CLAVE}:")
    crear_clave_label.grid(column=0,row=2,sticky="e")

    repetir_clave = Label(mi_frame,text=f"{TEXTO_REPETIR_CLAVE}:")
    repetir_clave.grid(column=0,row=3,sticky="e")
    # CuadroDe Texto  ENTRY
    cuadro_usuario = Entry(mi_frame)
    cuadro_usuario.grid(column=1,row=1)

    cuadro_clave = Entry(mi_frame)
    cuadro_clave.grid(column=1,row=2)
    cuadro_clave.config(show="*")

    cuadro_repetir_clave = Entry(mi_frame)
    cuadro_repetir_clave.grid(column=1,row=3)
    cuadro_repetir_clave.config(show="*")

    # Boton 
    boton_acceder = Button(ventana_secundaria,text=TEXTO_ACCEDER,command=lambda: registro_usuario(arUser,cuadro_usuario.get(),cuadro_clave.get(),cuadro_repetir_clave.get()))
    boton_acceder.pack()

    ventana_secundaria.mainloop()

def ventana_configuracion():
    dicc = leer_configuracion()
    LONGITUD_PALABRA_MINIMA = dicc[TEXTO_LONGITUD_PALABRA_MINIMA] 
    CANTIDAD_LETRAS_ROSCO = dicc[TEXTO_CANTIDAD_LETRAS_ROSCO]
    MAXIMO_PARTIDAS = dicc[TEXTO_MAXIMO_PARTIDAS]
    PUNTAJE_ACIERTO = dicc[TEXTO_PUNTAJE_ACIERTO]
    PUNTAJE_DESACIERTO = dicc[TEXTO_PUNTAJE_DESACIERTO]

    ventana = Tk()
    ventana.title(TITULO_VENTANA_CONFIG)
    ventana.geometry(TAMANIO_VENTANA_CONFIG)
    ventana.resizable(0,0)

    # FRAME
    frame_config = Frame(ventana)
    frame_config.pack()

    # Texto
    palabra_minima = Label(frame_config,text=f"{TEXTO_LONGITUD_PALABRA_MINIMA}:")
    palabra_minima.grid(column=0,row=0,sticky="e")

    letras_rosco = Label(frame_config,text=f"{TEXTO_CANTIDAD_LETRAS_ROSCO}:") 
    letras_rosco.grid(column=0,row=1,sticky="e")

    max_partidas = Label(frame_config,text=f"{TEXTO_MAXIMO_PARTIDAS}:")
    max_partidas.grid(row=2,column=0,sticky="e")

    puntaje_positivo = Label(frame_config,text=f"{TEXTO_PUNTAJE_ACIERTO}:")
    puntaje_positivo.grid(row=3,column=0,sticky="e")

    puntaje_negativo = Label(frame_config,text=f"{TEXTO_PUNTAJE_DESACIERTO}:")
    puntaje_negativo.grid(row=4,column=0,sticky="e")

    Label(ventana,text=TEXTO_RESTRICCION_CONFIG,fg="red").pack()

    # Cuadro de texto
    cuadro_palabra_minima = Entry(frame_config)
    cuadro_palabra_minima.grid(column=1,row=0)
    cuadro_palabra_minima.insert(0,str(LONGITUD_PALABRA_MINIMA))

    cuadro_letras_rosco = Entry(frame_config)
    cuadro_letras_rosco.grid(column=1,row=1)
    cuadro_letras_rosco.insert(0,str(CANTIDAD_LETRAS_ROSCO))

    cuadro_max_partidas = Entry(frame_config)
    cuadro_max_partidas.grid(column=1,row=2)
    cuadro_max_partidas.insert(0,str(MAXIMO_PARTIDAS))

    cuadro_puntaje_positivo = Entry(frame_config)
    cuadro_puntaje_positivo.grid(column=1,row=3)
    cuadro_puntaje_positivo.insert(0,str(PUNTAJE_ACIERTO))

    cuadro_puntaje_negativo = Entry(frame_config)
    cuadro_puntaje_negativo.grid(column=1,row=4)
    cuadro_puntaje_negativo.insert(0,str(PUNTAJE_DESACIERTO))

    # Boton 
    boton_config = Button(ventana,text=TEXTO_BOTON_ACEPTAR,command= lambda: escribir_dicc_configuracion(cuadro_palabra_minima.get(),cuadro_letras_rosco.get(),cuadro_max_partidas.get(),cuadro_puntaje_positivo.get(),cuadro_puntaje_negativo.get()))
    boton_config.pack()

    ventana.mainloop()

#Seleccionamos al azar los nombres para dar comienzo al turno
def seleccion_azar(arUser):
    nombres = ventana_usuario(arUser)
    seleccion = random.sample(nombres,len(nombres))
    return seleccion

# Mostramos en ventana los turnos de los usuarios que ingresan 
def ventana_turnos(arUser):

    MIN = 0
    MAX = 4
    lista_nombres = seleccion_azar(arUser)
    ventana_terciaria = Tk()
    ventana_terciaria.geometry(TAMANIO_VENTANA_TURNOS)
    ventana_terciaria.resizable(False,False)
    ventana_terciaria.title(TITULO_VENTANA_TURNOS)

    titulo = Label(ventana_terciaria,text=f"{TEXTO_TURNO}:",font=("Arial",10))
    titulo.pack()
    contador = 1
    for element in lista_nombres:
        etiqueta = Label(ventana_terciaria,text=f"{contador}_{element}")
        etiqueta.pack()
        contador +=1
    boton_empezar = Button(ventana_terciaria,text=TEXTO_BOTON_EMPEZAR,command= lambda: eliminar_ventana_terciaria())
    boton_empezar.pack()
    def eliminar_ventana_terciaria():
        ventana_terciaria.destroy()
    # Se ejecuta cuando la cantidad de usuarios sea la indicada 
    if len(lista_nombres) > MIN and len(lista_nombres) <= MAX:
        # Boton para empezar el juego
        ventana_terciaria.mainloop()

    return lista_nombres



# Unimos todas las ventanas 
def interfaz_usuario(arUser):
    lista_nombres = ventana_turnos(arUser)
    return lista_nombres

'''archivo = "usuarios.csv"
interfaz_usuario(archivo)'''

