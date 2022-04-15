# ex026.py descobre as letras a
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe uma frase e descobre quantas letras a a frase possui e qual posição
# esta a primeira e em qual posição esta a última.
#
#       Exemplos:
#		./ex026.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
#       - Versão inicial
#       - Criado o cabeçalho
#       - Criado variável para receber frase
#       - Criado o print que conta os números de a na frase
#       - Criado o print que mostra a posição do primeiro a
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

frase = str(input('Digite uma frase\n>>> '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('A letra a aparece: {}'.format(frase.lower().count('a')))

print('O primeiro a esta na posição: {}'.format(frase.lower().find('a')))
