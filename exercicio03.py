'''Faça um programa para solicitar o código, a quantidade de alunos do sexo
masculino, a quantidade de alunos do sexo feminino e a quantidade de alunos
aprovados de uma determinada turma.
Calcular e informar: a porcentagem de alunos do sexo masculino; a porcentagem
de alunos do sexo feminino; a porcentagem de alunos reprovados; o total de
alunos da turma.'''

codigo = int(input('Digite o código: '))
aluno_M = int(input('Quantidade de Alunos: '))
aluno_F = int(input('Quantidade de alunas: '))
alunos_aprov = int(input('Quantidade de alunos aprovados: '))
print('Porcentagem de alunos: ', (aluno_M * 100//100), '%')
print('Porcentagem de alunas: ', (aluno_M * 100//100), '%')
print('Porcentagem de alunos aprovados: ', (alunos_aprov * 100//100), '%')
print('Total de alunos da turma: ', (aluno_M + aluno_F))
