import random

lista = []
for i in range(10):
    n = random.randint(1, 10)
    lista.append(n)
print(lista)

numero = int(input('Informe um número: '))
quantidade = 0
for item in lista:
    if item == numero:
        quantidade += 1
        print(f'Aparece {quantidade} vezes')
