import pygame
import math
ANCHO=640
ALTO=480

class Cuadro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill([255,0,0])
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.vel_x=0
        self.presionado=False
        self.inicio=False
        self.vel_x=-5


    def update(self):
        if self.presionado:
            self.rect.center=pygame.mouse.get_pos()
        if self.inicio:
            self.rect.x+=self.vel_x

class Bloque(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill([0,255,0])
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=400
        self.vel_x=0
        self.presionado=False

    def update(self):
        if self.presionado:
            self.rect.center=pygame.mouse.get_pos()


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana

    todos=pygame.sprite.Group()
    cuadros=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    cuadro=Cuadro()
    cuadros.add(cuadro)
    todos.add(cuadro)

    b=Bloque()
    bloques.add(b)
    todos.add(b)


    print 'Funciona'
    fin=False
    presionado=False
    cuadro.inicio=False
    reloj=pygame.time.Clock()



    while not fin:

        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            encima=cuadro.rect.collidepoint(pos)

            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in bloques:
                    if b.rect.collidepoint(pos):
                        b.presionado=True

                for c in cuadros:
                    if c.rect.collidepoint(pos):
                        c.presionado=True

            if event.type == pygame.MOUSEBUTTONUP:

                if b in bloques:
                    b.presionado=False

                for c in cuadros:
                    if c.rect.collidepoint(pos):
                        c.presionado=False
                        c.inicio=True

        #Colision
        for b in bloques:
                  alcance=pygame.sprite.collide_circle(cuadro, b)
                  if alcance:
                      print 'disparo'




        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.draw.line(pantalla, [0,255,0], [100,200], [400,150])

        pygame.display.flip()
        reloj.tick(20)
        print cuadro.inicio
