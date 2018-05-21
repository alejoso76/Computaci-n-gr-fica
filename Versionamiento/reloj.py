import pygame
import random

ANCHO=500
ALTO=500

BLANCO = [255, 255, 255]
NEGRO = [0, 0, 0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Carga la imagen a una variable

    print 'Funciona'
    fin=False
    reloj=pygame.time.Clock()
    pag=1
    Fuente=pygame.font.Font(None, 32)
    segundo=0
    tasa=60
    seg=0
    lim=15

    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pag+=1
        x=random.randrange(0,5)
        if pag==1:
            texto=Fuente.render("Pagina 1", True, BLANCO)
            imagen = pygame.image.load("emoji-feliz.png")
            imagen = pygame.transform.scale(imagen, [50, 50])
            pantalla.fill(NEGRO)
            pantalla.blit(texto, [100, 100])
            pantalla.blit(imagen, [300, 100])
            pygame.display.flip()
            reloj.tick(50)

        if pag==2:
            segundo = lim-(seg//tasa)
            seg+=1
            if segundo>5:
                txt_reloj = "Reloj: {0:00} s".format(segundo)
                texto=Fuente.render("Pagina 2", True, BLANCO)
                textoReloj=Fuente.render( txt_reloj, True, BLANCO)

            else:
                txt_reloj = "Reloj: {0:00} s".format(segundo)
                texto=Fuente.render("Pagina 2", True, ROJO)
                textoReloj=Fuente.render( txt_reloj, True, ROJO)

            if segundo==0:
                pag+=1
                
            pantalla.fill(NEGRO)
            pantalla.blit(texto, [100, 100])
            pantalla.blit(textoReloj, [300, 100])
            pygame.display.flip()
            reloj.tick(50)
        if pag==3:
            fin=True
