class Student:
    max = 300

    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        sum = self.phy + self.chem + self.bio
        return sum


    def Percentaje(self):
        percen = (self.totalObtained()/self.max)*100
        return percen


mark1 = Student("Mark", 80, 90, 40)
print(mark1.totalObtained())
print(mark1.Percentaje())
