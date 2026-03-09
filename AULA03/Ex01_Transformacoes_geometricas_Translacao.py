import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a translação dos pontos
def translacao(pontos, Tx, Ty):
    pontos_transladados = []
    for ponto in pontos:
        x_u = ponto[0] + Tx
        y_u = ponto[1] + Ty
        pontos_transladados.append((x_u, y_u))
    return pontos_transladados

# Pontos originais
p1 = (0, 0)
p2 = (2, 2)

# Vetor de translação
Tx = 3
Ty = 2

# Calcular a translação dos pontos
pontos_transladados = translacao([p1, p2], Tx, Ty)

# Imprimir os pontos transladados
print("Pontos transladados:")
for ponto in pontos_transladados:
    print(ponto)

# Plotar os pontos originais e os pontos transladados
#plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'bo-', label='Pontos originais')

# Plotar os pontos transladados da mesma forma
# Pegando o X do primeiro [0][0] e o X do segundo [1][0]
#lista_x = [ pontos_transladados[0][0], pontos_transladados[1][0] ]
# Pegando o Y do primeiro [0][1] e o Y do segundo [1][1]
#lista_y = [ pontos_transladados[0][1], pontos_transladados[1][1] ]
#plt.plot(lista_x, lista_y, 'ro-', label='Pontos transladados')

# Plotar os PONTOS ORIGINAIS
plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'bo-', label='Pontos originais')

# Plotar os PONTOS TRANSLADADOS
plt.plot([ponto[0] for ponto in pontos_transladados], [ponto[1] for ponto in pontos_transladados], 'ro-', label='Pontos transladados')
#[ponto[0] for ponto in pontos_transladados]:
#Isso é uma compreensão de lista, uma construção Python que permite criar listas de maneira mais compacta.
#O que está entre os colchetes é uma expressão que define como cada elemento da lista será construído.
#ponto[0] é a expressão usada para cada elemento da lista. Aqui, 'ponto' representa cada elemento da lista 'pontos_transladados',
#que são as coordenadas dos pontos transladados.
#ponto[0] extrai o primeiro elemento de cada tupla dentro da lista pontos_transladados, que corresponde à coordenada x do ponto.
#Então, [ponto[0] for ponto in pontos_transladados] cria uma lista contendo apenas as coordenadas x dos pontos transladados.
#Essa lista é usada para definir os valores do eixo x no gráfico.
'''
Imagine que seus pontos_transladados sejam: [(-3, -2), (-1, 0)].
O comando plt.plot do Matplotlib é um pouco exigente: ele não aceita uma lista de pontos agrupados.
Ele quer uma lista só com todos os Xs e depois outra lista só com todos os Ys.
A mágica que acontece ali é:
[ponto[0] for ponto in pontos_transladados]:
O Python entra na lista, pega o X do primeiro ponto, depois o X do segundo ponto...
Resultado: [-3, -1] (Uma lista só de coordenadas X).
[ponto[1] for ponto in pontos_transladados]:
O Python entra na lista, pega o Y do primeiro ponto, depois o Y do segundo ponto...
Resultado: [-2, 0] (Uma lista só de coordenadas Y).'''


#'bo-' especifica o estilo do gráfico: b para azul (blue), 'o' para marcador de círculo e '-' para linha contínua.
#'ro-':
#Isso define o estilo do gráfico para os pontos transladados. Aqui, 'r' indica que os pontos serão vermelhos,
# 'o' especifica que os marcadores serão círculos e '-' indica que uma linha contínua conectará os pontos.

# Definir os limites dos eixos
plt.xlim(-5, 10)  # Define o limite do eixo X de 0 a 10
plt.ylim(-5, 10)  # Define o limite do eixo Y de 0 a 10


# Configurações do gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Translação de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()
