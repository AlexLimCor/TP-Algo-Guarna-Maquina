from interfaz_grafica import interfaz_usuario
from dinamica_juego_v2 import iniciar_partida
import platform

def pasapalabra():
    archivo_user = "recursos/usuarios.csv" 
    jugadores = interfaz_usuario(archivo_user)
    if jugadores:
        iniciar_partida(jugadores)

print(platform.platform())
print(platform.system())
pasapalabra()