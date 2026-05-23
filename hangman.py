import random

words = ["python", "computer", "developer", "internship", "programming"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game")

while wrong_guesses < max_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed_letters:
        print("Letter already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess")
    else:
        wrong_guesses += 1
        print("Wrong Guess")
        print("Remaining Chances:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("\nYou lost the game")
    print("Correct word was:", secret_word)

print("Game Over")