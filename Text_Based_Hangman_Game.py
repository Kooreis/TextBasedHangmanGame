import random

def hangman():
    word_list = ['python', 'java', 'ruby', 'javascript']
    random_number = random.randint(0, 3)
    word = word_list[random_number]
    guessed_letters = []
    attempts = 10

    print('Let's play Hangman!')