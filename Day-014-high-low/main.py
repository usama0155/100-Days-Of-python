from game_data import data
import art
import random


def format_data(account):
    account_name = account["name"]
    account_desc= account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_desc}, from {account_country}."

def check(user_guess,account_1,account_2):
    if account_1 > account_2:
        return user_guess == "a"
    else:
        return user_guess == 'b'

print(art.logo)
score = 0
game_runnig = True
account_s = random.choice(data)
#Generate random accounts from data 
while game_runnig:
    account_f = account_s
    account_s = random.choice(data)
    if account_f == account_s:
        account_s = random.choice(data)

    print(f"Comapre A: {format_data(account_f)}")
    print(art.vs)
    print(f"Comapre B: {format_data(account_s)}")

    #Ask user for a guess
    guess = input("Who has more followers, Type 'A' or 'B': ").lower()

    f_account_followers = account_f["follower_count"]
    s_account_followers = account_s["follower_count"]


    is_correct = check(guess,f_account_followers,s_account_followers)

    if is_correct:
        score += 1
        print(f"You're Right! Current score {score}")
    else:
        print(f"Sorry, thats' wrong. Final score: {score}")
        game_runnig = False

