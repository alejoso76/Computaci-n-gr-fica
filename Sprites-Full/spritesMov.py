import pygame
import math
ANCHO=640
ALTO=480

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #Carga la imagen a una variable
    fondo=pygame.image.load('mov1.png')
    infoFondo=fondo.get_rect()
    print infoFondo

    ancho_imagen=infoFondo[2]
    alto_imagen=infoFondo[3]

    print "Ancho = ",ancho_imagen
    print "Alto = ",alto_imagen

    print 'Funciona'
    fin=False

    pos_x=0
    pos_y=0

    i=0
    
    alto_corte=alto_imagen/4
    ancho_corte=ancho_imagen/12

    x=0
    y=0
    fila=[]
    #Ancho:48, alto:72 sin disparo
    #Ancho:62, alto:72 con disparo

    #Animacion mov
    for i in range(10):
        cuadro=fondo.subsurface((i+2)*ancho_corte,y*alto_corte,50,72)
        fila.append(cuadro)




    reloj=pygame.time.Clock()


    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        pantalla.fill([0,0,0])
        pantalla.blit(fila[i], [pos_x, pos_y])
        pygame.display.flip()
        i+=1
        if i>=10:
            i=0
        pos_x+=5
        reloj.tick(30)
