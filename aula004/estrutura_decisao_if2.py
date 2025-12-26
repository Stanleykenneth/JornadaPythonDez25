nota = 4

# Maoir ou igal 3 9 = "Excelente"
# Acima de 7 = "Aprovado"
# Acima de 5 = "Recuperação"
# Acima de 3 = "Reprovado"

"""
if  nota >= 9:
    print('Excelente')
else: 
    # if aninhado
    if nota >= 7:
        print('Aprovado')
    else:
       if nota >= 5:
          print('Recuperação')

       else:
          print('Reprovado')
"""

if nota >= 9:
    print('Excelente')
elif nota >=7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')            

