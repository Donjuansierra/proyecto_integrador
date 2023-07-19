from readchar import readkey, key

name = input ('Hello gamer, put your name or nickname: ') 

print(f'{name}, welcome to this game !!!')


while True:
    k = readkey()
    if k == key.UP:
        break
    else:
        print(k)

