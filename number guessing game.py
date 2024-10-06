# Md Mushfiqur Rahman
# mmrahman@umc.edu

import random # module that contains the function of selecting a random integer

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.\nYou can choose to leave anytime you want")
print("Picking a number...")

correct_number = random.randint(1, 100) # selecting a random integer between 1 and 100
guess_count = 0 # initiating the number of guesses
while True:
    guess = input("What is your guess (from 1 to 100)? (or type -1 to quit): ") # player input
    # Validating the input of the guess
    try:
        guess = int(guess)  # Convert the input to an integer

        if guess in [-1] + list(range(1, 101)):  # Check if the guess is in the valid range
            # if the player wants to exit the game.
            if guess == -1:
                print("You've chosen to exit the game. Goodbye!")
                break

            guess_count += 1 # counting the number of guesses.
            # The conditions of the game.
            if guess < correct_number:
                print("Wrong. You need to guess higher.")
            elif guess > correct_number:
                print("Wrong. You need to guess lower.")
            else:
                print(f'Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.')
                break
        # if the player chooses integer outside of the given range and -1. This error will pop up.
        else:
            print("Invalid Input: The number should be an integer from 1 up to 100")
    # If the player input is wrong input (floating number and string). This error will be showed.
    except ValueError:
        print("Invalid Input: Please enter a valid integer.")

