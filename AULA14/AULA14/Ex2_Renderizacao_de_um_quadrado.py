# ============================================================
# Exemplo 02 - Renderização de um quadrado utilizando OpenGL Moderno
#
# Neste exemplo utilizamos:
# - GLFW para criação da janela
# - VAO (Vertex Array Object)
# - VBO (Vertex Buffer Object)
# - Vertex Shader
# - Fragment Shader
#
# O quadrado é formado por 2 triângulos.
# ============================================================

# Biblioteca GLFW responsável pela criação da janela
import glfw

# Importa todas as funções do OpenGL
from OpenGL.GL import *

# Biblioteca utilizada para compilação dos shaders
import OpenGL.GL.shaders

# Biblioteca NumPy utilizada para armazenar os dados dos vértices
import numpy as np


# ============================================================
# Variáveis globais
# ============================================================

Window = None
Shader_programm = None
Vao = None

# Tamanho inicial da janela
WIDTH = 800
HEIGHT = 600


# ============================================================
# Callback executado quando a janela é redimensionada
# ============================================================

def redimensionaCallback(window, w, h):

    global WIDTH, HEIGHT

    # Atualiza os valores da largura e altura
    WIDTH = w
    HEIGHT = h


# ============================================================
# Inicialização do OpenGL e criação da janela
# ============================================================

def inicializaOpenGL():

    global Window, WIDTH, HEIGHT

    # Inicializa GLFW
    glfw.init()

    # Criação da janela
    Window = glfw.create_window(
        WIDTH,
        HEIGHT,
        "Exemplo - renderização de um quadrado",
        None,
        None
    )

    # Caso ocorra erro na criação da janela
    if not Window:

        glfw.terminate()
        exit()

    # Define callback de redimensionamento
    glfw.set_window_size_callback(Window, redimensionaCallback)

    # Torna o contexto OpenGL atual
    glfw.make_context_current(Window)

    # Exibe a GPU utilizada
    print("Placa de vídeo: ", OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))

    # Exibe a versão do OpenGL
    print("Versão do OpenGL: ", OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))


# ============================================================
# Inicialização dos objetos gráficos
# ============================================================

def inicializaObjetos():

    global Vao

    # ========================================================
    # VAO - Vertex Array Object
    #
    # Responsável por armazenar a configuração
    # dos atributos dos vértices
    # ========================================================

    # Cria 1 VAO
    Vao = glGenVertexArrays(1)

    # Ativa o VAO
    glBindVertexArray(Vao)


    # ========================================================
    # VBO DOS VÉRTICES
    #
    # O quadrado será formado por 2 triângulos
    # ========================================================

    points = [

        # ----------------------------------------------------
        # Triângulo 1
        # ----------------------------------------------------

         0.5,  0.5, 0.0,   # vértice superior direito
         0.5, -0.5, 0.0,   # vértice inferior direito
        -0.5, -0.5, 0.0,   # vértice inferior esquerdo


        # ----------------------------------------------------
        # Triângulo 2
        # ----------------------------------------------------

        -0.5,  0.5, 0.0,       # vértice superior esquerdo
         0.5,  0.5, 0.0,       # vértice superior direito
        -0.5, -0.5, 0.0        # vértice inferior esquerdo
    ]

    # Converte os dados para float32
    points = np.array(points, dtype=np.float32)

    # Cria o VBO dos vértices
    pvbo = glGenBuffers(1)

    # Ativa o buffer
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)

    # Envia os dados dos vértices para a GPU
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)

    # Habilita o atributo de posição
    glEnableVertexAttribArray(0)

    # Define como os dados serão interpretados
    glVertexAttribPointer(
        0,              # localização do atributo no shader
        3,              # quantidade de componentes (x,y,z)
        GL_FLOAT,       # tipo do dado
        GL_FALSE,       # normalização
        0,              # stride ou distância de um vertice para outro
        None            # offset inicial dos dados no buffer, None = começa no início do buffer
    )


    # ========================================================
    # VBO DAS CORES
    #
    # Cada vértice terá uma cor RGB
    # ========================================================

    cores = [

        # ----------------------------------------------------
        # Triângulo 1
        # ----------------------------------------------------

        1.0, 1.0, 0.5,     # amarelo
        0.0, 1.0, 1.0,     # ciano
        1.0, 0.0, 1.0,     # magenta


        # ----------------------------------------------------
        # Triângulo 2
        # ----------------------------------------------------

        0.0, 1.0, 1.0,     # ciano
        1.0, 1.0, 0.0,     # amarelo
        1.0, 0.0, 1.0      # magenta
    ]

    # Converte para float32
    cores = np.array(cores, dtype=np.float32)

    # Cria o VBO das cores
    cvbo = glGenBuffers(1)

    # Ativa o buffer
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)

    # Envia as cores para a GPU
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)

    # Habilita o atributo de cor
    glEnableVertexAttribArray(1)

    # Define o layout do atributo
    glVertexAttribPointer(
        1,              # localização do atributo no shader
        3,              # RGB
        GL_FLOAT,
        GL_FALSE,
        0,
        None
    )


