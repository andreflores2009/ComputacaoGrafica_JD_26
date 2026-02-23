"""
Exemplo 5 - Estrutura Condicional (if/else)
O programa avalia uma nota e decide se o aluno está aprovado, em recuperação ou reprovado.
"""
# lê a nota do aluno e converte para float
nota = float(input("Digite a nota do aluno: "))

# se a nota for maior ou igual a 7, aluno aprovado
if nota >= 7:
    print("Aprovado")
# se a nota for maior ou igual a 5, mas menor que 7, recuperação
elif nota >= 5:
    print("Recuperação")
# caso contrário, reprovado
else:
    print("Reprovado")
