import matplotlib.pyplot as plt  # Importa a biblioteca para plotar gráficos
import numpy as np  # Importa a biblioteca NumPy para operações matemáticas

# Função para calcular a translação dos pontos
def translacao(pontos, Tx, Ty):
    pontos_transladados = []  # Lista para armazenar os pontos transladados
    for ponto in pontos:  # Percorre cada ponto na lista
        x_u = ponto[0] + Tx  # Soma o deslocamento Tx à coordenada x
        y_u = ponto[1] + Ty  # Soma o deslocamento Ty à coordenada y
        pontos_transladados.append((x_u, y_u))  # Adiciona o ponto transladado à lista
    return pontos_transladados  # Retorna a lista de pontos transladados

# Define os pontos originais
p1 = (6, 8)  # Primeiro ponto
p2 = (4, 5)  # Segundo ponto
p3 = (8, 5)  # Terceiro ponto

# Define o vetor de translação
Tx = 3  # Translação no eixo X
Ty = -4  # Translação no eixo Y

# Calcula a translação dos pontos
pontos_transladados = translacao([p1, p2, p3], Tx, Ty)

# Imprimir os pontos transladados
print("Pontos transladados:")
for ponto in pontos_transladados:
    print(ponto)

# Imprime os pontos transladados para verificação
#print("Pontos transladados:")
#for i, p in enumerate(pontos_transladados, start=1):  # Percorre os pontos transladados
#    print(f"P{i}: {p}")  # Exibe o ponto transladado no console

#OBS repetimos sempre o primeiro ponto para fechar a linha do triangulo na hora de plotar o gráfico
# Plotar os pontos originais e os pontos transladados como triângulos
plt.plot([p1[0], p2[0], p3[0], p1[0]], [p1[1], p2[1], p3[1], p1[1]], 'bo-', label='Pontos originais')  # Plota os pontos originais como triângulo

# 1. Pegamos os pontos da lista que a função retornou
# (Lembrando que a lista pontos_transladados tem os índices 0, 1 e 2) tem 3 pontos (p1,p2,p3) cada um com x,y
pt1 = pontos_transladados[0] #x,y
pt2 = pontos_transladados[1] #x,y
pt3 = pontos_transladados[2] #x,y

# 2. Agora o plot dos transladados
# [X1, X2, X3, X1], [Y1, Y2, Y3, Y1]
plt.plot([pt1[0], pt2[0], pt3[0], pt1[0]],     #OBS repetimos sempre o primeiro ponto para fechar a linha do triangulo na hora de plotar o gráfico
         [pt1[1], pt2[1], pt3[1], pt1[1]],
         'ro-', label='Pontos transladados')


'''
#outra forma
# 1. Criamos uma lista temporária que já contém o primeiro ponto repetido no final
# Isso garante que volte para o início e feche o triângulo
pontos_fechados = pontos_transladados + [pontos_transladados[0]]

# 2. Agora o plot usa o 'for' para extrair os Xs e os Ys automaticamente
plt.plot([p[0] for p in pontos_fechados],  # "Pega o X de cada ponto p"
         [p[1] for p in pontos_fechados],  # "Pega o Y de cada ponto p"
         'ro-', label='Pontos transladados')
'''


# O enumerate() é uma função que 'numera' os itens de uma lista enquanto você os percorre.
# Ele retorna dois valores a cada volta do laço:
# 'i' (o índice/contador) e 'p' (o conteúdo do ponto, como x e y).
# O start=1 indica que a contagem do 'i' deve começar em 1, em vez do padrão 0 (zero).

# Adicionar rótulos aos pontos originais
for i, p in enumerate([p1, p2, p3], start=1):
    plt.text(p[0], p[1], f' P{i}', fontsize=12, verticalalignment='bottom', horizontalalignment='right')  # Exibe rótulo dos pontos originais
    #p[0]=x e p[1]=y obtidos da tupla

# Adicionar rótulos aos pontos transladados
for i, p in enumerate(pontos_transladados, start=1):
    plt.text(p[0], p[1], f' P{i}`', fontsize=12, verticalalignment='bottom', horizontalalignment='right')  # Exibe rótulo dos pontos transladados
    #p[0]=x e p[1]=y obtidos da tupla

# Configurações do gráfico
plt.xlabel('X')  # Define o rótulo do eixo X
plt.ylabel('Y')  # Define o rótulo do eixo Y
plt.title('Translação de pontos no plano cartesiano')  # Define o título do gráfico
plt.grid(True)  # Exibe a grade no gráfico
plt.legend()  # Adiciona a legenda

# Definir os limites dos eixos
plt.xlim(0, 15)  # Define o limite do eixo X de 0 a 15
plt.ylim(0, 15)  # Define o limite do eixo Y de 0 a 15

# Definir os ticks nos eixos X e Y
plt.xticks(np.arange(0, 16, 1))  # Define os intervalos do eixo X de 1 em 1
plt.yticks(np.arange(0, 16, 1))  # Define os intervalos do eixo Y de 1 em 1

# Mostrar o gráfico
plt.show()  # Exibe o gráfico
