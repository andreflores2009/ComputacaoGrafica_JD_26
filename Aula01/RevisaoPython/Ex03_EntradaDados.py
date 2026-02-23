"""
Exemplo 3 - Entrada de Dados
Este programa mostra como ler informações digitadas pelo usuário usando input().
"""
# lê o nome do usuário como string
nome = input("Digite seu nome: ")
# lê a idade do usuário como string e converte para inteiro
idade = int(input("Digite sua idade: "))

# exibe o resultado usando f-string (formatação de texto)
print(f"Olá, {nome}! Você tem {idade} anos.")
