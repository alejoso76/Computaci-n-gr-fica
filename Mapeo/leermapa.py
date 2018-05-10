import pygame
import ConfigParser
ancho=640
alto=480

negro=[0,0,0]

def recortar(max_x, max_y, archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()

    ancho_imagen=infoFondo[2]
    alto_imagen=infoFondo[3]

    alto_corte=alto_imagen/altoSprite

    ancho_corte=ancho_imagen/anchoSprite


    m=[]
    for y in range(max_y):
        fila=[]
        for x in range(max_x):
            cuadro=fondo.subsurface(x*ancho_corte,y*alto_corte,ancho_corte,alto_corte)
            fila.append(cuadro)
        m.append(fila)
    return m

def dibujarMapa(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    ancho_imagen=infoFondo[2]
    alto_imagen=infoFondo[3]

    alto_corte=alto_imagen/altoSprite

    ancho_corte=ancho_imagen/anchoSprite

    i=0
    for a in range (len(mapa)):
        for e in mapa[a]:
            #print e, interprete.get(e,'nom'), interprete.get(e,'x'), interprete.get(e,'y')
            posXPantalla=int(interprete.get(e,'x'))
            posYPantalla=int(interprete.get(e,'y'))
            pantalla.blit(m[posYPantalla][posXPantalla], [i*ancho_corte,a*alto_corte])
            i+=1
        i=0

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])

    interprete=ConfigParser.ConfigParser()
    interprete.read('mapa.map')
    nom_ar=interprete.get('nivel', 'origen')
    #Cantidad sprites filas y columnas
    anchoSprite=int(interprete.get('nivel', 'an'))
    altoSprite=int(interprete.get('nivel', 'al'))


    print 'Ancho=', anchoSprite, 'Alto=', altoSprite


    m=recortar(anchoSprite,altoSprite,nom_ar)
    mapa=interprete.get('nivel', 'mapa')
    #Divide el mapa por lineas
    mapa=mapa.split('\n')
    print mapa
    i=0
    '''
    for a in range (len(mapa)):
        for e in mapa[a]:
            print e, interprete.get(e,'nom'), interprete.get(e,'x'), interprete.get(e,'y')
            posXPantalla=int(interprete.get(e,'x'))
            posYPantalla=int(interprete.get(e,'y'))
            pantalla.blit(m[posYPantalla][posXPantalla], [i*anchoSprite,a*altoSprite])
            i+=1
        i=0
    '''
    dibujarMapa(nom_ar)
    '''
    print mapa[0]
    print mapa[1][3]
    '''
    #pantalla.fill(negro)
    #pantalla.blit(m[0][0], [0,0])
    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
