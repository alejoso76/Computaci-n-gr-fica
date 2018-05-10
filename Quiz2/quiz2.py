import pygame
from libpol import*
import math

ALTO=700
ANCHO=700
centro = [350,350]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    p = Polar(centro,ANCHO,ALTO,pantalla)
    p.ejes()

    fin=False
    y=5
    reloj=pygame.time.Clock()
    angulo = 0
    Q = [350,350]
    P = [0,0]
    Q2 = [-350,350]
   
    i = 0

    var = Q[0]
    var2 = P[0]
    con1 = 0
    con = 0
    band = 0
    band2 = 0
    uno = 0
    dos = 0


    while not fin:

        if P[0] > Q[0]:
            x1 = P[0]-Q[0]
            band = 1
            var += 1
           
            
        else:
            x1 = Q[0]-P[0]
            band2 = 1


        if con1 <= x1 :
            pantalla.fill(NEGRO)
            p.Punto(p.recta(P,Q,var))
            pygame.display.flip()
            if band == 1:
                var += 1
            if band2== 1:
                var-=1
            con1 += 1


            

        if P[0]>Q2[0] and var<= P[0]:
            x = P[0]-Q2[0]
            uno = 1
            var2 -= 1
            
        else:
            dos = 1
            x = Q2[0]-P[0]

            
        if con <= x and var<= P[0]:
            pantalla.fill(NEGRO)
            p.Punto(p.recta(Q2,P,var2))
            pygame.display.flip()
            #p.ejes()
            if uno == 1:
                var2 -= 1
            if dos == 1:
                var2+=1
            con += 1
            
            


        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:

                #print 'tecla de raton', pygame.mouse.get_pressed()
                pantalla.fill(NEGRO)
                pos = pygame.mouse.get_pos() #coordenadas del raton
                pygame.display.flip()
                p.ejes()
                r = int(math.sqrt(((pos[0]-centro[0])**2)+((pos[1]-centro[1])**2)))
                p.Punto([0,0],r)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    angulo -= 1
                    
                if event.key == pygame.K_UP:
                    angulo += 1
                   

                pantalla.fill(NEGRO)
                p.Punto([0,0],r)
                p.Polares(r,angulo)
                pygame.display.flip()
                p.ejes()
                



               