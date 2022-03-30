# aula-6-ex001.py Soma dois números
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Uma calculadora de adição que soma dois números.
#
#       Exemplos:
#		Coloque um exemplo
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-19, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

# Variável que recebe o primeiro número.
num = int(input('digite um número: '))

# Variável que recebe o segundo número.
ndois = int(input('digite um número: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

# Escreve o resultado da adição na tela.
print('A soma é: {}'.format(num + ndois))