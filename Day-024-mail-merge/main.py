placeholder = "[name]"
with open("Day-024-mail-merge/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Day-024-mail-merge/Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace(placeholder, strip_name)
        with open(f"Day-024-mail-merge/Output/ReadyToSend/letter_to_{strip_name}.docx" , 'w') as complete_letter:
            complete_letter.write(new_letter)