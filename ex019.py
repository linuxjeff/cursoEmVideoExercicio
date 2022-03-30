# ex019.py Descrição curta
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Descrição longa
#
#       Exemplos:
#		./ex019.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-22, Jefferson Santana:
#       - Versão inicial
#   v0.0.1 2022-03-23, Jefferson Santana:
#       - Finalizado a função de sorteio.
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

from random import choice

###############################################################################
#                             Variáveis                                       #
###############################################################################

aluno1 = input('Qual o nome do primeiro aluno?\n>>> ')

aluno2 = input('Qual o nome do segundo aluno?\n>>> ')

aluno3 = input('Qual o nome do terceiro aluno?\n>>> ')

aluno4 = str(input('Qual o nome do quarto aluno?\n>>> '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O aluno a limpar o quadro é: {}'.format(choice([aluno1, aluno2, aluno3, aluno4])))
