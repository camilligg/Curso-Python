# Faça um programa que leia duas notas de um aluno e calcule sua média.

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a N1: '))
n2 = float(input('Digite a N2: '))

print()
print('===============')
print('PORTAL DE NOTAS')
print('===============')
print()
print('Notas do Aluno(a) {}' .format(nome))
print('N1: {}' .format(n1))
print('N2: {}' .format(n2))
print('Média Final: {}' .format(((n1+n2)/2)))
