from interfaz_grafica import interfaz_usuario
from pasapalabra_v2 import iniciar_partida
import os
import platform

def pasapalabra():
    archivo_user = os.path.join("recursos","usuarios.csv")
    jugadores = interfaz_usuario(archivo_user)
    if jugadores:
        iniciar_partida(jugadores)

print(platform.platform())
print(platform.system())
pasapalabra()