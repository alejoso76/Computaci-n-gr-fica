from pygame import *
# todos los ejercicios 3


ANCHO = 1000
ALTO = 600

MITAD = 500


#Colores

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white =[255,255,255]
black = [0,0,0]
gold = [255,215,0]
darkturquoise = [0,206,209]

# 1 Objeto que se mueve en una trayectoria
# 2 Cardioide

class Recta():

    def __init__(self,q,p):
        self.vec = q
        self.pendiente = float(p[1]-q[1])/(p[0]-q[0])
        self.x = p[0]
        self.b = p[1]-(p[0]*self.pendiente)
        self.y = int(p[0]*self.pendiente + self.b)

    def Calculate(self,x):
        self.y = int(x*self.pendiente + self.b)

    def Position(self,var = 0):
        self.x = var
        self.Calculate(var)
        return [self.x,self.y]



    

def punto(p,color = red,r = 5):
    draw.circle(pantalla,color,p,r)

if __name__ == '__main__':

    init()
    pantalla = display.set_mode([ANCHO,ALTO])
    display.set_caption("ejemplo")
    fin = False

    reloj = time.Clock()

    #recta.calculate([0,350])
    P = [0,300]
    Q = [500,0]
    Q2 = [500,600]

    recta = Recta(Q,P)
    recta1 = Recta(Q2,P)
    
    var_x = Q[0]
    var_x2 = 0 
    pantalla.fill(black)




    while not fin:
        for evento in event.get():
            if evento.type == QUIT:
                fin = True

        #punto(recta.Position(var_x),darkturquoise)
        pantalla.fill(black)
        if var_x >= 0:
            punto(recta.Position(var_x),darkturquoise)
            var_x-=1
        if var_x2 <= MITAD and var_x <= 0:
            punto(recta1.Position(var_x2),darkturquoise)
            var_x2+=1
        #if var_x2 > MITAD:

            #print recta2.pendiente, recta2.Position2(var_y)
            #punto(recta2.Position2(var_y),red)
            #var_y -= 1  


        display.flip()

        reloj.tick(900)