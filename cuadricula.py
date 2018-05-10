#Interfaz grafica
import pygame
ANCHO=600
ALTO=480

if __name__ == '__main__':
    pygame.init()
    print 'Funciona'
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana


#Horizontal
    for i in range(0, ALTO, 20):
        pygame.draw.line(pantalla, [0, 255, 0], [0,i], [ANCHO,i] ) #La dibuja pero no actualiza la pantalla


#Vorizontal
    for i in range(0, ANCHO, 20):
        pygame.draw.line(pantalla, [0, 255, 0], [i,0], [i,ALTO] ) #La dibuja pero no actualiza la pantalla
    pygame.display.flip()





    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                cont+=1
            if cont==1:
                c1=pos
            if cont==2:
                c2=pos
                pygame.draw.line(pantalla, [0, 255, 0], c1, c2 ) #La dibuja pero no actualiza la pantalla
                pygame.display.flip() #Actualiza la pantalla
                cont=0
            '''
