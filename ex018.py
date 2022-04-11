# ex018.py calcula seno, cosseno e tangente
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe um angulo e calcula seno, cosseno e tangente.
#
#       Exemplos:
#		Coloque um exemplo
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-30, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

from math import cos, sin, tan, radians

###############################################################################
#                             Variáveis                                       #
###############################################################################

angulo = float(input('Qual é o angulo que deseja calcular?\n>>> '))

rangul = radians(angulo)

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O angulo é {:.2f}\n Seu seno é {:.2f}\n Seu cosseno é {:.2f}\n Sua tangente é {:.2f}'.format(angulo, sin(rangul), cos(rangul), tan(rangul)))
