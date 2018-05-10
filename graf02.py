#Interfaz grafica
import pygame
ANCHO=600
ALTO=480

if __name__ == '__main__':
    pygame.init()
    print 'Funciona'
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana





    cont=0

    lista = []

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                lista.append(pygame.mouse.get_pos())
            if cont % 2 == 0 and cont > 0:
                pygame.draw.line(pantalla, [0, 255, 0], lista[0], lista[1]) #La dibuja pero no actualiza la pantalla
                pygame.display.flip() #Actualiza la pantalla
