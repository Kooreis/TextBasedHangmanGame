```python
import random

def hangman():
    word_list = ['python', 'java', 'ruby', 'javascript']
    random_number = random.randint(0, 3)
    word = word_list[random_number]
    guessed_letters = []
    attempts = 10

    print('Let\'s play Hangman!')
    
    while attempts > 0:

        failed = 0

        for char in word: 
            if char in guessed_letters: 
                print(char, end = '')
            else: 
                print("_", end = '')
                failed += 1

        if failed == 0:
            print('\nYou Win') 
            print('The word is: ', word) 
            break

        guess = input("\n\nGuess a letter:")

        guessed_letters.append(guess) 

        if guess not in word: 
            attempts -= 1
            print("\nIncorrect!")
            print("You have ", + attempts, ' more guesses')

            if attempts == 0:
                print("\nYou Lose")
                print('The word was: ', word)

hangman()
```