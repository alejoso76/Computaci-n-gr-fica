import pygame
import math
#Theta 0->360
#
ANCHO=600
ALTO=480

def dibujarPunto(p, pant):
     pygame.draw.circle(pant, [0, 255, 0], p, 5, 0)
     pygame.display.flip()

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

def calcularPosPantalla(o, p):
    x=o[0]+p[0]
    y=o[1]-p[1]
    return x, y

def llevarAlOrigen(fijo, p):
    x=p[0]-fijo[0]
    y=p[1]-fijo[1]
    return x,y

def regresarAPos(fijo, p):
    x=p[0]+fijo[0]
    y=p[1]+fijo[1]
    return x,y

def funcionPolar(ang):
    r=math.cos(3*math.radians(ang))
    return r

def calcularPuntoCartesiano(r, ang):
    x=int(100*r*(math.cos(math.radians(ang))))
    y=int(100*r*(math.sin(math.radians(ang))))
    return x, y

#x'=xcos - ysen
#y'=xsen + ycos


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    o=[ANCHO/2, ALTO/2]
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

            #Ciclo
            for i in range (0, 360):
                r=funcionPolar(i)
                #print r
                p=calcularPuntoCartesiano(r, i)
                paux=p
                paux=calcularPosPantalla(o, p)
                #print paux
                dibujarPunto(paux, pantalla)
                pygame.display.flip()
