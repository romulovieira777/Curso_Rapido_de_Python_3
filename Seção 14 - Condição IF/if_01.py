# Declarando uma Variável
nota = float(input('Informe a nota do aluno: '))

# Criando a COndição If(Se)
if nota >= 9:
    # Imprimindo na Tela do Usuário
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra!')

# Condição elif (Se)
elif nota >= 7:
    # Imprimindo na Tela do Usuário
    print('Aprovado!')

# Condição elif (Se)
elif nota >= 5.5:
    # Imprimindo na Tela do Usuário
    print('Recuperação!')

# Condição elif (Se)
elif nota >= 3.5:
    # Imprimindo na Tela do Usuário
    print('Recuperação + Trabalho!')

# Condição Else (Se Não)
else:
    # Imprimindo na Tela do Usuário
    print('Reprovado!')

# Imprimindo na Tela do Usuário
print(nota)
