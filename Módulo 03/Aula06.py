# receba dois valores do usuário e imprima a soma dos dois


# n1 = input('Digite um número: ')
# n2 = input('Digite mais um número: ')

# s = n1 + n2 
# print('A soma vale ', s)

# esse código não funciona, pois s = n1 + n2 está realizando uma concatenção, não uma adição 

# como resolver ??

# AULA 06 - TIPOS PRIMITIVOS

n1 = int(input('Digite um número: ')) # tudo que está dentro de int() será convertido para o tipo inteiro 
n2 = int (input('Digite mais um número: ')) 

s = n1 + n2 
print('A soma vale ', s)
print('A soma entre {} e {}, vale: {}'.format(n1, n2, s))
print('A soma vale {}' .format(s))

# O .format() é um método de strings em Python usado para inserir variáveis ou valores em um texto de forma organizada e flexível. 
# Ele é especialmente útil quando você precisa montar mensagens dinâmicas.

nome = input('Digite o seu nome: ')
print('Olá, {:^20}' .format(nome))
print('Olá, {:=^20}' .format(nome))
print('Seja bem-vindo(a)!')
