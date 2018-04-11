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
    fin=False
    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN and cont==0:
                pantalla.fill([0, 0, 0])
                pos=mostrarPos()
                a=random.randint(0, 255)
                b=random.randint(0, 255)
                c=random.randint(0, 255)
                print pos
                dibujarCircunferencia(pantalla, pos, a, b, c)
                pygame.display.flip()


            if event.type == pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:
                    if(pos[0]>=0):
                        print 'Left'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[pos[0]-5, pos[1]]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()
                    else:
                        print 'Left'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[ANCHO, pos[1]]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()

                if event.key==pygame.K_RIGHT:
                    if(pos[0]<ANCHO):
                        print 'Right'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[pos[0]+5, pos[1]]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()
                    else:
                        print 'Right'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[0, pos[1]]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()


                if event.key==pygame.K_UP:
                    if(pos[1]>=0):
                        print 'Up'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[pos[0], pos[1]-5]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()
                    else:
                        print 'Up'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[pos[0], ALTO]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()

                if event.key==pygame.K_DOWN:
                    if(pos[1]<ALTO):
                        print 'Down'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[pos[0], pos[1]+5]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()
                    else:
                        print 'Down'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        pos=[pos[0], 0]
                        print pos
                        dibujarCircunferencia(pantalla, pos, a, b, c)
                        pygame.display.flip()
