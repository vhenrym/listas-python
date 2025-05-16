lista_nomes = []
lista_idades = []
for i in range(10):
    nome = input("Nome: ")
    lista_nomes.append(nome)
    idade = int(input("Idade: "))
    lista_idades.append(idade)

    print(lista_nomes)
    print(lista_idades)

    for i in range(len(lista_idades)):
        if lista_idades[i] >= 10:
            print(lista_nomes[i])