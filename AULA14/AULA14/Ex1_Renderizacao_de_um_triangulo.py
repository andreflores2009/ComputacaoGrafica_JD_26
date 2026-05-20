# Este exemplo apresenta uma aplicação completa de OpenGL, que renderiza um triângulo na tela.
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programm = None
Vao = None
WIDTH = 1000
HEIGHT = 800

#Função callback que é executada sempre que a janela for redimensionada
#Sempre que a tela for redimensionada, salvamos sua nova largura e altura nas variáveis globais acima
def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    #Inicializa GLFW
    glfw.init()

    #Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um triângulo", None, None)
    #Caso não seja possível criar a janela, a GLFW e a aplicação são terminadas
    if not Window:
        glfw.terminate()
        exit()

    #Registramos a função "redimensionaCallback" como sendo a função de redimensionamento
	#Isso significa que a função "redimensionaCallback" será chamada sempre que a janela for redimensionada,
	#seja pelo sistema ou pelo usuário
    glfw.set_window_size_callback(Window, redimensionaCallback)

    #Define o contexto atual do GLFW como sendo a janela criada acima. O contexto define
	#em qual janela o OpenGL irá funcionar, o que é essencial para que o programa funcione
    glfw.make_context_current(Window)

    #Buscamos informações a respeito do hardware (placa de vídeo) e a versão do OpenGL que a mesma da suporte
    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))

def inicializaObjetos():
    global Vao
    # Devido ao fato de que cada objeto que modelarmos possui, geralmente, uma coleção
	# de buffers de informaçõees referentes aos seus vértices (tais como coordenadas dos vértices,
	# coordenadas de texturas, normais, cores, etc), utilizamos um objeto do tipo Vertex Attribute Object (VAO)
	# que "une" e "representa" todos os buffers do objeto em um único identificador.

	# Nós devemos especificar um VAO para cada objeto que estamos modelando.
	# No caso deste exemplo, vamos renderizar somente 1 triângulo, logo, precisamos somente de
	# 1 VAO para representá-lo.

	# Geramos o VAO, definindo um identificador para ele através glGenVertexArrays
    Vao = glGenVertexArrays(1) #gera 1 único VAO
    # Damos um bind no VAO, setando ele como VAO atual e colocando o mesmo no topo da máquina de estados do OpenGL
    glBindVertexArray(Vao)

    # Definição de um VBO para os vértices do triângulo
	# - Primeiramente, definimos em um vetor de float os vértices do triângulo;
	# - Em seguida, criamos uma cópia desses dados na placa gráfica através de uma unidade denominada Vertex Buffer Object (VBO).
	# Para isso, nós geramos primeiramente um buffer vazio, através da função glGenBuffers, e então setamos esse buffer como buffer 
	# atual na máquina de estados do OpenGL através de glBindBuffer,e por fim copiamos os pontos para esse buffer através do glBufferData.
    points = [
        #X    Y    Z
		0.0, 0.5, 0.0, #cima
		0.5, -0.5, 0.0, #direita
		-0.5, -0.5, 0.0 #esquerda
	]

    # Convertemos o array do Python para um array da biblioteca NumPy, pois é o tipo de array que o OpenGL trabalha
    points = np.array(points, dtype=np.float32)

    pvbo = glGenBuffers(1) #cria 1 VBO
    #Vertex Buffer Object (VBO):
    #Propósito: O VBO é usado para armazenar os dados dos vértices.
    #Funcionalidade: Ele armazena os dados do vértice, como posições, cores, normais, etc., em um buffer de memória na GPU.
    #Uso Típico: Carrega os dados do vértice para a GPU usando glBufferData ou glBufferSubData. 
    #O VBO é, então, associado ao VAO usando glBindBuffer para que o VAO saiba de onde obter os dados.

    glBindBuffer(GL_ARRAY_BUFFER, pvbo) #coloca o pvbo no topo da pilha/maquina de estados
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW) #copia os dados do python para dentro do VBO
    # Ativamos o primeiro atributo do VAO (índice 0), que é o atributo referente ao buffer das posições dos vértices.
    glEnableVertexAttribArray(0)
    # E então definimos o layout do buffer de vértices:
	# - o primeiro parâmetro (0) significa que estamos definido o layout do atributo 0 (buffer de vértices)
	# - o segundo parâmetro (3) significa que esse buffer é formado por 3 variáveis (x,y, e z),
	# - o terceiro parâmetro, indica que as variáveis são do tipo float
	# - o quarto parâmetro indica se os valores devem ser normalizados automaticamente ou não, neste exemplo os valores já estão normalizados
    # - o quinto parâmetro é o byte offset entre os atributos, caso tenha sido especificado um único VBO para mais de um tipo de informação
    # - o sexto parâmetro é o offset do primeiro elemento, que no nosso caso, é 0, pois queremos todos os elementos do array
    #   -- Devido a um bug da biblioteca, precisamos passar None ao invés de 0
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # Definição de um VBO para as cores do triângulo. Observe que passamos como parâmetro o valor 1
	# na chamada ao "glEnableVertexAttribArray", pois estamos ativando o segundo atributo deste VAO,
	# que são as cores dos vértices. Além disso, também passamos o parâmetro 1 na chamada ao "glVertexAttribPointer", 
	# pois estamos definindo o layout do segundo atributo.
    cores = [
        #R    G    B
		1.0, 0.0, 0.0, #vermelho
		0.0, 1.0, 0.0, #verde
		0.0, 1.0, 1.0  #azul
	]
    cores = np.array(cores, dtype=np.float32) #converte o array para numpy
    cvbo = glGenBuffers(1) #gera o vbo para as cores
    glBindBuffer(GL_ARRAY_BUFFER, cvbo) # define o VBO das cores como buffer atual
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW) #copia os dados para a memória de vídeo
    glEnableVertexAttribArray(1) #ativa o índice 1 para o vbo das cores
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None) #configura o vbo das cores


