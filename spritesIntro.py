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
    fondo=pygame.image.load('terrenogen.png')
    infoFondo=fondo.get_rect()
    print infoFondo

    ancho_imagen=infoFondo[2]
    alto_imagen=infoFondo[3]

    print "Ancho = ",ancho_imagen
    print "Alto = ",alto_imagen

    print 'Funciona'
    fin=False

    pos_x=0
    pos_y=0

    alto_corte=alto_imagen/12
    ancho_corte=ancho_imagen/32

    x=28
    y=6
    cuadro=fondo.subsurface(x*ancho_corte,y*alto_corte,32,32)


    pantalla.blit(cuadro, [pos_x, pos_y])
    pygame.display.flip()
    reloj=pygame.time.Clock()


    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
