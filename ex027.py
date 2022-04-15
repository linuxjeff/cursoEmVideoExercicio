# ex027.py Recebe nome e sobrenome
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe nome e sobrenome e mostra o primeiro nome e o último sobrenome.
#
#       Exemplos:
#		./ex027.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
#       - Versão inicial
#       - Criado cabeçalho
#       - Criado variável que recebe o nome e sobrenome
#       - Criado o split para pegar o primeiro nome e plintar na tela
#       - Criado o rsplit para pegar o útilmo sobrenome
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

nome_sobrenome = str(input('Qual seu nome e sobrenome?\n>>> '))

feito_split = nome_sobrenome.split()

feito_rsplit = nome_sobrenome.rsplit(maxsplit=1)

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O primeiro nome é: {}'.format(feito_split[0]))

print('O último sobrenome é: {}'.format(feito_rsplit[1]))
