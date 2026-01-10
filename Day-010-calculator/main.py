from calculator_art import calculator_ascii
def add(n1, n2):
    return n1 + n2

def substract(n1 , n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : substract,
    "*" : multiplication,
    "/" : divide
}
def calculator():
    print(calculator_ascii)
    calculation = True
    num1 = float(input("What's First Number: "))
    while calculation:
        for symbols in operation:
            print(symbols)
        user_operation = input("Choose operater: ")
        num2 = float(input("What's the next number: "))
        reuslt = operation[user_operation](num1,num2)
        print(f"{num1} {user_operation} {num2} = {reuslt}")

        choice = input(f"Type 'y' to continue with {reuslt},or type 'n' to start a new calculation: ")
        if choice == 'y':
            num1 = reuslt
        else:
            calculation = False
            print("\n" * 20)
            calculator()

calculator()
