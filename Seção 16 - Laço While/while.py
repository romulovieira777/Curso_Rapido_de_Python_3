# Declarando uma Variável
x = 0

# Criando o Laço While
while x != -1:
    # Criando a Variável para o Usuário Inserir um Valor
    x = float(input('Informe o número ou -1 para sair: '))

# Imprimindo na Tela o Valor
print('Fim!')


# Declarando Três Variável
total = 0
quantidade = 0
nota = 0

# Criando o Laço While
while total != -1:
    # Criando uma Variável para o Usuário Inserir um Valor
    nota = float(input('Informe a nota ou -1 para sair: '))

    # Criando um IF para Verificar se a Nota é Difernte -1
    if nota != -1:
        # Se a Nota for Diferente ela será Somada e Acresentada a Quantidade
        quantidade += 1
        total += nota

# Imprimindo o Valor Médio na Tela
print(f'A média da turma é {total / quantidade}')


# Declarando uma Variável
x = 10

# Criando um Laço While
while x:
    # Imprimindo o Valor na Tela
    print(x)

    # Subtraindo da Variável x Declarada
    x -= 1

# Imprimindo o Valor na Tela
print('Fim!')
