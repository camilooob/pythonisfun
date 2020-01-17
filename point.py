class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def SqSum(self):
        powx = self.x * self.x
        powy = self.y * self.y
        powz = self.z * self.z
        sumpow = powx + powy + powz
        return sumpow

prueba = Point(2, 3, 4)

print(prueba.SqSum())
