# Faça um programa que leia a altura e a largura de uma parede, calcule a sua área e a quantidade de tinta necessária para pintar toda a parede. 
# Obs: cada litro de tinta pinta 2m².

altura = float(input('Dê a altura da parede que deseja pintar: '))
largura = float(input('Dê a largura da parede que deseja pintar: '))

area = altura * largura 
tinta = area/2

print()
print('Para pintar uma parede de {}m, será preciso de {} litros de tinta' . format(area, tinta))