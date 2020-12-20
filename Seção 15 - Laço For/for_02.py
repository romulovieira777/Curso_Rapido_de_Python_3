# Declando Duas Listas
pessoas = ['Gui', 'Rebeca']
adjetivos = ['Sapeca', 'Inteligente']


# Percorrendo as Duas Listas Utilizando for
for p in pessoas:
    for a in adjetivos:
        # Imprimindo Valores na Tela
        print(f'{p} é {a}!')


# Passando uma Classe Vazia
for i in [1, 2, 3]:
    pass


# Utilizando o Continue no for
for i in range(1, 11):
    # Criando uma Condição If
    if i % 2:
        # Continuando
        continue
    # Imprimindo o Valor de i se for Par
    print(i)


# Utilizando o Break no for
for i in range(1, 11):
    # Criando uma Condição If
    if i == 5:
        # Saindo o Laço
        break
    print(i)


# Imprimindo o Valor na Tela
print('Fim!!!')
