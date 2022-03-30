# ex016.py mostra o valor inteiro.
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe um número Real e nostra sua parte inteira.
#
#       Exemplos:
#		./ex016.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-22, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

# Importando a função trunc da biblioteca math
from math import trunc

###############################################################################
#                             Variáveis                                       #
###############################################################################

numeroReal = float(input('Digite um número Real: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O valor inteiro de {} é {}'.format(numeroReal, trunc(numeroReal)))
