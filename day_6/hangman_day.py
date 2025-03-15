import random
from arts.day_6_art import word_list, logo, stages

print(logo)

random_word = random.choice(word_list)
word_length = len(random_word)

end_game = False
lives = 6

# Testing random word
print(f"Psssst the word is {random_word}")

# creating blanks for guessing
display = ["_" for x in range(word_length)]
user_letters = ""

# The game
while not end_game:
    
    guess = input("Guess a letter:\n").lower()

    while guess in user_letters:

        print(f"{guess} letter was already guessed, plz try another one")

        guess = input("Guess a letter:\n").lower()
        
    user_letters += guess

    for position, letter in enumerate(random_word):
        if guess == letter:
            display[position] = letter
    
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")
            
    print(f"{' '.join(display)}")

    # Checks if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])