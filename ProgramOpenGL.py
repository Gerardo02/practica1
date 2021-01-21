from OpenGL.GL import *
from glew_wish import *
import glfw


def main():
    if not glfw.init():
        return
    #crea la ventana
    #independientemente del Sistema operativo que usemos
    window = glfw.create_window(800, 600, "La ventanta", None, None)


    #configuramos OPENGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    
    #establecemos eel contexto
    glfw.make_context_current(window)

    #activamos la validacion de funciones modernas de OpenGL
    glewExperimental = True

    #inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar glew")
        return

    #Obtenemos versions de OpenGL y Shaders
    version = glGetString(GL_VERSION)

    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)
    red = 0
    green = 0
    blue = 0
    flag1 = 0
    flag2 = 0
    flag3 = 0
    while not glfw.window_should_close(window):
        
        #Establece region de dibujo
        glViewport(0, 0, 800, 600)
        #Establece region de borrado
        glClearColor(red, green, blue, 1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if red < 1:
            red += 0.002
            flag1 += 1
        elif green < 1:
            green += 0.002
            flag2 += 1
        elif blue < 1:
            blue += 0.002
            flag3 += 1
            
        
        if flag1 == 500 & flag2 == 500 & flag3 == 500:
            red = 0
            green = 0
            blue = 0
            flag1 = 0
            flag2 = 0
            flag3 = 0
        

        

        
        
        #Dibujar
        
        #Preguntar si ubo entradas de perifericos
        #(Teclado, mouse, gamepad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)
        

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inicio de glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()









