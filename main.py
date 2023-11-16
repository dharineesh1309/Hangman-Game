import random

print("""
 _    _              _   _    _____   __  __              _   _ 
| |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |
| |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |
|  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |
| |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |
|_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|

""")

menu = input('Type "s" to start the game, or any other key to quit: ')
while menu == 's':
    guessed = {}
    guessed = set()
    attempts = 5
    answer = random.choice(
        ['happy', 'physics', 'pluck', 'route', 'tedious', 'disappear', 'science'])
    display = "-" * len(answer)

    print(" ")
    while attempts > 0 and display.count('-') > 0:
        print(display)
        guess = input("Input a letter: ")

        if guess in guessed:
            print("You already tried that letter")

        if guess in answer:
            display = ""
            for i in range(len(answer)):
                if answer[i] == guess or answer[i] in guessed:
                    if answer[i] not in guessed:
                        guessed.add(answer[i])
                    display += answer[i]
                else:
                    display += "-"

            print("\n")
        else:
            attempts -= 1
            print("No such letter in the word, " +
                  str(attempts) + " attempts left.\n")

    if display.count('-') > 0:
        print("You lost and are hanged :(")
    else:
        print("You guessed " + display + " and survived!")

    menu = input('\nType "s" to start the game, or any other key to quit: ')
