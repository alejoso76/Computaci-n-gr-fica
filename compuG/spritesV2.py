import pygame
import math
ANCHO=640
ALTO=480

VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]

class Bloque(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Representacion del objeto
        self.image=pygame.Surface([20,20])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    usuario=Bloque()
    grupo=pygame.sprite.Group()

    var_x=0
    var_y=0
    vel=0
    grupo.add(usuario)
    grupo.draw(pantalla)

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
        if  usuario.rect.x<=ANCHO-21:
            usuario.rect.x+=var_x #*vel
        else:
            usuario.rect.x=ANCHO-21

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
        if  usuario.rect.y<=ALTO-21:
            usuario.rect.y+=var_y #*vel
        else:
            usuario.rect.y=ALTO-21

        print usuario.rect
        pantalla.fill(NEGRO)
        grupo.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
