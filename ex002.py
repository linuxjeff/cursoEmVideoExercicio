# ex002.py Pergunta o nome do usuário
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Pergunta o nome do usuário e escreve uma frase de saudação.
#
#       Exemplos:
#           ./ex002.py
#           Digiti seu nome: Jefferson
#           É um prazer te conhecer, Jefferson!
#
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-19, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-19, Jefferson Santana:
#       - Melhorando o programa com .format
#   v0.0.3 2022-03-19, Jefferson Santana:
#       - Melhorando o input que solicita o nome do usuário.
#   v0.0.4 2022-03-19, Jefferson Santana:
#       - Troca do exemplo
#       - Separando licença de vercionameno
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

nome = input('Digiti seu nome: ')

###############################################################################
#                             Programa Principal                              #
###############################################################################

# Imprimindo a frase de saudação.
print('É um prazer te conhecer, {}!'.format(nome))
