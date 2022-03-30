# ex013.py Calcula novo salário
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe o atual salário do funcionário e calcula o novo salário com almento de
# 15 porcento.
#
#       Exemplos:
#		./ex013.py
#       Qual o salário atual do funcionario?
#       >>> 1000
#       O salário atual é: R$1000.00
#       O novo salário com 15 porcento de reajuste é: R$1150.00
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

salarioatual = int(input('Qual o salário atual do funcionario?\n>>> '))

novosalario = ((salarioatual / 100) * 15) + salarioatual

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O salário atual é: R${:.2f}'.format(salarioatual))

print('O novo salário com 15 porcento de reajuste é: R${:.2f}'.format(novosalario))
