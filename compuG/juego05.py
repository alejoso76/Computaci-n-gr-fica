import pygame
import math
import random
import time
ANCHO=640
ALTO=480

VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

class Usuario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Representacion del objeto
        self.image=pygame.Surface([20,20])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=100

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Representacion del objeto
        self.image=pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.espera=0

    def update(self):
        if self.espera<0:
            self.rect.x+=random.randint(-10,10)
            self.rect.y+=random.randint(-10,10)
        else:
            self.espera-=1

class Agresivo(Enemigo):
    def __init__(self):
        pass

class Punto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Representacion del objeto
        self.image=pygame.Surface([20,20])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.espera=0

    def update(self):
        if self.espera<0:
            self.rect.x+=random.randint(0,10)
        else:
            self.espera-=1


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    pygame.display.set_caption('Game')



    #Grupo general
    todos=pygame.sprite.Group()

    #Grupo usuarios
    usuario=Usuario()
    usuarios=pygame.sprite.Group()
    usuarios.add(usuario)
    todos.add(usuario)

    #Grupo enemigos
    enemigos=pygame.sprite.Group()
    cantidad_enemigos=10
    for i in range(cantidad_enemigos):
        e=Enemigo()
        e.espera=random.randrange(0, 100)
        e.rect.x=random.randint(0, ANCHO-e.rect.width)
        e.rect.y=random.randint(0, ALTO-e.rect.height)
        enemigos.add(e)
        todos.add(e)

    #Grupo puntos
    puntos=pygame.sprite.Group()
    cantidad_puntos=10
    for i in range(cantidad_puntos):
        p=Punto()
        p.espera=random.randrange(0, 100)
        p.rect.x=random.randint(0, ANCHO-p.rect.width)
        p.rect.y=random.randint(0, ALTO-p.rect.height)
        puntos.add(p)
        todos.add(p)



    var_x=0
    var_y=0
    puntosCont=0
    salud=100
    vel=0


    reloj=pygame.time.Clock()
    pygame.display.flip()
    fin=False


    #Ciclo principal
    while not fin:
        #Gestionb de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True





        #Right
        if  usuario.rect.x<ANCHO-1-usuario.rect.width:
            usuario.rect.x+=var_x #*vel
        else:
            usuario.rect.x=ANCHO-usuario.rect.width

        #Left
        if  usuario.rect.x>0:
            usuario.rect.x+=var_x #*vel
        else:
            usuario.rect.x=0

        #Up
        if  usuario.rect.y>0:
            usuario.rect.y+=var_y #*vel
        else:
            usuario.rect.y=0

        #Down
        if  usuario.rect.y<ALTO-1-usuario.rect.height:
            usuario.rect.y+=var_y #*vel
        else:
            usuario.rect.y=ALTO-usuario.rect.height

        #Colision
        ls_col_enemigos = pygame.sprite.spritecollide(usuario, enemigos, True)
        ls_col_puntos = pygame.sprite.spritecollide(usuario, puntos, True)


        for ec in ls_col_enemigos:
            salud-=100
            print salud

            if salud==0:
                fuente = pygame.font.SysFont("None", 60)
                rendered = fuente.render ("You have lost", 0, ROJO)
                pantalla.blit(rendered,(ANCHO/2-100, ALTO/2-100))
                pygame.display.flip()

                print 'YOU HAVE LOST'
                time.sleep(3)
                fin=True

        for ec in ls_col_puntos:
            puntosCont+=1
            print puntosCont

            if puntosCont==10:
                fuente = pygame.font.SysFont("None", 60)
                rendered = fuente.render ("You have won", 0, AZUL)
                pantalla.blit(rendered,(ANCHO/2-100, ALTO/2-100))
                pygame.display.flip()

                print 'YOU HAVE WON'
                time.sleep(3)
                fin=True

        pygame.mouse.set_visible(False)
        pos=mostrarPos()
        usuario.rect.x=pos[0]
        usuario.rect.y=pos[1]

        #print usuario.rect
        pantalla.fill(NEGRO)
        enemigos.update()
        #usuarios.draw(pantalla)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
