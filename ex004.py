# aula-6-desafio-2.py mostra varios "is"
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Pede ao usuário que digite algo e devolve varios "is" como informações.
#
#       Exemplos:
#		./aula-6-desafio-2.py
#       Digite algo: Python
#       A variável é do tipo: <class 'str'>
#       O que foi digitado é alfabeto? True
#       O que foi digitado é número? False
#       O que foi digitado é alfanumerico? True
#       O que foi digitado está em letras minúsculas? False
#       O que foi digitado está em letras maiúsculas? False
#       O que foi digitado é um espaço em branco? False
#       O que foi digitado esta dentro da tabela ASCII? True
#       O que foi digitado está capitalizado? True
#
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-19, Jefferson Santana:
#       - Versão inicial
#   v0.0.2 2022-03-19, Jefferson Santana:
#       - Trocando as quebras de linhas por espaços
#   v0.0.3 2022-03-19, Jefferson Santana:
#       - Colocando a função capitalizada
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

algos = input('Digite algo: ')

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('A variável é do tipo: {}'.format(type(algos)))
print('O que foi digitado é alfabeto? {}'.format(algos.isalpha()))
print('O que foi digitado é número? {}'.format(algos.isnumeric()))
print('O que foi digitado é alfanumerico? {}'.format(algos.isalnum()))
print('O que foi digitado está em letras minúsculas? {}'.format(algos.islower()))
print('O que foi digitado está em letras maiúsculas? {}'.format(algos.isupper()))
print('O que foi digitado é um espaço em branco? {}'.format(algos.isspace()))
print('O que foi digitado esta dentro da tabela ASCII? {}'.format(algos.isascii()))
print('O que foi digitado está capitalizado? {}'.format(algos.istitle()))