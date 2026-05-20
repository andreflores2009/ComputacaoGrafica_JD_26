# ============================================================
# Exemplo 03 - Invertendo um triângulo na vertical
#
# Objetivo:
# Neste exemplo iremos renderizar 2 triângulos utilizando
# o mesmo VAO e os mesmos VBOs.
#
# O segundo triângulo será invertido verticalmente,
# demonstrando como alterar vértices no eixo Y.
#
# Conceitos utilizados:
# - GLFW
# - VAO (Vertex Array Object)
# - VBO (Vertex Buffer Object)
# - Vertex Shader
# - Fragment Shader
# - glDrawArrays
# ============================================================

# Biblioteca GLFW responsável pela criação da janela
import glfw

# Importa todas as funções do OpenGL
from OpenGL.GL import *

# Biblioteca para compilação dos shaders
import OpenGL.GL.shaders

# Biblioteca NumPy para trabalhar com arrays
import numpy as np


# ============================================================
# Variáveis globais
# ============================================================

Window = None
Shader_programm = None
Vao = None

WIDTH = 1000
HEIGHT = 800


# ============================================================
# Função callback executada ao redimensionar a janela
# ============================================================

def redimensionaCallback(window, w, h):

    global WIDTH, HEIGHT

    WIDTH = w
    HEIGHT = h


# ============================================================
# Inicialização do OpenGL
# ============================================================

def inicializaOpenGL():

    global Window, WIDTH, HEIGHT

    # Inicializa GLFW
    glfw.init()

    # Criação da janela
    Window = glfw.create_window(
        WIDTH,
        HEIGHT,
        "Exemplo 03 - Inverter triangulo",
        None,
        None
    )

    # Caso a janela não possa ser criada
    if not Window:

        glfw.terminate()
        exit()

    # Registra callback de redimensionamento
    glfw.set_window_size_callback(
        Window,
        redimensionaCallback
    )

    # Define o contexto OpenGL atual
    glfw.make_context_current(Window)

    # Exibe informações da GPU
    print(
        "Placa de vídeo: ",
        OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER)
    )

    # Exibe versão do OpenGL
    print(
        "Versão do OpenGL: ",
        OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION)
    )


# ============================================================
# Inicialização dos objetos
# ============================================================

