import pygame
#Dibuja triangulo y lo escala con el teclado
ANCHO=640
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
    return a[0]*factor, a[1]*factor



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana

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
                if cont==1:
                    o=mostrarPos()
                    dibujarPlano(o, pantalla)
                    pygame.display.flip()
                    lista.append(o)
                if cont>1:
                    lista.append(mostrarPos())

            if event.type == pygame.KEYDOWN:

                if event.key==pygame.K_UP:
                    pantalla.fill([0, 0, 0])
                    dibujarPlano(o, pantalla)
                    puntos=lista
                    '''
                    print 'Puntos iniciales:'
                    print puntos
                    '''
                    puntos[0]=escalarPunto(puntos[0], 1.5)
                    puntos[1]=escalarPunto(puntos[1], 1.5)
                    puntos[2]=escalarPunto(puntos[2], 1.5)
                    ''''
                    print 'Puntos finales:'
                    print puntos
                    '''
                    dibujarTriangulo(puntos[0], puntos[1], puntos[2], pantalla)


                if event.key==pygame.K_DOWN:
                    pantalla.fill([0, 0, 0])
                    dibujarPlano(o, pantalla)
                    puntos=lista
                    '''
                    print 'Puntos iniciales:'
                    print puntos
                    '''
                    puntos[0]=escalarPunto(puntos[0], 0.5)
                    puntos[1]=escalarPunto(puntos[1], 0.5)
                    puntos[2]=escalarPunto(puntos[2], 0.5)
                    '''
                    print 'Puntos finales:'
                    print puntos
                    '''
                    dibujarTriangulo(puntos[0], puntos[1], puntos[2], pantalla)

            if cont==3:
                dibujarTriangulo(lista[0], lista[1], lista[2], pantalla)
                cont=0
                #lista=[]
