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

PISTAS = [
    'lugar',
    'electrodomestico',
    'raza perro',
    'transporte',
    'accesorio',
    'dispositivo'
]


def generate_random():
	index = random.randint(0, len(WORDS) - 1)
	return WORDS[index], PISTAS[index]


def display_board(hidden_word, tries, pista):
	print(FRAMES[tries])
    print('--- * --- * ---- * --- * --- * ---')


def start():
    word_random, pista = generate_random()
    hidden_word = ['-'] * len(word_random)
    tries = 0

    while True:
        display_board(hidden_word, tries, pista)
        current_letter_a = input('Escribe una letra:'))
        current_letter = current_letter_a.lower()


def main():
    print("Bienvido a Ahorcado by Camilo Baquero")
    start()
