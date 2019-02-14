import pygame
import math
ANCHO=640
ALTO=480

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Carga la imagen a una variable
    fondo=pygame.image.load('fondo.png')
    infoFondo=fondo.get_rect()

    print 'Funciona'
    fin=False

    var_x=-2
    var_y=-2

    pos_x=0
    pos_y=0

    pantalla.blit(fondo, [pos_x, pos_y])
    pygame.display.flip()
    reloj=pygame.time.Clock()

    print infoFondo

    while not fin:

        pos=mostrarPos()
        if pos[0]>590 and pos_x>=-1*(infoFondo[2]-ANCHO):
            pantalla.blit(fondo, [pos_x, pos_y])
            pygame.display.flip()
            reloj.tick(10)
            pos_x+=var_x

        if pos[0]<50 and pos_x!=0:
            pantalla.blit(fondo, [pos_x, pos_y])
            pygame.display.flip()
            reloj.tick(10)
            pos_x-=var_x

        if pos[1]>430 and pos_y!=0:
            pantalla.blit(fondo, [pos_x, pos_y])
            pygame.display.flip()
            reloj.tick(10)
            pos_y-=var_y

        if pos[1]<50 and pos_y>=-1*(infoFondo[3]-ALTO):
            pantalla.blit(fondo, [pos_x, pos_y])
            pygame.display.flip()
            reloj.tick(10)
            pos_y+=var_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
