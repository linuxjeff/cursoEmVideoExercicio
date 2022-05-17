# ex031.py Calcula o preço da passagem
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Calcula o preço da passagem por quilômetro com preço mais alto por quilômetro
# para destinos até 200 quilômetros.
#
#       Exemplos:
#		./ex031.py
#       Qual a distância da viagem em quilômetros?
#       >>> 219
#       A distância é 219.0 o preço da é de: R$98.55
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-05-17, Jefferson Santana:
#       - Versão inicial
#       - Criado cabeçalho
#       - Criado a variável que recebe o número em quilômetros
#       - Criado if que calcula o preço por quilômetro
#       - Feito correção na descrição longa
#       - Colocado exemplo no cabeçalho
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

QuilometrosDaViagem = float(input('Qual a distância da viagem em quilômetros?\n>>> '))

###############################################################################
#                             Programa Principal                              #
###############################################################################
if (QuilometrosDaViagem <= 200):
    print('A distância é {} o preço da é de: R${:.2f}'.format(QuilometrosDaViagem, (QuilometrosDaViagem * 0.50)))
else:
    print('A distância é {} o preço da é de: R${:.2f}'.format(QuilometrosDaViagem, (QuilometrosDaViagem * 0.45)))
