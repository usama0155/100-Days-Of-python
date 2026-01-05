import random 

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+',
    '-', '.', '/', ':', ';', '<', '=', '>', '?',
    '@', '[', ']', '^', '_', '{', '}', '~'
]

number_letter = int(input("How many would you like in your Password_list: "))
number_of_numbers = int(input("How many number you like: "))
number_symbols = int(input("How many symbols you like: "))

# passowrd = ""
# for char in range(1, number_letter +1):
#     random_char = random.choice(letters)
#     passowrd += random_char

# for char in range(1, number_of_numbers + 1):
#     random_number = random.choice(numbers)
#     passowrd += random_number

# for char in range(1, number_symbols+1):
#     random_symbols = random.choice(symbols)
#     passowrd += random_symbols

# print(f"Your Password is: {passowrd}")

password_list = []
for char in range(1, number_letter +1):
    random_char = random.choice(letters)
    password_list += random_char

for char in range(1, number_of_numbers + 1):
    random_number = random.choice(numbers)
    password_list += random_number

for char in range(1, number_symbols+1):
    random_symbols = random.choice(symbols)
    password_list += random_symbols
random.shuffle(password_list)
password = ""
for letter in password_list:
    password += letter

print(f"Your Password is: {password}")