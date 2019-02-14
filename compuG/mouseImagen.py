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
    nave=pygame.image.load('thor.png')
    infoFondo=fondo.get_rect()
    infoNave=nave.get_rect()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pygame.mouse.set_visible(False)
        pos=mostrarPos()
        pantalla.blit(fondo, [pos_x, pos_y])
        #pantalla.blit(nave, [pos[0]+infoNave[2], pos[1]+infoNave[3]])
        pantalla.blit(nave, [pos[0]-infoNave[2]/2, pos[1]-infoNave[3]/2])
        pygame.display.flip()
