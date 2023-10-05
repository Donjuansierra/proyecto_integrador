from readchar import readkey, key
import os

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

def limpiar_pantalla():
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


numeros = numero()
