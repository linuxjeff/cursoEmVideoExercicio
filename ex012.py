# ex012.py calcula o desconto
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe o preço do produto e devolve seu valor com desconto.
#
#       Exemplos:
#		./ex012.py
#       Qual o preço do produto: 50
#       Preço do produto sem desconto: R$50.00
#       Preço do produto com 5% de desconto: R$47.50
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

valor = int(input('Qual o preço do produto: '))

# Cancula o desconto
desconto = (valor / 100) * 95

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('Preço do produto sem desconto: R${:.2f}'.format(valor))

print('Preço do produto com 5% de desconto: R${:.2f}'.format(desconto))
