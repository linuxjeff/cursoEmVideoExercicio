# ex017.py Descrição curta
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Descrição longa
#
#       Exemplos:
#		./ex017.py
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

from math import hypot

###############################################################################
#                             Variáveis                                       #
###############################################################################

catetooposto = float(input('Digite o comprimento do cateto oposto: '))

catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('A hipotenusa vai medir: {}'.format(hypot(catetooposto, catetoadjacente)))
