'''nomes = ['Joao', 'Maria', 'Jose']

for n in nomes:
    print(n)

print('FIM')


for num in range(0, 21, 2):
    print(num)'''



funcionario1 = {
    'nome':'João'
    ,'sobrenome':'Silva'
    ,'idade':15
    ,'salario':1999.99
    ,'ativo': True
}

funcionario2 = {
    'nome':'Maria'
    ,'sobrenome':'Souza'
    ,'idade':21
    ,'salario':2999.99
    ,'ativo': False
}
funcionarios = [funcionario1, funcionario2]

for chave, valor in funcionario1.items():
    print(chave, valor)


for fun in funcionarios:
    print(fun)