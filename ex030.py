# ex030.py Par ou Impar
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Programa verifica se número digitado é par ou impar
#
#       Exemplos:
#		Coloque um exemplo
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-05-17, Jefferson Santana:
#       - Versão inicial
#       - Criado cabeçalho
#       - Criado variável para recolher número
#       - Criado variável para recolher o resto da divisão
#       - Criado if para verificar se número é par ou impar
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

Numero = int(input('Digite um número: '))

RestoDaDivisao = Numero % 2

###############################################################################
#                             Programa Principal                              #
###############################################################################

if (RestoDaDivisao == 1):
    print('O número {} é impar.'.format(Numero))
else:
    print('O número {} é par'.format(Numero))
