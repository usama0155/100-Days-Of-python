import random 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


selection = ["rock", "paper", "scissors"]
computer_choice =random.choice(selection)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

if computer_choice == selection[0]:
    print("Computer Chose")
    print(rock)
elif computer_choice == selection[1]:
    print("Computer Chose")
    print(paper)
else:
    print("Computer Chose")
    print(scissors)

if computer_choice == selection[user_choice]:
    print("It's Draw!!!")
elif selection[user_choice] == 'rock' and computer_choice == 'scissors':
    print("You Win!!!")
elif selection[user_choice] == 'scissors' and computer_choice == 'paper':
    print("You Win!!!")
elif selection[user_choice] == 'paper' and computer_choice == 'rock':
    print("You Win!!!")
else:
    print("You Lose!!!")
