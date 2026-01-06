# arquivo = open('aula006/funcionarios.txt', 'a')
# arquivo.write('João Silva\n')
# arquivo.close()

with open('aula006/funcionarios.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Marina Silva\n')
   
