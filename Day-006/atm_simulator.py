balance = 1000.00
transaction_history = []

def check_balance():
    print(f"Your current balance is : {balance:.2f}")

def deposit(amount):
    global balance
    if amount <= 0:
        print("❌ Invalid deposit amount. Please enter a positive number.")
        return
    else:
        balance += amount
    deposit_message = f"{amount} Deposited"
    print(f"✅ Successfully deposited {amount:.2f}")
    transaction_history.append(deposit_message)

def withdraw(amount):
    global balance
    if amount <=0:
        print("❌ Invalid withdrawal amount. Please enter a positive number.")
        return
    if balance >= amount:
        balance -= amount
        print(f"{amount} Withdrawed from account")
        withdraw_message = f"{amount} Withdrawed"
        transaction_history.append(withdraw_message)
    else:
        print("Insufficient Balance")

def print_receipt():
    """Prints a full history of all transactions"""
    if not transaction_history:
        print("📜 No transactions yet.")
        return
    print("\n📜 TRANSACTION RECEIPT")
    print("----------------------")
    for transaction in transaction_history:
        print(transaction)
    print(f"\nFinal Balance: {balance:.2f}")

def main():
    print("=== WELCOME TO USAMA'S ATM ===")
    while True:
        print("\nPlease select an option:")
        print("1.  Check Balance")
        print("2.  Deposit Funds")
        print("3.  Withdraw Funds")
        print("4.  Print Transaction Receipt")
        print("5.  Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                deposit(amount)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                withdraw(amount)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print_receipt()
        elif choice == "5":
            print("👋 Thank you for using our ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

main()