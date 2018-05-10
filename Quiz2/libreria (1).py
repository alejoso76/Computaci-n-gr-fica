#Libreria funciones
import pygame
ANCHO=600
ALTO=480

def dibujarPlano(o, pantalla):
    pygame.draw.line(pantalla, [0, 255, 0], [o[0], 0], [o[0], 480] )
    pygame.draw.line(pantalla, [0, 255, 0], [0, o[1]], [640, o[1]] )

def dibujarTriangulo(a, b, c, plano):
    '''
    pygame.draw.line(plano, [0, 255, 0], [a[0], a[1]], [b[0], b[1]] )
    pygame.draw.line(plano, [0, 255, 0], [b[0], b[1]], [c[0], c[1]] )
    pygame.draw.line(plano, [0, 255, 0], [c[0], c[1]], [a[0], a[1]] )
    '''
    pygame.draw.polygon(plano, [0, 255, 0], [a,b,c])
    pygame.display.flip()
    return a, b, c

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

def escalarPunto (a, factor):
    x=a[0]*factor
    y=a[1]*factor
    return x, y

def rotacionHoraria(a):
    #xcos+ysen, -xsen+ycos
    x=int(a[0]*math.cos(math.pi/2) + a[1]*math.sin(math.pi/2))
    y=int(-(a[0]*math.sin(math.pi/2)) + a[1]*math.cos(math.pi/2))
    return x, y

def rotacionAntiHoraria(a):
    #xcos-ysen, xsen+ycos
    x=int(a[0]*math.cos(math.pi/2) - a[1]*math.sin(math.pi/2))
    y=int(a[0]*math.sin(math.pi/2) + a[1]*math.cos(math.pi/2))
    return x, y

def calcularPosPlano(o, pos):
    x=pos[0]-o[0]
    y=-1*(pos[1]-o[1])
    return x, y

def dibujarCircunferencia(pant, punto, a, b, c):
    pygame.draw.circle(pant, [a, b, c], pos, 5, 0)

'''
Para posiciones en pantalla
def rotacionHoraria(a):
    #xcos+ysen, -xsen+ycos
    x=abs(int(a[0]*math.cos(math.pi/2) + a[1]*math.sin(math.pi/2)))
    y=abs(int(-(a[0]*math.sin(math.pi/2)) + a[1]*math.cos(math.pi/2)))
    return x, y

def rotacionAntiHoraria(a):
    #xcos-ysen, xsen+ycos
    x=abs(int(a[0]*math.cos(math.pi/2) - a[1]*math.sin(math.pi/2)))
    y=abs(int(a[0]*math.sin(math.pi/2) + a[1]*math.cos(math.pi/2)))
    return x, y
'''

def calcularPosPantalla(o, p):
    x=o[0]+p[0]
    y=o[1]-p[1]
    return x, y

def calcularVectorCanonico(v1, v2):
    x=v2[0] - v1[0]
    y=v2[1] - v1[1]
    return x, y


if __name__ == '__main__':
    pygame.init()
    print 'Funciona'
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Para borrar pantalla pant.fill([0,0,0])








    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            #CLIC
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
            #TECLA
            if event.type == pygame.KEYDOWN:
'''
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
'''
