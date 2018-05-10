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
    fondo=pygame.image.load('animals.png')
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

    i=0

    alto_corte=alto_imagen/8
    ancho_corte=ancho_imagen/12

    x=0
    y=0
    movR=[]
    movL=[]
    movU=[]
    movD=[]
    posGato=[50,50]
    dir='R'

    #Ancho:30, alto:40
    for i in range(3):
        cuadro=fondo.subsurface(i*ancho_corte,2*alto_corte,ancho_corte, alto_corte)
        movR.append(cuadro)

    for i in range(3):
        cuadro=fondo.subsurface(i*ancho_corte,1*alto_corte,ancho_corte, alto_corte)
        movL.append(cuadro)

    for i in range(3):
        cuadro=fondo.subsurface(i*ancho_corte,3*alto_corte,ancho_corte, alto_corte)
        movU.append(cuadro)

    for i in range(3):
        cuadro=fondo.subsurface(i*ancho_corte,0*alto_corte,ancho_corte, alto_corte)
        movD.append(cuadro)

    pantalla.blit(movR[0], posGato)
    pygame.display.flip()


    reloj=pygame.time.Clock()


    while not fin:

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    dir='L'
                    var_x=-2
                    posGato[0]+=var_x
                    pantalla.fill([0,0,0])
                    pantalla.blit(movL[i], posGato)
                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0


                if event.key==pygame.K_RIGHT:
                    dir='R'
                    var_x=2
                    posGato[0]+=var_x
                    pantalla.fill([0,0,0])
                    pantalla.blit(movR[i], posGato)

                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0


                if event.key==pygame.K_UP:
                    dir='U'
                    var_y=-2
                    posGato[1]+=var_y
                    pantalla.fill([0,0,0])
                    pantalla.blit(movU[i], posGato)

                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0

                if event.key==pygame.K_DOWN:
                    dir='D'
                    var_y=+2
                    posGato[1]+=var_y
                    pantalla.fill([0,0,0])
                    pantalla.blit(movD[i], posGato)

                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0

            if event.type==pygame.KEYUP:
                 #Variaciones
                 var_x=0
                 var_y=0

        #pantalla.blit(movR[i], posGato)

        pygame.display.flip()

        reloj.tick(15)
