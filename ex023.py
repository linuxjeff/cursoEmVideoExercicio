# ex023.py Lê um número e mostra suas casa
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Lê um número de 0 a 9999 e mostra unidade, dezena, centena e milhar.
#
#       Exemplos:
#		./ex023.py
#       Digite um número de 0 a 9999
#       >>> 8426
#       O número tem:
#       Unidade 6
#       Dezena 2
#       Centena 4
#       Milhar 8
#
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-05-01, Jefferson Santana:
#       - Bug de números com menos de 4 caracteres resolvido
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

numero = str(input('Digite um número de 0 a 9999\n>>> '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
###############################################################################
#                             Programa Principal                              #
###############################################################################
# Bug: não funciona com numeros sem os quatro caractéres.
# Bug resolvido, mas tive que ver a resolução. :(

print('O número tem:\nUnidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(u, d, c, m))
