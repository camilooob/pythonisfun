import random
# variable en mayuscula es constante.
FRAMES = ['''
     +---+
     |   |
     +   |
         |   START
         |   GAME
         |
         |
         |
         +-----------+
         +-----------+''', '''
     +---+
     |   |
     +   |
     O   |  TRY AGAIN
         |
         |
         |
         |
         +-----------+
         +-----------+''', '''
     +---+
     |   |
     +   |
     O   |  TRY AGAIN
     |   |
         |
         |
         |
         +-----------+
         +-----------+''', '''
     +---+
     |   |
     +   |
     O   |  TRY AGAIN
    /|   |
         |
         |
         |
         +-----------+
         +-----------+''', '''
     +---+
     |   |
     +   |
     O   |  TRY AGAIN
    /|\  |
         |
         |
         |
         +-----------+
         +-----------+''', '''
     +---+
     |   |
     +   |
     O   |  TRY AGAIN
    /|\  |
     |   |
         |
         |
         +-----------+
         +-----------+''', '''
     +---+
     |   |
     +   |  TRY AGAIN
     O   |
    /|\  |
     |   |
    /    |
         |
         +-----------+
         +-----------+''', '''
     +---+
     |   |
     |   |   GAME
     +   |   OVER
     O   |
    /|\  |
	 |   |
    / \  |
         +-----------+
         +-----------+''', '''
''']

WORDS = [
    'casa',
    'refrigerador',
    'dalmata',
    'carro',
    'reloj',
    'macbook'
]


def generate_random():


index = random.choice(WORDS)
return WORDS[index]


def start():
    word_random = generate_random()
    pass


# main
def main():
    print("Bienvido a Ahorcado by Camilo Baquero")
    start()
