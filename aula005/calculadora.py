from calculo import soma, subtracao, multiplicacao, divisao 

numero1 = float(input('Digite o primeiro Número: '))
numero2 = float(input('Digite o Segundo Número: '))


r1 = soma(numero1, numero2)
r2 = subtracao(numero1, numero2)
r3 = multiplicacao(numero1, numero2)
r4 = divisao(numero1, numero2)

print('Soma: ',r1)
print('Subtração: ',r2)
print('Multiplicação: ',r3)
print('Divisão: ',r4)
