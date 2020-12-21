# Criando uma Função
def saudacao():
    # Imprimindo o Valor na Tela
    print('Bom Dia!')


# Criando uma Função com Parâmetro
def saudacao(nome):
    # Imprimindo o Valor na Tela
    print(f'Bom dia {nome}!')


# Criando uma Função com o Valor Padrão
def saudacao(nome = 'Pessoa'):
    # Imprimindo o Valor na Tela
    print(f'Bom dia {nome}!')


# Função com Dois Parâmetros e Valores Padrão
def saudacao(nome = 'Pessoa', idade = 20):
    # Imprimindo o Valor na Tela
    print(f'Bom dia {nome}!\nVocê nem parece ter {idade} anos!')


# Deixando a Funçaõ como Principal
if __name__ == '__main__':
    saudacao('Ana', idade = 30)


# Criando uma Função com Três Parâmetros
def soma_e_multiplicacao(a, b, x):
    # Retona o Valor da Operação
    return a + b * x
