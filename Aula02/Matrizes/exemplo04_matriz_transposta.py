
# Importa a biblioteca NumPy para facilitar a manipulação de matrizes
import numpy as np

# Define a matriz A com a nova entrada
A = np.array([[2, 3, 8],
              [6, 0, 4],
              [1, 5, 7]])

# Exibe a matriz original
print("Matriz A:")
print(A)

# Obtém as dimensões da matriz
linhas, colunas = A.shape

# Inicializa a matriz transposta com zeros na mesma dimensão (tamanho) de A
transposta = np.zeros((linhas, colunas), dtype=int)

# Calcula a transposta manualmente
for i in range(linhas):
    for j in range(colunas):
        transposta[j][i] = A[i][j]  # Troca linhas por colunas

# Exibe a matriz transposta
print("\nMatriz Transposta de A:")
print(transposta)
