class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setEdad(self, edad):
        self.edad = edad
