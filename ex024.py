# ex024.py mostra se a santo no nome
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe o nome da cidade e verifica se a santo no nome é a primeira.
#
#       Exemplos:
#		./ex024.py
#       Digite o nome da sua cidade: Ribeirão Preto
#       Sua cidade não tem a palavra Santo!
#
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-04-15, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-05-03, Jefferson Santana:
#       - Bug de espaço no inicio consertado
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

# lcidade = cidade.lower()
#
# slcidade = lcidade.strip()

###############################################################################
#                             Programa Principal                              #
###############################################################################

if (cidade.strip().lower().find('santo') == 0):
    print('Sua cidade tem a palavra Santo!' )
else:
    print('Sua cidade não tem a palavra Santo!')
