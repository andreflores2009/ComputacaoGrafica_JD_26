"""
Exemplo 10 - Dicionários
Mostra como usar dicionários em Python para armazenar pares chave-valor.
"""
# cria um dicionário com informações de um aluno
aluno = {
    "nome": "João",
    "idade": 18,
    "curso": "Computação"
}

# imprime o dicionário completo
print("Dados do aluno:", aluno)
# imprime o valor associado à chave "nome"
print("Nome:", aluno["nome"])
# imprime o valor associado à chave "curso"
print("Curso:", aluno["curso"])

# altera o valor da chave "idade"
aluno["idade"] = 19
print("Idade atualizada:", aluno["idade"])


