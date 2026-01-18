import csv

with open("Day-026-nato-alphabets/nato_phonetic_alphabet.csv") as file:
    data = csv.reader(file)
    next(data)
    data_dict = {row[0]:row[1] for row in data}

word = input("What's the letter: ").upper()
output= [data_dict[letter] for letter in word]
print(output)