def inicializaObjetos():

    global Vao

    # ========================================================
    # VAO
    #
    # O VAO será responsável por armazenar
    # a configuração dos atributos dos vértices
    # ========================================================

    Vao = glGenVertexArrays(1)

    glBindVertexArray(Vao)


    # ========================================================
    # VBO DOS VÉRTICES
    # ========================================================
    #
    # Neste exemplo teremos:
    #
    # Triângulo 1 = normal
    # Triângulo 2 = invertido verticalmente
    #
    # Para inverter um objeto verticalmente,
    # alteramos os sinais do eixo Y
    # ========================================================

    points = [

        # ----------------------------------------------------
        # TRIÂNGULO 1
        # ----------------------------------------------------

        # X     Y     Z

        0.0,  0.5, 0.0,   # vértice superior
        0.5, -0.5, 0.0,   # vértice inferior direito
       -0.5, -0.5, 0.0,   # vértice inferior esquerdo


        # ----------------------------------------------------
        # TRIÂNGULO 2 (invertido verticalmente)
        # ----------------------------------------------------
        #
        # Observe que agora:
        #
        # 0.5 virou -0.5
        # -0.5 virou 0.5
        #
        # Isso faz o triângulo ficar "de cabeça para baixo"
        # ====================================================

        0.6, -0.5, 0.0,   # vértice inferior
        1.0,  0.5, 0.0,   # vértice superior direito
        0.2,  0.5, 0.0    # vértice superior esquerdo
    ]


    # Converte o array Python para NumPy
    points = np.array(points, dtype=np.float32)


    # ========================================================
    # Criação do VBO dos vértices
    # ========================================================

    pvbo = glGenBuffers(1)

    # Define o VBO atual
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)

    # Copia os vértices para a GPU
    glBufferData(
        GL_ARRAY_BUFFER,
        points,
        GL_STATIC_DRAW
    )

    # Ativa o atributo 0 do shader
    glEnableVertexAttribArray(0)

    # Define o layout do atributo posição
    glVertexAttribPointer(

        0,              # atributo 0 do shader

        3,              # x,y,z

        GL_FLOAT,       # tipo float

        GL_FALSE,       # sem normalização

        0,              # stride

        None            # offset inicial
    )


    # ========================================================
    # VBO DAS CORES
    # ========================================================

    cores = [

        # ----------------------------------------------------
        # TRIÂNGULO 1
        # ----------------------------------------------------

        1.0, 0.0, 0.0,   # vermelho
        0.0, 1.0, 0.0,   # verde
        0.0, 0.0, 1.0,   # azul


        # ----------------------------------------------------
        # TRIÂNGULO 2
        # ----------------------------------------------------

        1.0, 1.0, 0.0,   # amarelo
        1.0, 0.0, 1.0,   # magenta
        0.0, 1.0, 1.0    # ciano
    ]

    cores = np.array(cores, dtype=np.float32)


    # ========================================================
    # Criação do VBO das cores
    # ========================================================

    cvbo = glGenBuffers(1)

    # Define o VBO das cores como atual
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)

    # Copia as cores para a GPU
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW )

    # Ativa o atributo 1 do shader
    glEnableVertexAttribArray(1)

    # Define layout das cores
    glVertexAttribPointer(

        1,              # atributo 1 do shader

        3,              # r,g,b

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
    # ========================================================

    vertex_shader = """
        #version 400
        // posição
        layout(location = 0) in vec3 vertex_posicao;
        // cor
        layout(location = 1) in vec3 vertex_cores;

        // saída para o fragment shader
        out vec3 cores;

        void main () {
            // envia as cores
            cores = vertex_cores;
            // posição final do vértice
            gl_Position = vec4(
                vertex_posicao.x,
                vertex_posicao.y,
                vertex_posicao.z,
                1.0
            );
        }
    """

    # Compila o vertex shader
    vs = OpenGL.GL.shaders.compileShader(
        vertex_shader,
        GL_VERTEX_SHADER
    )

    # Verifica erros de compilação
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):

        infoLog = glGetShaderInfoLog(
            vs,
            512,
            None
        )

        print(
            "Erro no vertex shader:\n",
            infoLog
        )


    # ========================================================
    # FRAGMENT SHADER
    # ========================================================
    fragment_shader = """
        #version 400
        // recebe cores do vertex shader
        in vec3 cores;
        // saída final
        out vec4 frag_colour;

        void main () {
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

    # Verifica erros
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):

        infoLog = glGetShaderInfoLog(
            fs,
            512,
            None
        )

        print(
            "Erro no fragment shader:\n",
            infoLog
        )


    # ========================================================
    # SHADER PROGRAM
    # ========================================================
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs,fs)

    # Verifica erros de linkagem
    if not glGetProgramiv(
        Shader_programm,
        GL_LINK_STATUS
    ):

        infoLog = glGetProgramInfoLog(
            Shader_programm,
            512,
            None
        )

        print(
            "Erro na linkagem do shader:\n",
            infoLog
        )


    # Remove shaders após compilação
    glDeleteShader(vs)
    glDeleteShader(fs)


# ============================================================
# Renderização
# ============================================================
def inicializaRenderizacao():

    global Window
    global Shader_programm
    global Vao
    global WIDTH
    global HEIGHT

    # Loop principal
    while not glfw.window_should_close(Window):

        # ====================================================
        # Limpa a tela
        # ====================================================
        glClear(GL_COLOR_BUFFER_BIT)

        # ====================================================
        # Cor de fundo
        # ====================================================
        glClearColor(0.2, 0.3, 0.3,1.0)

        # ====================================================
        # Viewport
        # ====================================================
        glViewport(0, 0, WIDTH,HEIGHT)

        # ====================================================
        # Ativa o shader program
        # ====================================================
        glUseProgram(Shader_programm)

        # ====================================================
        # Ativa o VAO
        # ====================================================
        glBindVertexArray(Vao)

        # ====================================================
        # Desenha os 2 triângulos
        # ====================================================
        #
        # Agora temos:
        #
        # 2 triângulos
        # 6 vértices
        # ====================================================
        glDrawArrays(GL_TRIANGLES, 0, 6)


        # Atualiza eventos
        glfw.poll_events()

        # Troca os buffers
        glfw.swap_buffers(Window)

        # ====================================================
        # Fecha a janela ao pressionar ESC
        # ====================================================

        if (
            glfw.PRESS ==
            glfw.get_key(Window, glfw.KEY_ESCAPE)
        ):

            glfw.set_window_should_close(
                Window,
                True
            )


    # Finaliza GLFW
    glfw.terminate()


# ============================================================
# Função principal
# ============================================================

def main():

    # Inicialização do OpenGL
    inicializaOpenGL()

    # Criação dos objetos
    inicializaObjetos()

    # Inicialização dos shaders
    inicializaShaders()

    # Renderização
    inicializaRenderizacao()


# Executa o programa
if __name__ == "__main__":

    main()
