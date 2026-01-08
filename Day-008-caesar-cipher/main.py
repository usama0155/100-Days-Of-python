alphabets = 'abcdefghijklmnopqrstuvwxyz'

def encoder():
    message = input("Enter you message: ").lower()
    shift = int(input("Number of shift: "))
    encode_message = ""
    for letter in message:
        if letter in alphabets:
            index = alphabets.index(letter)
            new_index = index + shift 
            encode_message +=alphabets[new_index % 26]
        else:
            encode_message += letter

    print(f"Your encrypt message is: \n{encode_message}")

def decoder():
    decode_message = ""
    message_to_decode = input("Enter Message to decode: ").lower()
    shift_of_encode = int(input("Enter shift that is used to encode the message: "))
    for letter in message_to_decode:
        if letter in alphabets:
            index = alphabets.index(letter)
            new_index = index - shift_of_encode
            decode_message += alphabets[new_index % 26]
        else:
            decode_message += letter

    print(f"Your decrypt message is: \n{decode_message}")

def choose_type():
    while True:
        cipher_type= input("Do you Want to encode or decode? ").lower().strip()
        if cipher_type == "encode":
            encoder()
            break
        elif cipher_type == "decode":
            decoder()
            break
        else:
            print("Invalid Input. Type 'encode' OR 'decode': ")


def main():
    choose_type()
    while True:
        repeat = input("Type 'yes' if you want to go again. otherwise 'no': ")
        if repeat != "no":
            choose_type()
        else:
            break

main()