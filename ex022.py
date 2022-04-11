# arquivo.py Recebe nome e sobrenome
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe nome e sobrenome e mostra varias curiosidades.
#
#       Exemplos:
#		./ex022
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-11, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

nome = input('Digite seu nome e sobrinome\n>>> ')

lista_do_split = nome.split()

tudojunto = ''.join(lista_do_split)

###############################################################################
#                             Programa Principal                              #
###############################################################################

print(nome.upper())

print(nome.lower())

print(len(tudojunto))