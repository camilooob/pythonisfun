class Player:
    teamName = "Millonarios"

    def __init__(self,name):
        self.name = name
    @classmethod
    def getName(cls):
        return cls.teamName

print(Player.getName())
