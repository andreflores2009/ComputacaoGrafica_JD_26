# Importa a biblioteca NumPy para facilitar a manipulação de matrizes
import numpy as np

# Define a matriz A
A = np.array([[1, 3, 2],
              [4, 7, 6]])

# Define a matriz B
B = np.array([[2, 8],
              [3, 1],
              [5, 9]])

# Exibe as matrizes iniciais
print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

# Multiplica as matrizes A e B usando a função dot do NumPy
resultado = np.dot(A, B)

# Exibe o resultado da multiplicação das matrizes
print("\nResultado da multiplicacao de A e B:")
print(resultado)
