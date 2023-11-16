print("""
 _    _              _   _    _____   __  __              _   _ 
| |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |
| |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |
|  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |
| |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |
|_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|

""")

import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "computer", "keyboard", "debugging"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts):
    hangman_doodle = [
        "  ____",
        " |    |",
        f" |    {'' if attempts < 1 else 'O'}",
        f" |   {'/' if attempts < 2 else ''}{'|' if attempts < 3 else ''}{'\\' if attempts >= 3 else ''}",
        f" |   {'/' if attempts < 4 else ''} {'\\' if attempts >= 4 else ''}",
        " |",
        "========="
    ]

    for line in hangman_doodle:
        print(line)

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                attempts += 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        draw_hangman(attempts)
        print("Attempts remaining:", max_attempts - attempts)
        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()