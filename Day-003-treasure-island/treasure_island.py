print("Welcome to Treasure Island")
print("Your mission is to find the Treasure.")
left_right = input("You'r at road a croos road. Where do you want to go?(Left or Right) ").lower().strip()
if left_right == 'left':
    print("You've come to lake.There is island in middle of lake.")
    wait_swim = input("type 'wait' to wait for a boat. Type 'swim' to swim across ").lower().strip()
    if wait_swim == 'wait':
        print("you arrive at  island unharmed. There is a house with 3 doors")
        door = input("One red, one yellow and one blue. Which color do you choose? ").lower().strip()
        if door == 'yellow':
            print("You Win")
        elif door == 'red':
            print("There's Fire. Game over!!!")
        else:
            print("Game Over!!!")
    else:
        print("There's Crocadile. Game Over!!!")
else:
    print("Game Over!!!")