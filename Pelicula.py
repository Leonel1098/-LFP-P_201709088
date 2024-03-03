class Pelicula:

    def __init__(self, nombre, actor, año, genero):
        self.nombre = nombre
        self.actor = actor
        self.año = año
        self.genero = genero
    
        #Métodos set
    def setNombre (self,nombre):      
        self.nombre = nombre

    def setActor (self,actor):
        self.actor = actor

    def setAño (self,año):      
        self.año = año

    def setGenero (self,genero):      
        self.genero = genero

    #Métodos get
    def getNombre (self):      
        return self.nombre

    def getActor (self):
        return self.actor

    def getAño (self):    
        return self.año

    def getGenero (self):      
        return self.genero