# Dicionário define a representação do tipo de dados
# Dicionário = Json
# Funcionário

nome = 'João'
sobrenome = 'Silva'
idade = 15
salario = 1999.99
ativo = True

# chave-valor
funcionario = {
    'nome':'João'
    ,'sobrenome':'Silva'
    ,'idade':15
    ,'salario':1999.99
    ,'ativo': True
}

print(funcionario.get('nome'))