print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? $"))
percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
tip = bill*(percentage/100)
total_bill = bill + tip 
splited_bill = total_bill/split
print(f"Each person should pay: ${splited_bill:.2f}")