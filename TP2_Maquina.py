from etapa7 import Interfaz
from etapa9 import Partida
import platform

def pasapalabra():
    archivo_user = "usuarios.csv" 
    jugadores = Interfaz(archivo_user)
    if jugadores:
        Partida(jugadores)

print(platform.platform())
print(platform.system())
pasapalabra()