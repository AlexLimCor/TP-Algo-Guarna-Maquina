from etapa7 import Interfaz
from etapa10 import definir_configuracion
from etapa9 import Partida

def pasapalabra():
    archivo_user = "usuarios.csv" 
    jugadores = Interfaz(archivo_user)
    if jugadores:
        definir_configuracion()
        Partida(jugadores)

pasapalabra()
