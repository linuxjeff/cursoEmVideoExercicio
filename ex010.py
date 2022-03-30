# ex010.py Caculo de cotação
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Calcula quanto dolares da para se comprar com um número x de reais.
#
#       Exemplos:
#		./ex010.py
#        Digite o valor em reais: R$1520
#        Com R$1520.00 da para comprar $464.83
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-20, Jefferson Santana:
#       - Trocando para número float
#       _ Adicionado R$ a pergunta
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

reaisvalor = float(input('Digite o valor em reais: R$'))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('Com R${:.2f} da para comprar ${:.2f}'.format(reaisvalor, reaisvalor / 3.27))
