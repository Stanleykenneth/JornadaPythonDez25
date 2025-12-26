from time import sleep

nomes = ['Joao', 'Maria', 'Jose', 'Pedro']


numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1


index = 0
while index < len(nomes):
    print(nomes[index])
    index += 1

#-----------------------------------------------------------------------------------------------#

opcao = -1

while opcao != 0:
    print('='*20, 'Modulo Usuário', '='*20, '\n')
    print('\t1 - Cadastrar')
    print('\t2 - Editar')
    print('\t3 - Listar')
    print('\t4 - Deletar')
    print('\t0 - Sair')
    print('='*20, 'Menu', '='*20, '\n')

    opcao = int(input('\nDigite uma opção: '))

    match opcao:
        case 0:
            print('Saindo...')
        case 1:
            print('Casdatrando...')
        case 2:
            print('Editando...')
        case 3:
            print('Listando...')
        case 4:
            print('Deletando...')
        case _:
            print('Invalido...')
    sleep(2)    