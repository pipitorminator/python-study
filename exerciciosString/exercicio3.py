# Data por extenso. Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.


data = input("insira sua data de nascimento(separando com '/'): ")
mes =  ['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

data = data.split('/')

print("data: " + data[0] + " " + mes[int(data[1])] + " " + data[2])
