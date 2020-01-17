class Player:
  teamName = 'Liverpool, soy class method'      # class variables

  def __init__(self, name, text):
    self.name = name
    self.text = text        # creating instance variables

  @classmethod
  def getTeamName(cls):
    return cls.teamName

  @staticmethod
  def demo():
    print ("Soy static method.")


print(Player.getTeamName())
# Liverpool
p1 = Player("p","soy instance Method")
print(p1.text)
p1.demo()
# I am a static method
Player.demo()
# I am a static method
