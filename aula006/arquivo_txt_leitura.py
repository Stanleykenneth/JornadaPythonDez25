with open('aula006/funcionarios.txt', 'r', encoding='utf-8') as arquivo:    
    for linha in arquivo:
        print('Nome: ', linha.strip())
