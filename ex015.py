# ex015.py Calcula o aluguel dos carros
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Pede os quilomêtros rodados e os dias e calcula o valor a ser pago.
#
#       Exemplos:
#		./ex015.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-17, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

kmro = float(input('Quantos quilomêtros foram rodados?\n>>> '))

dias = int(input('Quantos dias foram utilizados?\n>>> '))

totalu = (dias * 60) + (kmro * 0.15)

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O total do aluguesl é: R${:.2f}'.format(totalu))