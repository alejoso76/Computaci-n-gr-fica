#Crear una pantalla y un sprite animado en una posicion x,y de esa pantalla
#Dar clic en otra posicion de la pantalla y el sprite debe moverse hasta ese punto
import pygame
import math
ANCHO=640
ALTO=480

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

def calcularPendiente(p1, p2):
    x=p2[0]-p1[0]
    y=p2[1]-p1[1]
    m=float(y/x)
    return m

def calcularIntercepto(m, p2):
    b=p2[1]-m*p2[0]
    return b

def calcularY(m, b, x):
    funcion=m*x + b
    return funcion

class Jugador(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[1][0]
        self.rect=self.image.get_rect()
        self.indice=0
        self.rect.x=10
        self.rect.y=10
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
    ken=pygame.image.load('ken.png')
    infoKen=ken.get_rect()

    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()


    ancho_imagen=infoKen[2]
    alto_imagen=infoKen[3]
    '''
    print "Ancho = ",ancho_imagen
    print "Alto = ",alto_imagen
    '''

    print 'Funciona'
    fin=False

    alto_corte=alto_imagen/10
    ancho_corte=ancho_imagen/7

    posKen=[50,50]
    fila=[]
    matriz=[]

    limites=[4,4,3, 5, 2, 4, 5, 5, 7, 1]
    x=0
    clic=0
    posF=[]


    reloj=pygame.time.Clock()
    for x in range(10):
        matriz.append([])
        for i in range(limites[x]):
            cuadro=ken.subsurface(i*ancho_corte,x*alto_corte,ancho_corte, alto_corte)
            matriz[x].append(cuadro)



    jugador=Jugador(matriz)
    jugadores.add(jugador)
    todos.add(jugador)


    while not fin:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                posI=[jugador.rect.x, jugador.rect.y]
                posF=mostrarPos()
                print posI, posF

            if event.type == pygame.MOUSEBUTTONUP:
                m=calcularPendiente(posI, posF)
                print m





        #pantalla.blit(movR[i], posGato)

        todos.update()
        pantalla.fill([0,0,0])

        todos.draw(pantalla)

        pygame.display.flip()

        reloj.tick(20)
