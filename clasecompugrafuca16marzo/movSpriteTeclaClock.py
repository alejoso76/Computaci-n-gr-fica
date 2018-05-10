import pygame
import math
ANCHO=640
ALTO=480

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Carga la imagen a una variable
    nave=pygame.image.load('thor.png')
    #La ubica en pantalla
    posNave=[10,10]
    pantalla.blit(nave, posNave)

    pygame.display.flip()

    print 'Funciona'
    fin=False
    x=0
    reloj=pygame.time.Clock()
    dir='R'
    while not fin:
        x+=1
        if dir=='R':

            posNave[0]+=x
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()
            reloj.tick(10)

        if dir=='L':
            #x+=1
            posNave[0]-=x
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()
            reloj.tick(10)

        if dir=='U':
            #x+=1
            posNave[1]-=x
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()
            reloj.tick(10)

        if dir=='D':
            #x+=1
            posNave[1]+=x
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()
            reloj.tick(10)


        if posNave[0]>500:
            reloj.tick(0)
            x=0
            posNave[0]=500
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()

        if posNave[0]<0:
            reloj.tick(0)
            x=0
            posNave[0]=0
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()

        if posNave[1]>480-128:
            reloj.tick(0)
            x=0
            posNave[1]=480-128
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()

        if posNave[1]<0:
            reloj.tick(0)
            x=0
            posNave[1]=0
            pantalla.fill([0, 0, 0])
            pantalla.blit(nave, posNave)
            pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:

                    if(posNave[0]>=0):
                        dir='L'
                        print 'Left'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0], posNave[1]]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        dir='N'
                        print 'Left'

                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()

                if event.key==pygame.K_RIGHT:

                    if(posNave[0]<625):
                        dir='R'
                        print 'Right'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        dir='N'
                        print 'Right'
                        x=0
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()


                if event.key==pygame.K_UP:

                    if(posNave[1]>=0):
                        dir='U'
                        print 'Up'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        dir='N'
                        print 'Up'
                        x=0
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()

                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()

                if event.key==pygame.K_DOWN:

                    if(posNave[1]<470):
                        dir='D'
                        print 'Down'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0], posNave[1]]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        dir='N'
                        print 'Down'

                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0], 0]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
        print posNave
