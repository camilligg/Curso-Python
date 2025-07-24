# Faça um programa que receba um valor em metros, e exiba ele em centímetros e milímetros.

# 1 metro = 100 centimetros
# 1 metro = 1000 milimetros

metros = float(input('Digite o valor em metros: '))

print()
print('=========')
print('CONVERSÃO')
print('=========')
print()
print('Valor em metros: {}' .format(metros))
print('Valor em centímetros: {}' .format(metros * 100))
print('Valor em milímetros: {}' .format(metros * 1000))