import ConfigParser
#Manipula la libreria
interprete = ConfigParser.ConfigParser()
print 'Funciona'
interprete.read('proto.map')

#get
print interprete.get('seccion','n')
print interprete.get('seccion','m')

print interprete.get('seccion2','n')

#sections
print interprete.sections()

#items
print interprete.items('seccion')
