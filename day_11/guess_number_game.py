from random import randint
from arts.day_11_art import logo

# working with Global variables
COMPUTER_CHOICE = randint(1, 100)
LEVEL = [5, 10]

def num_checker(user_num, computer_num):
    if user_num > computer_num:
        print("Too high")
        return False
    elif user_num < computer_num:
        print("Too low")
        return False
    print(f"You have WON\nYour number is {user_num} and computer number is {computer_num}")
    return True


def number_guess_game():
    global LEVEL
    global COMPUTER_CHOICE

    print(logo)
    print("Welcome to My Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")

    difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        difficulty = LEVEL[0]
    else:
        difficulty = LEVEL[1]

    print(COMPUTER_CHOICE)
    while difficulty >= 1:
        print(f"You have {difficulty} attempts remaining to guess the number.")
        user_input = int(input("Make a guess: "))
        if num_checker(user_input, COMPUTER_CHOICE):
            break
        print("Guess Again")
        difficulty -= 1

    text = "Better luck next time, would you like to play again?"
    if user_input == COMPUTER_CHOICE:
        text = "Good job, would you like to play again?"
    print(text)
    user_input = input("Yes or No? ").lower()
    if user_input == "yes":
        print("\n" * 100)
        COMPUTER_CHOICE = randint(1, 100)
        return number_guess_game()

    print("Thanks for playing, good bye")

number_guess_game()




