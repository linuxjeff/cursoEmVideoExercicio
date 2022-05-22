# ex032.py Fala se um ano é bissexto
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# O programa recebe um ano digitado pelo usuário e verifica se ele é bissexto.
#
#       Exemplos:
#		Coloque um exemplo
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-05-22, Jefferson Santana:
#       - Versão inicial
#       - Criado o cabeçalho
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

from calendar import leapdays

###############################################################################
#                             Variáveis                                       #
###############################################################################

AnoDoCalcular = int(input('Qual o ano que você quer saber se é bissexto?\n>>> '))

AnoMaisUm = AnoDoCalcular + 1

RespostaDoBissexto = leapdays(AnoDoCalcular, AnoMaisUm)

###############################################################################
#                             Programa Principal                              #
###############################################################################

if (RespostaDoBissexto > 0):
     print('O ano {} é bisexto.'.format(AnoDoCalcular))
else:
     print('O ano {} não é bissexto'.format(AnoDoCalcular))