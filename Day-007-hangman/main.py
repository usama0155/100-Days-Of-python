import random
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)

random_word = random.choice(word_list)

# Replacing letter of words to _
placeholder = ""
for letter in random_word:
    placeholder += "_"
print(f"Word to Guess: {placeholder}")

# Taking Guess from user and replacing it with letters(if they got correct)
game_over = False
random_word_list = []
live = 6
while not game_over:
    print(f"**********************{live}/6 LIVES**********************")
    guess_letter = input("Guess the letter: ").lower()
    if guess_letter in random_word_list:
        print(f"You Already Guessed {guess_letter}")
    display = ""
    for letter in random_word:
        if letter == guess_letter:
            display += letter
            random_word_list.append(letter)
        elif letter in random_word_list:
            display += letter
        else:
            display += "_"
    

    print(f"Word to guess: {display}")
    if guess_letter not in random_word:
        live -= 1
        print(f"You guessed {guess_letter}, that's not in word. You lose a life.")
        if live == 0:
            game_over = True
            print(f"**********************IT WAS {random_word}, YOU LOSE**********************")

    if "_" not in display:
        print("**********************YOU WON**********************")
        game_over = True
    print(stages[live])
