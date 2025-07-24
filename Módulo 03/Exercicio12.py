# Faça um programa que lê o preço de um produto e mostra o novo preço do produto com 5% de desconto.

preco = float(input('Digite o valor atual do produto: '))
novoPreco = preco - (preco*0.05)

print()
print('O valor do produto com desconto de 5% é {}' .format(novoPreco))