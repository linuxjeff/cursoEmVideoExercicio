# ex014.py converte temperatura
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Converte de graus celsius para fahrenheit
#
#       Exemplos:
#		./ex014.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-21, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

celsius = float(input('Digite a temperatura em celsius: '))

fahrenheit = (celsius * 9/5) + 32

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('{:.1f} celsius é {:.1f} fahrenheit'.format(celsius, fahrenheit))
