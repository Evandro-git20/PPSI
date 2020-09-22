'''O camelô Zé da banca vende diariamente, games, calculadoras e canetas. Faça
um programa para solicitar o total de games, o total de calculadoras e o
total de canetas vendidas ao término do dia. O programa deve solicitar também
o preço de cada um dos produtos e ao final calcular e informar o total do
faturamento com cada produto e o faturamento total.'''

game = int(input('Quantidade de Games: '))
preçog = float(input('Valor: '))
calculadora = int(input('Quantidade de Calculadoras: '))
preçocalc = float(input('Valor: '))
caneta = int(input('Quantidade de canetas: '))
preçocant = float(input('Valor: '))

game *= preçog
calculadora *= preçocalc
caneta *= preçocant
ft = game + calculadora + caneta

print("Faturamento total de games: {:.2f} ".format(game))
print("Faturamento total de calculadoras: {:.2f} ".format(calculadora))
print("Faturamento total de canetas: {:.2f}".format(caneta))
print("Faturamento total: {:.2f}".format(ft))



