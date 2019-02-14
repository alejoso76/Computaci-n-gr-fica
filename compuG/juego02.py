import pygame
import math
import random
ANCHO=640
ALTO=480

VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]

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
            self.rect.x+=random.randint(0,10)
        else:
            self.espera-=1



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana

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



    var_x=0
    var_y=0
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
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    var_x=-2
                    #var_y=0
                    #vel+=1

                if event.key==pygame.K_RIGHT:
                    var_x=2
                    #var_y=0
                    #vel+=1

                if event.key==pygame.K_UP:
                    var_y=-2
                    #var_x=0
                    #vel+=1

                if event.key==pygame.K_DOWN:
                    var_y=+2
                    #var_x=0
                    #vel+=1

            if event.type==pygame.KEYUP:
                 #Variaciones
                 var_x=0
                 var_y=0

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

        #print usuario.rect
        pantalla.fill(NEGRO)
        enemigos.update()
        #usuarios.draw(pantalla)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
