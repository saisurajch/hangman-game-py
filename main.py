import random
import os
from words import word_list
from art import stages
from art import logo

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = []
#
for _ in range(word_length):
    display.append("_")
#
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    # for windows we use 'cls', if os is linux or Mac we use 'clear'
    if guess in display:
        print(f"You've already guessed {guess}")

    #
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = chosen_word[position]
    #
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
    #
    print(f"{' '.join(display)}")
    #
    if "_" not in display:
        end_of_game = True
        print("You win.")
    #
    print(stages[lives])