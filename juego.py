import pygame
import math
ANCHO=640
ALTO=480

class Jugador(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[1][0]
        self.rect=self.image.get_rect()
        self.indice=0
        self.rect.x=50
        self.rect.y=250
        self.vel_x=0
        self.accion=1

    def update(self):

        if self.accion==0:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice >= len(self.f[self.accion]):
                self.indice = 0
                self.accion=1

        if self.accion==1:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice >= len(self.f[self.accion]):
                self.indice = 0
                self.accion=1
            self.rect.x += self.vel_x

        if self.accion==2:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice >= len(self.f[self.accion]):
                self.indice=0
                self.accion=1


def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Carga la imagen a una variable
    Danny=pygame.image.load('Danny.png')
    infoDanny=Danny.get_rect()

    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    barriles=pygame.sprite.Group()

    ancho_imagen=infoDanny[2]
    alto_imagen=infoDanny[3]

    print "Ancho = ",ancho_imagen
    print "Alto = ",alto_imagen

    print 'Funciona'
    fin=False
    '''
    alto_corte=alto_imagen/10
    ancho_corte=ancho_imagen/7
    '''
    posKen=[50,50]
    fila=[]
    matriz=[]

    limites=[10]
    anchoC=[]
    altoC=[]


    reloj=pygame.time.Clock()
    for i in range(6):
        cuadro=Danny.subsurface(8,344,33, 65)
        lista.append(cuadro)
    '''
    for x in range(10):
        matriz.append([])
        for i in range(limites[x]):
            cuadro=ken.subsurface(i*ancho_corte,x*alto_corte,ancho_corte, alto_corte)
            matriz[x].append(cuadro)
    '''


    jugador=Jugador(matriz)
    jugadores.add(jugador)
    todos.add(jugador)

    for i in range (10):
        print len(jugador.f[i])

    while not fin:

        for event in pygame.event.get():
            #Caminada
            if jugador.accion==2:

                for b in ls_col:
                    if b.rect.bottom >= (jugador.rect.bottom-25):
                        b.rect.x+=20


            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    jugador.accion=1
                    jugador.vel_x=5


                if event.key == pygame.K_LEFT:
                    jugador.accion=1
                    jugador.vel_x=-5

                if event.key == pygame.K_q:
                    jugador.indice=0
                    jugador.accion=0

                if event.key == pygame.K_w:
                    jugador.indice=0
                    jugador.accion=2




            if event.type == pygame.KEYUP:
                jugador.accion=1
                jugador.vel_x=0



        #pantalla.blit(movR[i], posGato)

        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)

        pygame.display.flip()

        reloj.tick(20)
