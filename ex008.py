# ex008.py Mostra conversão de metros
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Converte metros em cetímetros e milímetros.
#
#       Exemplos:
#		./ex008.py
#       Digite um número de metros: 253
#       O valor de 253.0 metros em quilômetro é: 0.253km
#       O valor de 253.0 metros em hectômetros é: 2.53hm
#       O valor de 253.0 metros em decâmetros é: 25.3dam
#       O valor de 253.0 metros em decímetros é: 2530dm
#       O valor de 253.0 metros em centímetros é: 25300cm
#       O valor de 253.0 metros em milímetros é: 253000mm
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-20, Jefferson Santana:
#       - Adicionando mais unidades
#       - Troca da variánte para float
#       - Retirado do ponto flutuante de mm, cm e dm
#       - Melhora na edentação do texto no dos printes
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

# Recebe os metros a ser convertidos.
metros = float(input('Digite um número de metros: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O valor de {} metros em quilômetro é: {}km'.format(metros, metros / 1000))

print('O valor de {} metros em hectômetros é: {}hm'.format(metros, metros / 100))

print('O valor de {} metros em decâmetros é: {}dam'.format(metros, metros / 10))

print('O valor de {} metros em decímetros é: {:.0f}dm'.format(metros, metros * 10))

print('O valor de {} metros em centímetros é: {:.0f}cm'.format(metros, metros * 100))

print('O valor de {} metros em milímetros é: {:.0f}mm'.format(metros, metros * 1000))
