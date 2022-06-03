# ex033.py Verifca a ordem dos números
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Recebe três números e vê qual é o maior e qual é o menor.
#
#       Exemplos:
#		Coloque um exemplo
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-05-22, Jefferson Santana:
#       - Versão inicial
#       - Criado cabeçalho
#   v0.0.2 2022-05-27, Jefferson Santana:
#       - Criado variável para receber o primeiro número
#       - Criado variável para receber o segundo número
#       - Criado variável para receber o terceiro número
#       - Correção na gramática das variáveis
#   v0.0.2 2022-06-03, Jefferson Santana:
#       - Criado if para teste do maior numero
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

PrimeniroNumero = int(input('Digite um número inteiro: '))

SegundoNumero = int(input('Digite um número inteiro: '))

TerceiroNumero = int(input('Digite um número interiro: '))

###############################################################################
#                             Programa Principal                              #
###############################################################################
# if para teste do maior número
if (PrimeniroNumero > SegundoNumero):
    if (PrimeniroNumero > TerceiroNumero):
        MaiorNumero = PrimeniroNumero
    else:
        MaiorNumero = TerceiroNumero
else:
    if (SegundoNumero > TerceiroNumero):
        MaiorNumero = SegundoNumero
    else:
        MaiorNumero = TerceiroNumero
