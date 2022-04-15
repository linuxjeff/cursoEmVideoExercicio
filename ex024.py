# ex024.py mostra se a santo no nome
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe o nome da cidade e verifica se a santo no nome.
#
#       Exemplos:
#		./ex024.py
#       Digite o nome da sua cidade: Santo Amaro
#       A palavra santo esta presente no nome da cidade?
#       Sim
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
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

cidade = str(input('Digite o nome da sua cidade: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

if 'santo' not in cidade.lower():
    resposta = 'Não'
else:
    resposta = 'Sim'

print('A palavra santo esta presente no nome da cidade?\n{}'.format(resposta))
