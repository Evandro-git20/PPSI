'''Crie um programa para ler a matrícula, o nome e o salário de dois empregados.
Descontar 5% no salário do primeiro e acrescentar 9% no salário do segundo.
Informar: o valor do desconto do primeiro; o valor do acréscimo do segundo; o
salário final do primeiro; o salário final do segundo.
'''

nome1 = input('Nome do 1º empregado: ')
matricula1 = int(input('Digite a matrícula: '))
salario1 = float(input('Digite o salário'))

nome2 = input('Nome do 2º empregado: ')
matricula2 = int(input('Digite a matrícula: '))
salario2 = float(input('Digite o salário'))

print('Salário com 5% de desconto: {:.2f}'.format(salario1 * 95/100))
print('Salário com 9% de acréscimo: {:.2f}'.format(salario2 * 109/100))
