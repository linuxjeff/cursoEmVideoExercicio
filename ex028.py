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

###############################################################################
#                             Programa Principal                              #
###############################################################################
