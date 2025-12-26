# Estrutura decisão - Match-Case = Switch-Case

# CRUD
print('='*20, 'Modulo Usuário', '='*20, '\n')
print('\t1 - Cadastrar')
print('\t2 - Editar')
print('\t3 - Listar')
print('\t4 - Deletar')
print('='*20, 'Menu', '='*20, '\n')

opcao = int(input('\nDigite uma opção: '))

match opcao:
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
