# ex029.py Calculadora de multa
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Calcula multa de excesso de velocidade.
#
#       Exemplos:
#		./ex029.py
#       Qual foi a velocidade do veiculo?
#       >>> 154
#       Sua multa é R$518.00
#       Procure ser um motorista mais prudente!
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-05-17, Jefferson Santana:
#       - Versão inicial
#       - Criado variável para receber velocidade
#       - Criado o if para fazer o teste da velocidade
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Bibliotecas                                     #
###############################################################################

###############################################################################
#                             Variáveis                                       #
###############################################################################

velocidadeDoVeiculo = int(input('Qual foi a velocidade do veiculo?\n>>> '))

###############################################################################
#                             Programa Principal                              #
###############################################################################

if (velocidadeDoVeiculo > 80):
    print('Sua multa é R${:.2f}'.format(7*(velocidadeDoVeiculo-80)))
    print('Procure ser um motorista mais prudente!')
else:
    print('Você é um motorista prudente e andou dentro do limite. Parabéns!')
