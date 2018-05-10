import pygame
import math
#Dibuja triangulo y lo escala con el teclado
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                lista.append(mostrarPos())

            if event.type == pygame.KEYDOWN:


                if event.key==pygame.K_UP:
                    pFijo=lista[0]
                    pantalla.fill([0, 0, 0])
                    dibujarPlano(o, pantalla)
                    puntos=lista
                    '''
                    print 'Puntos iniciales:'
                    print puntos
                    '''
                    puntos[0]=llevarAlOrigen(pFijo, puntos[0])
                    puntos[1]=llevarAlOrigen(pFijo, puntos[1])
                    puntos[2]=llevarAlOrigen(pFijo, puntos[2])

                    puntos[0]=escalarPunto(puntos[0], 1.5)
                    puntos[1]=escalarPunto(puntos[1], 1.5)
                    puntos[2]=escalarPunto(puntos[2], 1.5)

                    puntos[0]=regresarAPos(pFijo, puntos[0])
                    puntos[1]=regresarAPos(pFijo, puntos[1])
                    puntos[2]=regresarAPos(pFijo, puntos[2])


                    ''''
                    print 'Puntos finales:'
                    print puntos
                    '''
                    dibujarTriangulo(puntos[0], puntos[1], puntos[2], pantalla)


                if event.key==pygame.K_DOWN:
                    pFijo=lista[0]
                    pantalla.fill([0, 0, 0])
                    dibujarPlano(o, pantalla)
                    puntos=lista
                    '''
                    print 'Puntos iniciales:'
                    print puntos
                    '''
                    puntos[0]=llevarAlOrigen(pFijo, puntos[0])
                    puntos[1]=llevarAlOrigen(pFijo, puntos[1])
                    puntos[2]=llevarAlOrigen(pFijo, puntos[2])

                    puntos[0]=escalarPunto(puntos[0], 0.5)
                    puntos[1]=escalarPunto(puntos[1], 0.5)
                    puntos[2]=escalarPunto(puntos[2], 0.5)

                    puntos[0]=regresarAPos(pFijo, puntos[0])
                    puntos[1]=regresarAPos(pFijo, puntos[1])
                    puntos[2]=regresarAPos(pFijo, puntos[2])


                    ''''
                    print 'Puntos finales:'
                    print puntos
                    '''
                    dibujarTriangulo(puntos[0], puntos[1], puntos[2], pantalla)



            if cont==3:
                dibujarTriangulo(lista[0], lista[1], lista[2], pantalla)
                cont=0
