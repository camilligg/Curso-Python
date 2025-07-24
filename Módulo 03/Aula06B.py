
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input('Digite algo: ')
print('Informações sobre o conteúdo digitado: ')
print('O conteúdo digitado é do tipo ', type(entrada))
print('Só tem espaços? ', entrada.isspace())
print('O conteúdo digitado é numérico? ', entrada.isdigit())
print('O conteúdo digitado é alfabético? ', entrada.isalpha())
print('O conteúdo digitado é alfanumérico? ', entrada.isalnum())
print('O conteúdo está em maiúsculas? ', entrada.isupper())
print('O conteúdo está em minúsculas? ', entrada.islower())
print('O conteúdo está capitalizado? ', entrada.istitle())