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
listaDeNomes = []

listaDeNomes.append(aluno1)

listaDeNomes.append(aluno2)

listaDeNomes.append(aluno3)

listaDeNomes.append(aluno4)

###############################################################################
#                             Programa Principal                              #
###############################################################################

shuffle(listaDeNomes)

for i in listaDeNomes:
    print('{}'.format(i))
