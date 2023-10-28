import os
import readchar
from typing import List, Tuple

name = input ('Hello gamer, put your name or nickname: ') 

print(f'{name}, welcome to this game !!!')


"""
Codigo que permite leer caracteres del teclado y se detiene cuando se presiona la tecla flecha arriba o UP

while True:
    k = readkey()
    if k == key.UP:
        break
    else:
        print(k)

"""        
# Función que permite limpiar la terminal 

"""def limpiar_pantalla():
	os.system('cls' if os.name=='nt' else 'clear')
	
# Función que imprime  
	
def numero():
	n = 0
	while n <= 50:
		print(n)
		alpha_k = readkey()
		if alpha_k == 'n':
			n+= 1
			limpiar_pantalla()
		else:
			print('Oprime la tecla n para continuar')


numeros = numero() """

def string_to_matrix(laberinto: str):
    return [list(row) for row in laberinto.strip().split('\n')]


laberinto = """..###########
....#.......#
###.#.###.###
#...#...#...#
#.#####.#.#.#
#...#.#.#.#.#
#.#.#.#####.#
#.#.....#.#.#
#.###.###.#.#
#.#.........#
###.#####.###
#.......#...#
###########.#"""

mapa = string_to_matrix(laberinto)


def screen(mapa):

    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    for row in mapa:
        print(''.join(row))


def main_loop(mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
    px, py = posicion_inicial
    mapa[py][px] = 'P'

    screen(mapa)

    while (px, py) != posicion_final:
        key = readchar.readkey()

        x, y = 0, 0
        if key == readchar.key.UP:
            x, y = -1, 0
        elif key == readchar.key.DOWN:
            x, y = 1, 0
        elif key == readchar.key.LEFT:
            x, y = 0, -1
        elif key == readchar.key.RIGHT:
            x, y = 0, 1

        new_px, new_py = px + x, py + y

        if (0 <= new_px < len(mapa) and
            0 <= new_py < len(mapa[0]) and
            mapa[new_px][new_py] != '#'
            ):
            mapa[px][py] = '.'
            px, py = new_px, new_py
            mapa[px][py] = 'P'

            screen(mapa)


# Definir las coordenadas iniciales y finales
start = (0, 0)
end = (len(mapa) - 1, len(mapa[0]) - 1)

# Iniciar el bucle principal
main_loop(mapa, start, end)
