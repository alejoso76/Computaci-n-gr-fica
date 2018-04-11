import pygame
import random

ANCHO=640
ALTO=480

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

def dibujarCircunferencia(pant, punto, a, b, c):
    pygame.draw.circle(pant, [a, b, c], pos, 5, 0)

def pintarPantallaNegra(pant):
    pant.fill([0,0,0])


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()
    print 'Funciona'
    cont=0
    x=100
    pos=[x, 100]
    reloj=pygame.time.Clock()
    fin=False

    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True
        x+=1
        print x
        pos[0]=x
        pantalla.fill([0, 0, 0])
        dibujarCircunferencia(pantalla, pos, 0, 255, 0)
        pygame.display.flip()
        reloj.tick(10)
