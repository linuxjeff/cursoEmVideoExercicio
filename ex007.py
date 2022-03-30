# ex007.py Calcula a média
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe duas notas de um aluno e calcula a média.
#
#       Exemplos:
#		./ex007
#       Qual o nome do aluno?
#       >>> João
#       Digite a primeira nota: 8
#       Digite a segunda nota: 7
#       A média do aluno João é de: 7.5
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-20, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-20, Jefferson Santana:
#       - Retirando a variável media
#   v0.0.3 2022-03-20, Jefferson Santana:
#       - Mudando números para float
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

# Recebe o nome do aluno.
nome = input('Qual o nome do aluno?\n>>> ')

# Recebe a primeira nota do aluno.
nota1 = float(input('Digite a primeira nota: '))

# Recebe a segunda nota do aluno.
nota2 = float(input('Digite a segunda nota: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('A média do aluno {} é de: {:.1f}'.format(nome, (nota1 + nota2) / 2))