# ============================================================
# Inicialização dos shaders
# ============================================================

def inicializaShaders():

    global Shader_programm

    # ========================================================
    # VERTEX SHADER
    #
    # Responsável por processar os vértices
    # ========================================================

    vertex_shader = """

        #version 400

        // posição do vértice
        layout(location = 0) in vec3 vertex_posicao;

        // cor do vértice
        layout(location = 1) in vec3 vertex_cores;

        // saída para o fragment shader
        out vec3 cores;

        void main () {

            // envia a cor para o fragment shader
            cores = vertex_cores;

            // define a posição final do vértice
            gl_Position = vec4(vertex_posicao, 1.0);
        }
    """

    # Compila o vertex shader
    vs = OpenGL.GL.shaders.compileShader(
        vertex_shader,
        GL_VERTEX_SHADER
    )

    # Verifica erros de compilação
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):

        infoLog = glGetShaderInfoLog(vs, 512, None)

        print("Erro no vertex shader:\n", infoLog)


    # ========================================================
    # FRAGMENT SHADER
    #
    # Responsável pela cor final dos pixels
    # ========================================================

    fragment_shader = """

        #version 400

        // recebe as cores do vertex shader
        in vec3 cores;

        // saída final de cor
        out vec4 frag_colour;

        void main () {

            // define a cor final do fragmento
            frag_colour = vec4(
                cores.r,
                cores.g,
                cores.b,
                1.0
            );
        }
    """

    # Compila o fragment shader
    fs = OpenGL.GL.shaders.compileShader(
        fragment_shader,
        GL_FRAGMENT_SHADER
    )

    # Verifica erros de compilação
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):

        infoLog = glGetShaderInfoLog(fs, 512, None)

        print("Erro no fragment shader:\n", infoLog)


    # ========================================================
    # SHADER PROGRAM
    #
    # Faz a ligação entre vertex shader e fragment shader
    # ========================================================

    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)

    # Verifica erros de linkagem
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):

        infoLog = glGetProgramInfoLog(
            Shader_programm,
            512,
            None
        )

        print("Erro na linkagem do shader:\n", infoLog)

    # Remove os shaders após a compilação
    glDeleteShader(vs)
    glDeleteShader(fs)


# ============================================================
# Loop principal de renderização
# ============================================================

def inicializaRenderizacao():

    global Window
    global Shader_programm
    global Vao
    global WIDTH
    global HEIGHT

    # Loop principal da aplicação
    while not glfw.window_should_close(Window):

        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)

        # Define a cor de fundo da janela
        glClearColor(0.2, 0.3, 0.3, 1.0)

        # ====================================================
        # VIEWPORT
        #
        # Área da janela onde o OpenGL irá desenhar
        # ====================================================

        glViewport(0, 0, WIDTH, HEIGHT)


        # ====================================================
        # Ativa o shader program
        # ====================================================

        glUseProgram(Shader_programm)


        # ====================================================
        # Ativa o VAO
        # ====================================================

        glBindVertexArray(Vao)


        # ====================================================
        # Desenha os triângulos
        #
        # O quadrado possui:
        # 2 triângulos
        # 6 vértices
        # ====================================================

        glDrawArrays(GL_TRIANGLES, 0, 6)


        # Processa eventos da janela
        glfw.poll_events()

        # Troca os buffers
        glfw.swap_buffers(Window)


        # ====================================================
        # Fecha a janela ao pressionar ESC
        # ====================================================

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):

            glfw.set_window_should_close(Window, True)


    # Finaliza GLFW
    glfw.terminate()


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def main():

    inicializaOpenGL()

    inicializaObjetos()

    inicializaShaders()

    inicializaRenderizacao()


# Executa o programa
if __name__ == "__main__":

    main()
