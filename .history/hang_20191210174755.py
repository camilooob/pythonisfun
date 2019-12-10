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
     |   |   LAST
     +   |   TRY
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
    print('')
    print(hidden_word)
    print('--- * --- * ---- * --- * --- * ---')


def start():
    word_random, pista = generate_random()
    hidden_word = ['-'] * len(word_random)
    tries = 0

    while True:
        display_board(hidden_word, tries, pista)
        current_letter_a = str(input('Escribe una letra:'))
        current_letter = current_letter_a.lower()

        letter_index = []
        for index in range(len(word_random)):
            if word_random[index] == current_letter:
                letter_index.append(index)

        if len(letter_index) == 0:
            if tries == 0:
                display_board(hidden_word, tries, pista)
                print("")
                print('PISTA')
                print('{}'.format(pista))

            if tries == 7:
                display_board(hidden_word, tries, pista)
                print("")
                print('PERDISTE')
                print('La palabra era {}'.format(word_random))
                break
            
            tries += 1
        else:
            for index in letter_index:
                hidden_word[index] = current_letter

                letter_index = []


def main():
    print("Bienvido a Ahorcado by Camilo Baquero")
    start()


main()
