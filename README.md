# Python Documentation

# Hangman Game in Python

This repository contains a simple implementation of the classic Hangman game in Python.

## Description

The script `hangman.py` is a simple text-based Hangman game. The game randomly selects a word from a predefined list of words ('python', 'java', 'ruby', 'javascript') and the player has to guess the word one letter at a time. The player has 10 attempts to guess the word. If the player guesses a letter correctly, the script reveals the letter's position in the word. If the player guesses incorrectly, the number of remaining attempts decreases by one. The game continues until the player guesses the word or runs out of attempts.

## Libraries Used

The script uses the following Python libraries:

- `random`: This library is used to generate random numbers. In this script, it is used to randomly select a word from the list of words.

## How to Run

To run the script, you need to have Python installed on your system. You can then run the script from the command line using the following command:

```bash
python hangman.py
```

## Code Explanation

The script defines a function `hangman()` that implements the game. The function first initializes the list of words, selects a random word, and sets up other necessary variables (like the list of guessed letters and the number of remaining attempts).

The game then enters a loop where it repeatedly asks the player to guess a letter. If the guessed letter is in the word, the script reveals the letter's position in the word. If the guessed letter is not in the word, the number of remaining attempts decreases by one.

The game ends when the player has guessed the word or has run out of attempts. The script then prints a message indicating whether the player has won or lost.

---

# C# Documentation

# CSharp Word Guessing Game

This is a simple console-based word guessing game written in C#. The game randomly selects a word from a predefined list and the player has to guess the word one character at a time.

## Script Explanation

The script begins by defining a list of words. A random word is then selected from this list to be the mystery word that the player has to guess. The player's current guess is represented as an array of characters, initially filled with asterisks (`*`). The player is then repeatedly asked to guess a character. If the guessed character is in the mystery word, the corresponding asterisks in the guess are replaced with the guessed character. The player's current guess is then printed to the console.

## Imported Libraries

The script uses the following libraries:

- `System`: This is a fundamental library in C# that provides classes for input/output, string manipulation, and other basic tasks. In this script, it is used for console input/output and for working with strings and arrays.

- `System.Collections.Generic`: This library provides classes for working with collections of objects. However, in this script, it is not actually used and could be removed.

## Code

```CSharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        string[] listwords = new string[10];
        listwords[0] = "sheep";
        listwords[1] = "goat";
        listwords[2] = "computer";
        listwords[3] = "america";
        listwords[4] = "watermelon";
        listwords[5] = "icecream";
        listwords[6] = "warrior";
        listwords[7] = "thailand";
        listwords[8] = "assembly";
        listwords[9] = "university";
        Random randGen = new Random();
        var idx = randGen.Next(0, 9);
        string mysteryWord = listwords[idx];
        char[] guess = new char[mysteryWord.Length];
        Console.Write("Please enter your guess: ");

        for (int p = 0; p < mysteryWord.Length; p++)
            guess[p] = '*';

        while (true)
        {
            char playerGuess = char.Parse(Console.ReadLine());
            for (int j = 0; j < mysteryWord.Length; j++)
            {
                if (playerGuess == mysteryWord[j])
                    guess[j] = playerGuess;
            }
            Console.WriteLine(guess);
        }
    }
}
```

## How to Run

To run this script, you need a C# compiler such as the one provided by the .NET SDK. You can then compile the script with the command `csc Program.cs` and run it with the command `Program`.

---

# Java Documentation

# Hangman Game in Java

This repository contains a simple implementation of the classic Hangman game in Java.

## Description

The script `HangmanGame.java` is a console-based game where the player has to guess a word by suggesting letters within a certain number of tries. The game starts by randomly selecting a word from a predefined list of words. The player then guesses one letter at a time. If the guessed letter is in the word, the script reveals the position(s) of the letter in the word. If the guessed letter is not in the word, a part of the hangman is drawn. The player continues to guess letters until they have either guessed the word correctly or the hangman is fully drawn.

## Imported Libraries

The script uses the following Java library:

- `java.util.Scanner`: This library is used to read the player's input from the console. It provides methods to parse primitive types and strings using regular expressions, which can be used to break the input into tokens.

## Code Explanation

- The `words` array contains the list of words that the player has to guess.
- The `word` variable is a randomly selected word from the `words` array.
- The `asterisk` string is a string of asterisks that has the same length as the `word`. It is used to hide the word from the player.
- The `count` variable keeps track of the number of incorrect guesses made by the player.
- The `main` method is the entry point of the script. It creates a `Scanner` object to read the player's input and starts the game loop.
- The `hang` method is called every time the player makes a guess. It checks if the guessed letter is in the word and updates the `asterisk` string accordingly. If the guessed letter is not in the word, it increments the `count` variable and calls the `hangmanImage` method.
- The `hangmanImage` method draws a part of the hangman for each incorrect guess.

## How to Run

To run the script, you need to have Java installed on your machine. You can then compile the script using the Java compiler (`javac`) and run it using the Java interpreter (`java`):

```bash
javac HangmanGame.java
java HangmanGame
```

---
