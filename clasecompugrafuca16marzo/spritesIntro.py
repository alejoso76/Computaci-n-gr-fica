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
    #x=0
    #reloj=pygame.time.Clock()

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
                    if(posNave[0]>=-115):
                        print 'Left'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0]-5, posNave[1]]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        print 'Left'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[625, posNave[1]]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()

                if event.key==pygame.K_RIGHT:
                    if(posNave[0]<625):
                        print 'Right'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0]+5, posNave[1]]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        print 'Right'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[-115, posNave[1]]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()


                if event.key==pygame.K_UP:
                    if(posNave[1]>=-110):
                        print 'Up'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0], posNave[1]-5]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        print 'Up'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0], 470]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()

                if event.key==pygame.K_DOWN:
                    if(posNave[1]<470):
                        print 'Down'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0], posNave[1]+5]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
                    else:
                        print 'Down'
                        #pintarPantallaNegra(pantalla)
                        pantalla.fill([0, 0, 0])
                        pygame.display.flip()
                        posNave=[posNave[0], 0]
                        #print pos
                        pantalla.blit(nave, posNave)
                        pygame.display.flip()
        print posNave
