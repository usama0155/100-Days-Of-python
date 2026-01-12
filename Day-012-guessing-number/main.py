from random import randint
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5
def checking(user_guess,actual_number,turns):
    if user_guess > actual_number:
        print("Too high")
        return turns - 1
    elif user_guess < actual_number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answe was {actual_number}")

def difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL



def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,101)
    turns = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = checking(guess,answer,turns)
        if turns == 0:
            print("Good luck next time, you ran out of attempts")
            return
        elif guess != answer:
            print("Guess again")

game()