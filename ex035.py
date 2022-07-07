# Calcula se três retas formam um triângulo.
#
# Versão
#
#   0.0.1 2022-07-07 Jefferson
#   - Começo do programa
#   - Criado as variáveis
#   - Criado if para testar retas

# Variáveis
RetaUm = float(input('Digite o tamanho da primeira reta: '))
RetaDois = float(input('Digite o tamanho da segunda reta: '))
RetaTres = float(input('Digite o tamanho da terceira reta: '))

# If para calcular o triângulo
if  ((RetaUm + RetaDois) > RetaTres):
    if ((RetaUm + RetaTres) > RetaDois):
        if ((RetaDois + RetaTres) > RetaUm):
            print('As três retas formam um triângulo.')
        else:
            print('As três retas não formam um triângulo.')

    else:
        print('As três retas não formam um triângulo.')
else:
    print('As três retas não formam um triângolo.')
