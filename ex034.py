# programa para cancular aumento.
#
# Versão
#
#   0.0.1 2022-13-06 Jefferson
#   - Começo do programa
#   - Criada as varáveis para recolher nome e salário
#   - Criado if para cálcular o aumento.

# Variáveis
NomeDoFuncionario = str(input('Digite o nome do funcionario: ')).capitalize()
ValorAtualDoSalario = float(input('Qual o valor do salário: R$ '))

# If para efetuar o cálculo
if  (ValorAtualDoSalario <= 1250.00 ):
    Aumento = (ValorAtualDoSalario / 100) * 15
else:
    Aumento = (ValorAtualDoSalario / 100) * 10
