print("jogo de dados:")
from random import randint

dados1 = randint(1, 6)
print("Primeiro dado do player 1:", dados1)
dados2 = randint(1, 6)
print("Segundo dado do player 2:", dados2)
dados3 = randint(1, 6)
print("Primeiro dado do Player 2:", dados3)
dados4 = randint(1, 6)
print("Segundo dado do player 2: ", dados4)

jogador1 = dados1 + dados2
jogador2 = dados3 + dados4

print("Gerando resultado...")

if jogador1 > jogador2:
    print("Player 1 win!")
else:
    if jogador1 < jogador2:
        print("Player 2 win!")
    else:
        print("Empatou!")