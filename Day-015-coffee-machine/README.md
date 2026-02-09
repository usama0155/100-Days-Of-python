# Day 15 - Coffee Machine Project

## Overview
This is a Python program that simulates a coffee machine. Users can order different types of coffee (espresso, latte, cappuccino), insert coins, and receive their drink if resources are available and payment is sufficient. The machine also provides reports on current resources and profit.

## Features
- **Menu System**: Offers three types of coffee with different ingredients and prices
- **Resource Management**: Tracks water, milk, and coffee resources
- **Payment Processing**: Accepts quarters, dimes, nickels, and pennies
- **Transaction Handling**: Calculates change and refunds if payment is insufficient
- **Reporting**: Shows current resource levels and profit
- **Maintenance Mode**: Can be turned off with "off" command

## How to Use
1. Run the program
2. Enter your choice:
   - `espresso` - $1.50
   - `latte` - $2.50
   - `cappuccino` - $3.00
   - `report` - Shows current resources and profit
   - `off` - Turns off the machine
3. If ordering coffee, insert coins when prompted
4. Receive your drink or refund if resources are insufficient

## Code Structure
- **MENU**: Dictionary containing coffee options with ingredients and prices
- **resources**: Dictionary tracking available water, milk, and coffee
- **profit**: Variable tracking total earnings
- **Functions**:
  - `is_resource_available()`: Checks if enough resources exist
  - `process_coin()`: Handles coin input and calculates total
  - `is_transaction_successfull()`: Verifies payment and calculates change
  - `make_coffee()`: Deducts used resources and serves coffee

## Example Usage

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coin:
How many Quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 change
Here is your latte
```

## Learning Outcomes
- Working with nested dictionaries
- Function creation and parameter passing
- Global variables and scope
- While loops for continuous operation
- Conditional logic for decision making
- Basic arithmetic operations

## Repository
[View Code on GitHub](https://github.com/usama0155/100-Days-Of-python/tree/main/Day%2015%20-%20Coffee%20Machine)
