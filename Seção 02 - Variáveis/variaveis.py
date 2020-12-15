# Definindo uma variável int e float
a = 3
b = 4.4

print(a + b)


# Definindo uma variável de texto
texto = 'Sua idade é... '
idade = 23
print(texto + str(idade))
print(f'{texto} {idade}!')


# Imprimindo string
print(3 * 'Bom Dia! ')


# Criando uma Interação com o Usuário
pi = 3.14
raio = float(input('Informe o raio da circuferência: '))
area = pi * raio * raio
# area = pi * pow(raio, 2) outra forma de calcular com uma função Bult-in

print(f'A área da circuferência é {area} m2.')
