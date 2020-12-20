# Criando um Laço Utilizando for
for i in range(10):
    # Imprimindo Valor na Tela
    prin(i)


# Criando um Laço Utilizando for Iniciando em 1
for i in range(1, 10):
    # Imprimindo Valor na Tela
    print(i)


# Criando um Laço Utilizando for Iniciando em 1 e Passando de 7 em 7
for i in range(1, 100, 7):
    # Imprimindo Valor na Tela
    print(i)


# Criando um Laço Utilizando for Iniciando em 20 e Passando de -3 em -3
for i in range(20, 0, -3):
    # Imprimindo Valor na Tela
    print(i)


# Declarando uma Lista de Números
numeros = [2, 4, 6, 8]

# Percorrendo a Lista Utilizando for
for n in numeros:
    # Imprimindo Valor na Tela
    print(n)
    # Utilizando o end= para Imprimir na Tela em Linha
    priint(n, end= ' ')


# Criando uma String
texto = 'Python é muito massa!'

# Percorrendo a String Utilizando o for
for letra in texto:
    # Imprimindo Valor na Tela
    print(letra)
    # Utilizando o end= para Imprimir na Tela em Linha
    print(letra, end=' ')


# Percorrendo um Set
for i in {1, 2, 3, 4, 4, 4}:
    # Utilizando o end= para Imprimir na Tela em Linha
    print(i, end=' ')


# Criando um Dicionário
produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desconto': 0.5
}

# Percorrendo o Dicionário
for atributo in produto:
    # Imprimindo Valor na Tela da Chave e Valor
    print(atributo, produto[atributo])


# Outra Forma de Percorrer o Dicionário
for atributo, valor in produto.items():
    # Imprimindo Valor na Tela da Chave e Valor
    print(atributo, valor)


# Percorrendo só os Valores
for valor in produto.valor():
    # Imprimindo Valor na Tela Utilizando o end= para Imprimir em Linha
    print(valor, end=' ')


# Percorrendo só as Chaves
for chaves in produto.keys():
    # Imprimindo as Chaves na Tela Utilizando o end= para Imprimir em Linha
    print(chaves, end=' ')
