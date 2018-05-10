import pygame
import ConfigParser
ancho=576
alto=346

negro=[0,0,0]
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
        self.accion=0

    def update(self):

        if self.accion==0:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice >= len(self.f[self.accion]):
                self.indice = 0
                self.accion=1

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[4][3]
        self.rect=self.image.get_rect()
        self.indice=0
        self.rect.x=50
        self.rect.y=250
        self.vel_x=0
        self.accion=0

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

        if self.accion==2:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice >= len(self.f[self.accion]):
                self.indice = 0
                self.accion=1

        if self.accion==3:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice >= len(self.f[self.accion]):
                self.indice = 0
                self.accion=1


def recortar(max_x, max_y, archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()

    ancho_imagen=infoFondo[2]
    alto_imagen=infoFondo[3]

    alto_corte=alto_imagen/8

    ancho_corte=ancho_imagen/12


    m=[]
    for y in range(max_y):
        fila=[]
        for x in range(max_x):
            cuadro=fondo.subsurface(x*ancho_corte,y*alto_corte,ancho_corte,alto_corte)
            fila.append(cuadro)
        m.append(fila)
    return m

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])
    fondo=pygame.image.load('mapa01.png')
    animales=pygame.image.load('animals.png')
    infoAnimales=animales.get_rect()

    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()

    matrizAnimales=recortar(12, 8, 'animals.png')

    jugador=Jugador(matrizAnimales)
    jugadores.add(jugador)
    todos.add(jugador)

    cantidad_enemigos=10
    '''
    for i in range(cantidad_enemigos):
        e=Enemigo(matrizAnimales)

        e.rect.x=random.randint(0, ANCHO-e.rect.width)
        e.rect.y=random.randint(-30, 0-e.rect.height)
        enemigos.add(e)
        todos.add(e)
    '''
    reloj=pygame.time.Clock()
    var_x=0
    var_y=0




    #pantalla.fill(negro)
    pantalla.blit(fondo, [0,0])
    pantalla.blit(jugador.f[2][0], [jugador.rect.x, jugador.rect.y])
    pygame.display.flip()
    i=0
    fin=False
    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    dir='L'
                    jugador.accion=1
                    var_x=-8
                    jugador.rect.x+=var_x
                    pantalla.blit(fondo, [0,0])
                    pantalla.blit(jugador.f[jugador.accion][i], [jugador.rect.x, jugador.rect.y])
                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0



                if event.key==pygame.K_RIGHT:
                    dir='R'
                    jugador.accion=2
                    var_x=8
                    jugador.rect.x+=var_x
                    pantalla.blit(fondo, [0,0])
                    pantalla.blit(jugador.f[jugador.accion][i], [jugador.rect.x, jugador.rect.y])

                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0


                if event.key==pygame.K_UP:
                    dir='U'
                    jugador.accion=3
                    var_y=-8
                    jugador.rect.y+=var_y
                    pantalla.blit(fondo, [0,0])
                    pantalla.blit(jugador.f[jugador.accion][i], [jugador.rect.x, jugador.rect.y])

                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0

                if event.key==pygame.K_DOWN:
                    dir='D'
                    jugador.accion=0
                    var_y=+8
                    jugador.rect.y+=var_y
                    pantalla.blit(fondo, [0,0])
                    pantalla.blit(jugador.f[jugador.accion][i], [jugador.rect.x, jugador.rect.y])

                    pygame.display.flip()
                    i+=1
                    if i>=3:
                        i=0

            if event.type==pygame.KEYUP:
                 #Variaciones
                 var_x=0
                 var_y=0
        '''
        #Right
        if  jugador.rect.x<=ancho:
            jugador.rect.x+=var_x

        #Left
        if  jugador.rect.x>0:
            jugador.rect.x+=var_x
        #Up
        if  jugador.rect.y>0:
            jugador.rect.y+=var_y

        #Down
        if  jugador.rect.y<=alto:
            jugador.rect.y+=var_y
        else:
            jugador.rect.y=alto
        '''
    todos.update()
    #pantalla.blit(jugador.f[jugador.accion][i], [jugador.rect.x, jugador.rect.y])
    reloj.tick(15)
