from pygame import *
from math import *
from random import *

ANCHO = 1000
ALTO = 700

#Colores

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white =[255,255,255]
black = [0,0,0]


O = [int(ANCHO/2),int(ALTO/2)]
ANG = [0,30,45,90,135,180,210,260,300,360]

def dibujar_plano():

    # Dibujo eje y
    draw.line(pantalla,blue,[O[0],0],[O[0],ALTO])
    #dibujo eje x
    draw.line(pantalla,blue,[0,O[1]],[ANCHO,O[1]])
    draw.polygon(pantalla,black,[(10,10),(10,40),(40,40),(40,10),(35,20),(27,10),(17,20)])


def cartesiano(p):
    np = [p[0]+O[0],O[1]-p[1]]
    return np

def punto(p,color,r=1):
    #color = [randint(0,255),randint(100,255),randint(0,100)]
    draw.circle(pantalla,color,cartesiano(p),r)

def line(p1,p2,color=black):
    draw.line(pantalla,color,cartesiano(p1),cartesiano(p2))

def polar(a,r=1):
    np =[]
    a = radians(a)
    c = cos(a)
    s = sin(a)
    np = [int(r*c),int(r*s)]
    return np

def rosa(a,n,amp=100):
    np =[]
    a = radians(a)
    r = amp*cos(n*a)
    c = cos(a)
    s = sin(a)
    np = [int(r*c),int(r*s)]
    return np

def corazon(i):
    np = []
    r = 100 +100*cos(i)
    c = cos(i)
    s = sin(i)
    np = [int(r*c),int(r*s)]
    return np

def espiral(a,b,i):
    np = []
    r = a + b*i
    c = cos(i)
    s = sin(i)
    np = [int(r*c),int(r*s)]
    return np

def cicloide(a,i,r=1):
    np =[]
    i = radians(i)
    c = cos(i)
    s = sin(i)
    np = [int(a*(i-s)),int(a*(1-c))]
    return np


if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO,ALTO])
    display.set_caption("ejemplo")
    fin = False

    reloj = time.Clock()
    x = [0,360]
    var_x = x[0]
    pantalla.fill(white)

    #func()
    #func([-200,200])
    while not fin:
        for evento in event.get():
            if evento.type == QUIT:
                fin = True

        #dibujar_plano()
        #y = (var_x*3)+2
        #punto([var_x,y])
        #punto(rosa(var_x,6,200),5)
        #line(rosa(var_x,7,200),rosa(var_x+1,7,200))
        #line(espiral(5,2,var_x),espiral(5,2,var_x+1),red)
        #punto(polar(var_x,200))

        #if corazon(var_x)[1] >= 0:
        #    punto(corazon(var_x),red)
        #ine(corazon(var_x),corazon(var_x-1),red)
        punto(espiral(5,2,var_x),5)
        #punto(cicloide(50,var_x))
        display.flip()
        if var_x >= 50: var_x = 0
        var_x+=1

        reloj.tick(60)