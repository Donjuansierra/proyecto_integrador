import os
import readchar
import random
from typing import List, Tuple
from class_juego import Juego


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas: str):
        lista_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(lista_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()

        lineas = contenido.strip().split('\n')
        coordenadas = list(map(int, lineas[0].split()))
        mapa = [list(row) for row in lineas[1:]]
        posicion_inicial = (coordenadas[0], coordenadas[1])
        posicion_final = (coordenadas[2], coordenadas[3])

        super().__init__(mapa, posicion_inicial, posicion_final)

