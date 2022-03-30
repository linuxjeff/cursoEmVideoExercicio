# ex009.py Mostra a tabuada
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe um número inteiro e mostra sua tabuada do 0 ao 10 na tela.
#
#       Exemplos:
#		./ex009.py
#       Digite um numero para ver sua tabuada: 5
#       ---------------
#       tabuada do: 5
#       ---------------
#       5 x  0 = 0
#       5 x  1 = 5
#       5 x  2 = 10
#       5 x  3 = 15
#       5 x  4 = 20
#       5 x  5 = 25
#       5 x  6 = 30
#       5 x  7 = 35
#       5 x  8 = 40
#       5 x  9 = 45
#       5 x 10 = 50
#       ---------------
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-20, Jefferson Santana:
#       - Mudança na frase principal
#       - Alinhamentos dos resultados
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

numero = int(input('Digite um numero para ver sua tabuada: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('-' * 15)

print('tabuada do: {}'.format(numero))

print('-' * 15)

print('{} x {:>2} = {:<4}'.format(numero, 0, numero * 0))

print('{} x {:>2} = {:<4}\n{} x {:>2} = {:<4}'.format(numero, 1, numero * 1, numero, 2, numero * 2))

print('{} x {:>2} = {:<4}\n{} x {:>2} = {:<4}'.format(numero, 3, numero * 3, numero, 4, numero * 4))

print('{} x {:>2} = {:<4}\n{} x {:>2} = {:<4}'.format(numero, 5, numero * 5, numero, 6, numero * 6))

print('{} x {:>2} = {:<3}\n{} x {:>2} = {:<4}'.format(numero, 7, numero * 7, numero, 8, numero * 8))

print('{} x {:>2} = {:<4}\n{} x {:>2} = {:<4}'.format(numero, 9, numero * 9, numero, 10, numero * 10))

print('-' * 15)
