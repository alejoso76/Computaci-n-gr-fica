import pygame
import math
ANCHO=640
ALTO=480

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Carga la imagen a una variable
    nave=pygame.image.load('thor.png')
    fondo=pygame.image.load('mapa.jpg')
    #La ubica en pantalla
    posNave=[10,10]
    pos_x=0
    pos_y=0
    posFondo=[0,0]
    pantalla.blit(fondo, [pos_x,pos_y])
    pantalla.blit(nave, posNave)
    pygame.display.flip()

    print 'Funciona'
    fin=False
    var_x=0
    var_y=0

    hor=-2
    ver=-2

    #x=0
    reloj=pygame.time.Clock()
    info=nave.get_rect()
    print 'Ancho=', info[2], 'Alto=', info[3]
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:
                    var_x=-2

                if event.key==pygame.K_RIGHT:
                    var_x=2

                if event.key==pygame.K_UP:
                    var_y=-2

                if event.key==pygame.K_DOWN:
                    var_y=+2
############################################################################################

                if event.key==pygame.K_LEFT and posNave[0]<=0:
                    pos_x+=2
                    #var_x-=2
                    reloj.tick(60)

                if event.key==pygame.K_RIGHT and posNave[0]>=512:
                    pos_x-=2
                    #var_x+=2
                    reloj.tick(60)

                if event.key==pygame.K_UP and posNave[1]<=0:
                    pos_y+=2
                    reloj.tick(60)


                if event.key==pygame.K_DOWN and posNave[1]>=ALTO-info[3]:
                    pos_y-=2
                    reloj.tick(60)

                '''
                if event.key == pygame.K_UP and (posobj[1] > 0):
					posobj[1] -= 20
				elif event.key == pygame.K_DOWN and (posobj[1] < (height-128)):
					posobj[1] += 20
				elif event.key == pygame.K_LEFT and (posobj[0] > 0):
					posobj[0] -= 20

				elif event.key == pygame.K_LEFT and (posobj <= 0) and (posfondo < 0):
					posfondo[0] += 20
				elif event.key == pygame.K_RIGHT and (posobj[0] < (width-158)):
					posobj[0] += 20
				elif event.key == pygame.K_RIGHT and (posobj[0] >= (width-158)) and (posfondo[0] > -300):
					posfondo[0] -= 20
                '''
            if event.type==pygame.KEYUP:
                 #Variaciones
                 var_x=0
                 var_y=0

        #Limites
        #Right
        if  posNave[0]<ANCHO-info[2]:
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
        if  posNave[1]<ALTO-info[3]:
            posNave[1]+=var_y
        else:
            posNave[1]=ALTO-info[3]

        print posNave
        pantalla.fill([0,0,0])
        pantalla.blit(fondo, [pos_x, pos_y])
        pantalla.blit(nave, posNave)
        pygame.display.flip()
        reloj.tick(60)
