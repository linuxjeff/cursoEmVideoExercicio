# ex023.py Lê um número e mostra suas casa
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Lê um número de 0 a 9999 e mostra unidade, dezena, centena e milhar.
#
#       Exemplos:
#		./ex023.py
#       Digite um número de 0 a 9999
#       >>> 8426
#       O número tem:
#       Unidade 6
#       Dezena 2
#       Centena 4
#       Milhar 8
#
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

numero = str(input('Digite um número de 0 a 9999\n>>> '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O número tem:\nUnidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(numero[3], numero[2], numero[1], numero[0]))
