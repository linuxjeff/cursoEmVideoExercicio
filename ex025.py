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
#       Digite seu nome e sobrenome
#       >>> Lucas Silva e Silva
#       A palavra silva existe no nome ou sobrenome?
#       Sim
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
#       - Versão inicial
#       - Criado o cabeçalho
#       - Criado variável para receber nome e sobrenome
#       - Criado if para teste da palavra silva
#       - Criado o print para mostrar a resposta da pergunta
#       - Colocado o exemplo no cabeçalho
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

print('A palavra silva existe no nome ou sobrenome?\n{}'.format(resposta))
