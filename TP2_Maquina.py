from interfaz_grafica import interfaz_usuario
from dinamica_juego_v2 import iniciar_partida

def pasapalabra():
    """
    Inicio del juego
    """
    archivo_user = "recursos/usuarios.csv" 
    jugadores = interfaz_usuario(archivo_user)
    if jugadores:
        iniciar_partida(jugadores)

pasapalabra()