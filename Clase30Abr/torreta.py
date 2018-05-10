
import pygame

ANCHO=640
ALTO=480



class Cuadro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill([255,0,0])
        self.rect=self.image.get_rect()
        self.rect.x=ANCHO-75
        self.rect.y=400
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
        self.rect.x=25
        self.rect.y=400
        self.vel_x=0
        self.presionado=False

    def update(self):
        if self.presionado:
            self.rect.center=pygame.mouse.get_pos()

class Torreta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill([255,255,0])
        self.rect=self.image.get_rect()
        self.rect.x=ANCHO/2
        self.rect.y=400
        self.vel_x=0
        self.presionado=False

    def update(self):
        if self.presionado:
            self.rect.center=pygame.mouse.get_pos()

class Clic(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,30])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.presionado=False


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana

    todos=pygame.sprite.Group()
    cuadros=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    torretas=pygame.sprite.Group()
    clicsV=pygame.sprite.Group()
    clicsR=pygame.sprite.Group()
    clicsA=pygame.sprite.Group()

    clic=Clic([0,255,0])
    todos.add(clic)
    clicsV.add(clic)

    clic2=Clic([255,0,0])
    clic2.rect.x=ANCHO-30
    todos.add(clic2)
    clicsR.add(clic2)

    clic3=Clic([255,255,0])
    clic3.rect.x=ANCHO/2
    todos.add(clic3)
    clicsA.add(clic3)
    '''
    cuadro=Cuadro()
    cuadros.add(cuadro)
    todos.add(cuadro)


    b=Bloque()
    bloques.add(b)
    todos.add(b)
    '''


    print 'Funciona'
    fin=False
    #presionado=False
    #cuadro.inicio=False
    reloj=pygame.time.Clock()
    cont=0
    #disparo=pygame.mixer.Sound('shoot.wav')



    while not fin:

        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            #encima=cuadro.rect.collidepoint(pos)
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                for s in clicsV:
                    if s.rect.collidepoint(pos):
                        b=Bloque()
                        bloques.add(b)
                        todos.add(b)



                for s in clicsR:
                    if s.rect.collidepoint(pos):
                        cuadro=Cuadro()
                        cuadros.add(cuadro)
                        todos.add(cuadro)

                for s in clicsA:
                    if s.rect.collidepoint(pos):
                        cuadro=Torreta()
                        torretas.add(cuadro)
                        todos.add(cuadro)



                for b in bloques:
                    if b.rect.collidepoint(pos):
                        b.presionado=True

                for c in cuadros:
                    if c.rect.collidepoint(pos):
                        c.presionado=True

                for t in torretas:
                    if t.rect.collidepoint(pos):
                        t.presionado=True

            if event.type == pygame.MOUSEBUTTONUP:

                for b in bloques:
                    b.presionado=False

                for c in cuadros:
                    if c.rect.collidepoint(pos):
                        c.presionado=False
                        c.inicio=True

        #Colision
        for c in cuadros:
            ls=pygame.sprite.spritecollide(c, bloques, False)
            for b in ls:
                if b.rect.right >= c.rect.left:
                    c.rect.left=b.rect.right
                    c.vel_x=0
        for t in torretas:
            for c in cuadros:
                alcance=pygame.sprite.collide_circle(t, c)
                if alcance:
                    print 'disparo'
                    #disparo.play()
                    c.kill()



            '''
            for b in bloques:
            '''
            #c.vel_x=-5



        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        #pygame.draw.line(pantalla, [0,255,0], [100,200], [400,150])

        pygame.display.flip()
        reloj.tick(20)
        #print cuadro.inicio
