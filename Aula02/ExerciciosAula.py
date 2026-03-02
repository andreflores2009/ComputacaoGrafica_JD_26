print("Ola")

import math

#função que calcula o tamanho ou magnitude de um vetor
def calculaTamanho(x, y, z):
    tam = math.sqrt(x*x + y*y + z*z)
    return tam

#Faz a leitura das variáveis do primeiro vetor
print("EXERCÍCIO 01 - COMPUTAÇÃO GRÁFICA") #print mostra uma mensagem na tela
print("\n DIGITE OS VALORES DO VETOR") #print mostra uma mensagem na tela
x = float(input("Digite o valor de x: ")) #input é para ler pelo teclado
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))
print("----------------------\n")
print("\n Valor de X, Y e Z lidos",x,y,z) #print mostra uma mensagem na tela

while True:
    print("1. Calcular o tamanho do vetor") #print mostra uma mensagem na tela
    print("2. Normalizar o vetor") #quando a magnitude ou tamanho é igual a 1
    print("3. Adicionar outro vetor")
    print("4. Subtrair outro vetor")
    print("5. Multiplicar por escalar")
    print("6. Dividir por escalar")
    print("7. Produto escalar")
    print("8. Terminar")

    op = int(input("Digite a opção: "))

    # a)
    if op == 1:
        #calcula o tamanho do vetor
        tam = calculaTamanho(x,y,z)
        print("\n O tamanho é igual a", round(tam, 2))
        print("----------------------\n")


    # b)
    elif op == 2:
        #calcula o tamanho do vetor
        tam = calculaTamanho(x,y,z)
        #normaliza o vetor
        xn = x/tam
        yn = y/tam
        zn = z/tam
        print("\n O vetor normalizado é", round(xn, 2), round(yn, 2), round(zn, 2))
        #print("\n O vetor normalizado é {:.2f} {:.2f} {:.2f}".format(xn, yn, zn) )
        print("----------------------\n")

    # c)
    elif op == 3:
        print("\n DIGITE OS VALORES DO VETOR 02") #print mostra uma mensagem na tela
        x2 = float(input("Digite o valor de x2: "))
        y2 = float(input("Digite o valor de y2: "))
        z2 = float(input("Digite o valor de z2: "))
        print("\n A soma dos vetores é ",x+x2,",",y+y2,",",z+z2)
        print("----------------------\n")    

    # c)
    elif op == 4:
        print("\n DIGITE OS VALORES DO VETOR 02") #print mostra uma mensagem na tela
        x2 = float(input("Digite o valor de x2: "))
        y2 = float(input("Digite o valor de y2: "))
        z2 = float(input("Digite o valor de z2: "))
        print("\n A soma dos vetores é ",x-x2,",",y-y2,",",z-z2)
        print("----------------------\n") 


    # e)
    elif op == 5:
        escalar = float(input("Digite o escalar: "))
        print("\n A multiplicação pelo escalar é ",x*escalar,",",y*escalar,",",z*escalar)
        print("----------------------\n")


    # f)
    elif op == 6:
        escalar = float(input("Digite o escalar: "))
        print("\n A divisão pelo escalar é", round(x/escalar, 2), ",", round(y/escalar, 2), ",", round(z/escalar, 2))
        print("----------------------\n")

    # g)
    elif op == 7:
        print("\n DIGITE OS VALORES DO VETOR 02") #print mostra uma mensagem na tela
        x2 = float(input("Digite o valor de x2: "))
        y2 = float(input("Digite o valor de y2: "))
        z2 = float(input("Digite o valor de z2: "))
        produtoEscalar = x*x2 + y*y2 + z*z2
        print("\n Produto escalar = ",produtoEscalar)
        print("----------------------\n")
      
    elif op == 8:
        break #sai do laço

    else:
        print("Opção inválida!")
