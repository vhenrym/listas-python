#Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba:
#a. a lista com todos os itens armazenados.
#b. o somatório de todos os números contidos na lista.
#c. o maior número da lista.
#d. o menor número da lista.

import random

lista = []
for i in range(20):
    numero = random.randint(1, 50)
    lista.append(numero)
    print(lista)


    print(f'Somatório: {sum(lista)}')
    print(f"Menor: {min(lista)}")
    print(f'Maior: {max(lista)}')