# ex025.py encontra os Silva
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Programa recebe um nome e sobrenome e procura por silva no mesmo.
#
#       Exemplos:
#		./ex025.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
#       - Versão inicial
#       - Criado o cabeçalho
#       - Criado variável para receber nome e sobrenome
#       - Criado if para teste da palavra silva
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

nome_sobrenome = str(input('Digite seu nome e sobrenome\n>>> '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

if 'silva' in nome_sobrenome.lower():
    resposta = 'Sim'
else:
    resposta = 'Não'
