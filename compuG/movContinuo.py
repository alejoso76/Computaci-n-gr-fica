import pygame
import math
ANCHO=640
ALTO=480

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Carga la imagen a una variable
    nave=pygame.image.load('thor.png')
    fondo=pygame.image.load('fondo.png')
    #La ubica en pantalla
    posNave=[10,10]

    pantalla.blit(fondo, [0,0])
    pantalla.blit(nave, posNave)
    pygame.display.flip()

    print 'Funciona'
    fin=False
    var_x=0
    var_y=0
    #x=0
    reloj=pygame.time.Clock()
    info=nave.get_rect()
    print 'Ancho=', info[2], 'Alto=', info[3]
    while not fin:
        '''
        x+=1
        posNave[0]=10+x
        pantalla.fill([0, 0, 0])
        pantalla.blit(nave, posNave)
        pygame.display.flip()
        reloj.tick(60)
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if posNave[0]>-5:
                        var_x=-2
                    else:
                        var_x=0

                if event.key==pygame.K_RIGHT:
                    if posNave[0]<ANCHO-info[2]:
                        var_x=2
                    else:
                        var_x=0

                if event.key==pygame.K_UP:
                    var_y=-2

                if event.key==pygame.K_DOWN:
                    var_y=+2

            if event.type==pygame.KEYUP:
                 #Variaciones
                 var_x=0
                 var_y=0
        #Right
        if  posNave[0]<=ANCHO-info[2]:
            posNave[0]+=var_x
        else:
            posNave[0]=ANCHO-info[2]

        #Left
        if  posNave[0]>0:
            posNave[0]+=var_x
        else:
            posNave[0]=0
        #Up
        if  posNave[1]>0:
            posNave[1]+=var_y
        else:
            posNave[1]=0
        #Down
        if  posNave[1]<=ALTO-info[3]:
            posNave[1]+=var_y
        else:
            posNave[1]=ALTO-info[3]

        print posNave
        pantalla.fill([0,0,0])
        pantalla.blit(fondo, [0,0])
        pantalla.blit(nave, posNave)
        pygame.display.flip()
        reloj.tick(60)
