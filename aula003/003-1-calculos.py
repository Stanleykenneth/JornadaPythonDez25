import math

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro numero: '))

soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2
expo = numero1 ** numero2
resto = numero1 % numero2



print(f'Soma: {soma}')
print(f'Subitração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {div}')
print(f'Exponenciação: {expo}')
print(f'Resto da Divisão: {resto}')
print(f'Raiz Quadrada da soma: {math.sqrt(soma):.2f}')