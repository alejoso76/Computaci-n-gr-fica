'''
A. -Dar click en la pantalla
-Crear 4 puntos
-Cada punto se debe mover indefinidamente en direccion cardinal

    N
  O + E
    S
4 puntos en el mismo lugar, cada uno se debe mover en una direccion cardinal
'''
'''
            #Left
            pos[0]-=x/100

            #Right
            pos[0]+=x/100

            #Up
            pos[1]-=x/100

            #Down
            pos[1]+=x/100
'''

import pygame
import random

ANCHO=640
ALTO=480

ROJO=[255, 0, 0]
VERDE=[0, 255, 0]
AZUL=[0, 0, 255]
MORADO=[255, 0, 255]

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

def dibujarCircunferencia(pant, punto):
    pygame.draw.circle(pant, [0, 255, 0], pos, 5, 0)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()

    print 'Funciona'
    cont=0
    x=0
    '''
    pos=[0,0]
    pos1=[0,0]
    pos2=[0,0]
    pos3=[0,0]
    pos4=[0,0]
    '''
    reloj=pygame.time.Clock()

    fin=False

    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and cont==0:

                pos=mostrarPos()

                pos1=pos
                pos2=pos
                pos3=pos
                pos4=pos




                dibujarCircunferencia(pantalla, pos1)
                dibujarCircunferencia(pantalla, pos2)
                dibujarCircunferencia(pantalla, pos3)
                dibujarCircunferencia(pantalla, pos4)

                pygame.display.flip()
                print 'Dibuja'
                cont+=1

            if event.type == pygame.QUIT:
                fin=True

            if cont > 0:
                x+=1
                print x

                pos1= [pos1[0]-x/100, pos1[1]]
                pos2= [pos2[0]+x/100, pos2[1]]
                pos3= [pos3[0], pos3[1]-x/100]
                pos4= [pos4[0], pos4[1]+x/100]

                print pos1, pos2, pos3, pos4

                pantalla.fill([0, 0, 0])
                pygame.display.flip()
                '''
                dibujarCircunferencia(pantalla, pos1)
                dibujarCircunferencia(pantalla, pos2)
                dibujarCircunferencia(pantalla, pos3)
                dibujarCircunferencia(pantalla, pos4)
                '''
                pygame.draw.circle(pantalla, [0, 255, 0], pos1, 5, 0)
                pygame.draw.circle(pantalla, [0, 255, 0], pos2, 5, 0)
                pygame.draw.circle(pantalla, [0, 255, 0], pos3, 5, 0)
                pygame.draw.circle(pantalla, [0, 255, 0], pos4, 5, 0)


                pygame.display.flip()

                reloj.tick(10)
