# ex020.py Sorte a ordem de apresentação
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe o nomes dos alunos e sortea a ordem de apresentação.
#
#       Exemplos:
#		./ex020.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-24, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################
from random import shuffle
###############################################################################
#                             Variáveis                                       #
###############################################################################

aluno1 = input('Qual o nome do primeiro aluno?\n>>> ')

aluno2 = input('Qual o nome do segunda aluno?\n>>> ')

aluno3 = input('Qual o nome terceiro aluno?\n>>> ')

aluno4 = input('Qual o nome do quarto aluno?\n>>> ')

posicao = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
listaDeNomes = [aluno1, aluno2, aluno3, aluno4]

###############################################################################
#                             Programa Principal                              #
###############################################################################

shuffle(listaDeNomes)

print('A ordem de apresentação será: ')
for i in listaDeNomes:
    print('{}'.format(i))

# print('O primeiro aluno é: {1}\n O segundo aluno é {2}\n O terceiro aluno é: {3}\n O quarto aluno é: {4}'.format(shuffle(listaDeNomes)))
