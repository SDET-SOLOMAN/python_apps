import random
import os
from arts import day_12_art

LOGO = day_12_art.logo
VS = day_12_art.vs
DATA = day_12_art.data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_contestants(a, b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(VS)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")

def game_logic(data_pool):
    if len(data_pool) < 2:
        return None, None, None  # End of game

    a = random.choice(data_pool)
    b = random.choice(data_pool)
    while a == b:
        b = random.choice(data_pool)

    if a["follower_count"] > b["follower_count"]:
        correct_answer = "a"
        data_pool.remove(a)
    else:
        correct_answer = "b"
        data_pool.remove(b)

    print(f"For testing purposes, the correct answer is {correct_answer}")
    return correct_answer, a, b

def compare(answer, user_input):
    return answer.lower() == user_input.lower()

def the_game():
    data_pool = DATA.copy()
    score = 0

    while True:
        clear_screen()
        print(LOGO)
        print(f"Current score: {score}")

        correct_answer, a, b = game_logic(data_pool)

        if not correct_answer:
            print(f"\n🎉 Congratulations! You've completed the game with a score of {score}!\n")
            break

        display_contestants(a, b)

        user_input = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if compare(correct_answer, user_input):
            score += 1
            print(f"\n✅ You're right! Current score: {score}\n")
        else:
            print(f"\n❌ Oops! That's wrong.")
            print(f"The correct answer was '{correct_answer.upper()}'!")
            print(f"Final score: {score}\n")
            break

# Main loop for replayability
while True:
    the_game()
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != 'y':
        print("👋 Thanks for playing! Goodbye!")
        break
