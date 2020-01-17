class Maniferos:
    def __init__(self, nombre, sexo, patas):
        self.nombre = nombre
        self.sexo = sexo
        self.patas = patas

    def printDet(self):
        print("Nombre es:", self.nombre)
        print("El sexo es:", self.sexo)
        print("Numero de Paras", self.patas)


class Perros(Maniferos): #No olvidar poner la clase padre
    def __init__(self, nombre, sexo, patas, raza):
        Maniferos.__init__(self, nombre, sexo, patas)
        self.raza = raza

    def printDogDet(self):
        self.printDet()
        print("La raza es:", self.raza)


dog1 = Perros("Cronos", "Macho", 4, "Dalmata")
dog1.printDogDet()
