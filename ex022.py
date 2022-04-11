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
#       Digite seu nome e sobrinome
#       >>> Jefferson Vitor de Santana
#       JEFFERSON VITOR DE SANTANA
#       jefferson vitor de santana
#       O total de caracteres é: 23
#       O total de caracteres do seu nome é: 9
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

so_o_nome = lista_do_split[0]

###############################################################################
#                             Programa Principal                              #
###############################################################################

print(nome.upper())

print(nome.lower())

print('O total de caracteres é: {}'.format(len(tudojunto)))

print('O total de caracteres do seu nome é: {}'.format(len(so_o_nome)))
