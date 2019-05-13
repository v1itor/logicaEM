#Este é o meu primeiro programa em Python!

from random import randint #Importa a função de gerar números aleatórios

print("Boa sorte aos jogadores!")

dado1 = randint(1,6) # gera um número entre 1 e 6 aleatoriamente
print("dado do player 1 :" , dado1)

dado2 = randint(1,6)
print("dado do player 2 :" , dado2)

if dado1 > dado2: #}"if" Verifica se a variável dado1 é ">" maior que a variável dado2
    print("Player 1 ganhou")

if dado2 > dado1:
    print("player 2 ganhou")
