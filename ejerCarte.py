import pygame
import random

ANCHO=640
ALTO=480

def dibujarPlano(o, pantalla):
    pygame.draw.line(pantalla, [0, 255, 0], [o[0], 0], [o[0], 480] )
    pygame.draw.line(pantalla, [0, 255, 0], [0, o[1]], [640, o[1]] )

def calcularPosPantalla(o, p):
    return o[0]+p[0], o[1]-p[1]

def sumaVectores(v1, v2):
    return v1[0]+v2[0], v1[1]+v2[1]

def multiplicarVPorEscalar(v, e):
    return v[0]*e, v[1]*e

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

def calcularPosPlano(o, pos):
    return pos[0]-o[0], -1*(pos[1]-o[1])

def calcularVectorCanonico(v1, v2):
    return v2[0] - v1[0], v2[1] - v1[1]


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana

    o=[320,240]
    dibujarPlano(o, pantalla)
    pygame.display.flip()
    print 'Funciona'
    cont=0
    lista=[]

    fin=False
    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=mostrarPos()
                cont+=1

            if cont==1:
                c1=pos
                '''
                print 'Primer punto'
                print c1
                '''
                c1p=calcularPosPlano(o, c1)

            if cont==2:
                c2=pos
                '''
                print 'Segundo punto'
                print c2
                '''
                c2p=calcularPosPlano(o, c2)

                vc=calcularVectorCanonico(c1p, c2p)
                vc=calcularPosPantalla(o, vc)

                a=random.randint(0, 255)
                b=random.randint(0, 255)
                c=random.randint(0, 255)

                pygame.draw.line(pantalla, [a, b, c], [c1[0], c1[1]], [c2[0], c2[1]] )
                pygame.draw.line(pantalla, [a, b, c], [o[0], o[1]], [vc[0], vc[1]] )
                pygame.display.flip()

                del lista[:]
                cont=0
