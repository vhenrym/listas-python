lista = [3, 10, 6, 1, 4, 5, 10, 200]
print(lista)

#len(lista): retorna o tamanho da lista
print(len(lista))

#min(lista): retorna o menor valor
print(min(lista))

nomes = ['Paulo', 'Ana', 'Joao']
print(max(nomes))

#sum(lista): retorna o somatório da lista
print(sum(lista))

media = sum(lista) / len(lista)
print(media)

#append(item): insere um item no final da lista
lista = [4, 6, 10, 3, 4, 3, 1]
lista.append(100)
print(lista)
lista.append(200)
print(lista)

#insert(indice, item): insere um item em um indice específico da lista
lista.insert(0, 300)
print(lista)

#pop(indice): remove um item de um indice
lista.pop()
print(lista)

#remove(lista): remove a primeira ocorrencia de um item
lista.remove(100)
print(lista)

#remover todas as ocorrencia de um item
while 3 in lista:
    lista.remove(3)
print(lista)

#index(item): retorna o indice de um item na lista
print(lista.index(6))

#lista.sort(): ordena uma lista em ordem crescente
lista = [5, 8, 10, 4, 1, 200, 60]
lista.sort(reverse=True)
print(lista)

#lista com ordem decrescente
nomes = ['Paulo', 'Ana', 'Joao']
nomes.sort()
print(nomes)

#count(item): Retorna a quantidade de ocorrencia de um item
lista = [4, 6, 6, 4, 7, 8, 9, 6]
print(lista.count(6))

#concatenação de listas *ajunta as listas*
lista1 = [4, 6, 7, 8]
lista2 = [9, 10, 11]
lista3 = lista1 + lista2
print(lista3)