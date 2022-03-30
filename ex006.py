# ex006.py Calcula o dobro, o triplo e sua raiz quadrada.
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe um número e calcula seu dobro, seu triplo e sua raiz quadrada.
#
#       Exemplos:
#		./ex006.py
#       Digite um número: 2
#       O dobro de 2 é 4
#       O triplo de 2 é 6
#       A raiz qudrada de 2 é 1.41
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Removendo a variável dobro
#       - Removendo a variável triplo
#       - Removendo a variável raizq
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

numero = int(input('Digite um número: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O dobro de {} é {}'.format(numero, numero * 2))

print('O triplo de {} é {}'.format(numero, numero * 3))

print('A raiz qudrada de {} é {:.2f}'.format(numero, numero ** (1/2)))