def inicializaShaders():
    
    global Shader_programm
    # ========================================================
    # Especificação do Shader_programm
    # ========================================================
    #
    # - O Vertex Shader é responsável por processar cada vértice
    #   do objeto e definir sua posição final na tela
    #
    # - A linha "#version 400" define que estamos utilizando
    #   a versão 4.0 da GLSL
    #
    # - "layout(location = 0)" define que este atributo receberá
    #   os dados da posição enviados pelo Python
    #
    # - "layout(location = 1)" define que este atributo receberá
    #   os dados das cores enviados pelo Python
    #
    # - "in" significa variável de entrada do shader
    #
    # - "vec3" significa vetor com 3 valores:
    #   x,y,z ou r,g,b
    #
    # - "out vec3 cores" envia os dados de cor
    #   para o Fragment Shader
    #
    # - gl_Position define a posição final do vértice
    #
    # - gl_Position deve obrigatoriamente ser um vec4,
    #   por isso adicionamos o valor 1.0 ao final
    # representando a coordenada W que é utilizada para transformações de perspectiva
    # O W é um valor que é utilizado para realizar transformações de perspectiva, ou seja, para simular a profundidade dos objetos na cena.
    # Ele é utilizado para transformar as coordenadas do espaço 3D para o espaço 2D da tela, permitindo que objetos mais distantes
    # pareçam menores do que objetos mais próximos.
    # No caso deste exemplo, como estamos renderizando um triângulo simples sem nenhuma transformação de perspectiva,
    # podemos simplesmente definir o valor de W como 1.0.
    vertex_shader = """
         #version 400

        // atributo posição
        layout(location = 0) in vec3 vertex_posicao;
        // atributo cor
        layout(location = 1) in vec3 vertex_cores;
        // saída para o fragment shader
        out vec3 cores;

        void main () {

            // envia a cor para o fragment shader
            cores = vertex_cores;

            // posição final do vértice
            gl_Position = vec4(vertex_posicao.x,vertex_posicao.y,vertex_posicao.z,1.0);
        }
    """
 
    # Como shaders são programas executados pela GPU,
    # precisamos compilá-los e verificar se não ocorreu nenhum erro
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    #   # - o Fragment Shader é responsável por determinar
    #   a cor final de cada fragmento (pixel) do objeto
    # - a primeira linha especifica a versão da GLSL
    #   que estamos utilizando, no caso, 4.0.0
    #
    # - "in vec3 cores" recebe as cores enviadas
    #   pelo Vertex Shader
    #
    # - a variável frag_colour define a cor final
    #   do fragmento
    #
    # - neste exemplo, utilizamos as cores vindas
    #   dos vértices do objeto
    #
    # - o valor 1.0 representa opacidade total
    #   (sem transparência)
    fragment_shader = """
        #version 400
        in vec3 cores;
		out vec4 frag_colour;
		void main () {
		    frag_colour = vec4 (cores.r, cores.g, cores.b, 1.0);
		}
    """
    # Do mesmo modo que o vertex shader, precisamos compilar o fragment shader e verificar se não houve nenhum erro de compilação
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
	# Após compilarmos os shaders, precisamos combiná-los em um único programa, denominado GPU Shader Program.
	# Para isso, chamamos a função compileProgram passando os dois shaders que irão formar o nosso shader program
    # e testamos se não houve nenhum erro de linkagem
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao, WIDTH, HEIGHT

	# O triangulo é redesenhado o tempo todo, dentro de um laço de repetição
	# que é executado enquanto a janela não for fechada
    while not glfw.window_should_close(Window):
        # Limpamos o buffer de cores da tela
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0) #cor de fundo

        # Redefinimos o tamanho da viewport para o tamanho atual da janela, a cada frame, de modo que
		# o desenho se ajuste de acordo com o tamanho da tela
        glViewport(0, 0, WIDTH, HEIGHT)

        # Especificamos qual Shader Programm vamos utilizar
        glUseProgram(Shader_programm)

        # Setamos o objeto Vao como sendo o VAO atual na máquina de estados do OpenGL
        glBindVertexArray(Vao)

        # Desenhamos o triângulo especificado no vao
        glDrawArrays(GL_TRIANGLES, 0, 3) #a partir do primeiro vértice, desenha 3 vértices

        # Atualizamos outros eventos, tais como entradas pelo teclado, mouse, etc, caso ocorram
        glfw.poll_events()

        # Renderizamos na tela tudo aquilo que foi desenhado logo acima
        glfw.swap_buffers(Window)

        # Verificamos se a tecla ESC foi pressionada. Caso positivo, definimos que a tela deve ser
		# fechada na próxima volta do laço.
		# Para testar se outras teclas foram pressionadas, verifique o seguinte link:
		# http://www.glfw.org/docs/latest/group__input.html
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)
    
    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL() #configuração do ambiente (janelas, bibliotecas, etc.)
    inicializaObjetos() #modelagem dos objetos e envio dos mesmos para a placa de vídeo   
    inicializaShaders() #programação dos shaders, especificando como esses objetos devem ser renderizados
    inicializaRenderizacao() #onde é feita a renderização na tela dos objetos modelados

if __name__ == "__main__":
    main()
