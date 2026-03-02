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

# Obtém as dimensões das matrizes (nomematriz.shape)
linhas_A, colunas_A = A.shape
linhas_B, colunas_B = B.shape

# Exibe as dimensões das matrizes
print(f"\nDimensões de A: {linhas_A}x{colunas_A}")
print(f"Dimensões de B: {linhas_B}x{colunas_B}")
print("\n ")

# Verifica se as matrizes podem ser multiplicadas
if colunas_A != linhas_B:
    print("\nErro: O número de colunas de A deve ser igual ao número de linhas de B para multiplicação.")
else:
    # Inicializa a matriz resultado com zeros (como inteiros para evitar pontos decimais) numpy por padrão inicializa variáveis como float
    resultado = np.zeros((linhas_A, colunas_B), dtype=int)
    #print(resultado)

    
    # Multiplica as matrizes A e B manualmente com loops aninhados












