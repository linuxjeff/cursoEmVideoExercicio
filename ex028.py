# ex028.py Jogo de adivinha
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# O CPU escolhe um numero de 1 a 5 e o jogador tem que adivinhar qual foi.
#
#       Exemplos:
#		./ex028.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-05-17, Jefferson Santana:
#       - Versão inicial
#       - Colocado o cabeçalho
#       - Importado a função randrange
#       - Criado variável que guarda o número
#       - Criado a variável para recolher o numero do jogador
#       - Criado o if que verifica o acerto ou erro do número
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################
from random import randrange
###############################################################################
#                             Variáveis                                       #
###############################################################################

numero = randrange(0, 6)

numeroDoJogador = int(input('Eu pensei em um número de zero a cinco.\nQual é?\n>>> '))

###############################################################################
#                             Programa Principal                              #
###############################################################################
if ( numero == numeroDoJogador):
    print('O número que eu pensei foi: {}'.format(numero))
    print('Você aceitou o número. ;)')
else:
    print('O número que eu pensei foi: {}'.format(numero))
    print('Você errou o número. :D')