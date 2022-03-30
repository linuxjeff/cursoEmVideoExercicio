# ex011.py Calcula quanta tinta será nesessária.
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe a altura e a largura da parede e calcula quanta tinta será nescessária
# para pintar a parede.
#
#       Exemplos:
#		./ex011.py
#       Digite a altura da parede em metros: 5
#       Digite a largura da parede em metros: 7
#       O total da área da parede é: 35 metros
#       Para pintar esta área é nescessário: 9 litros de tinta
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-20, Jefferson Santana:
#       - Mudança para float das variáveis
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

alturadaparede = float(input('Digite a altura da parede em metros: '))

larguradaparede = float(input('Digite a largura da parede em metros: '))

calculofinal = (alturadaparede * larguradaparede) / 2

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O total da área da parede é: {:.2f} metros'.format(alturadaparede * larguradaparede))

print('Para pintar esta área é nescessário: {} litros de tinta'.format(calculofinal))
