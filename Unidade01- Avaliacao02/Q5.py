#aluno: Elton Victor Da Costa - 20241014050024
#aluna: Kaillany Felix Souza - 20242014050021
import datetime

# Capturar a data de hoje usando datetime
date = datetime.datetime.today()
dia = date.day
mes = date.month
year = date.year

# Definindo a data de referência (27/04/1968)
data_inicial = datetime.date(1968, 4, 27)

# Definindo a data de hoje com os valores capturados
data_hoje = datetime.date(year, mes, dia)

# Calculando a diferença em dias entre as datas
diferenca = data_hoje - data_inicial
dias_passados = diferenca.days

# Calculando o número de sábados passados (1 sábado a cada 7 dias)
sábados_passados = dias_passados // 7

# Exibindo os resultados
print(f"Dias passados desde 27/04/1968: {dias_passados}")
print(f"Número de sábados desde 27/04/1968: {sábados_passados}")

