# ex005.py Mostra o número anterior e posterior de um número.
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe um número e mostra quais são o número a frente e o número atrás do nú-
# mero recebido.
#
#       Exemplos:
#		./ex005.py
#       Digiti um número: 3
#       O número anterior a 3 é 2
#       O número posterior a 3 é 4
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-20, Jefferson Santana:
#       - Modificando para usar apenas uma variável
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

numero = int(input('Digiti um número: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O número anterior a {} é {}\nO número posterior a {} é {}'.format(numero, numero - 1, numero, numero + 1))
