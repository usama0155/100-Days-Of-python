# Day 10 - Calculator App 🧮

This project is part of my **100 Days of Python Professional Bootcamp** journey. On Day 10, I built a functional terminal-based calculator that utilizes recursion, dictionaries, and functions with outputs.

## 🚀 Features
- **Basic Arithmetic:** Supports addition, subtraction, multiplication, and division.
- **Continuous Calculation:** Allows you to perform further calculations on the result of a previous operation.
- **Recursion:** The ability to reset the calculator and start a fresh session without restarting the script.
- **Clean UI:** Includes ASCII art for a better user experience and clears the screen between new sessions.

## 🛠️ How it Works
1. The program uses a **Dictionary** to map mathematical symbols (`+`, `-`, `*`, `/`) to specific functions.
2. It prompts the user for the first number and the desired operation.
3. After showing the result, the user can:
   - Type `'y'` to continue calculating with the current result.
   - Type `'n'` to clear the screen and start a brand new calculation.

## 📋 Key Programming Concepts
- **Higher-Order Functions:** Passing functions as values within a dictionary.
- **While Loops:** To maintain the state of the current calculation.
- **Recursion:** Calling the `calculator()` function within itself to restart the application.

## 🎮 Demo
```
What's First Number: 12
+
-
*
/
Choose operater: *
What's the next number: 3
12.0 * 3.0 = 36.0
Type 'y' to continue with 36.0, or type 'n' to start a new calculation: y
+
-
*
/
Choose operater: -
What's the next number: 6
36.0 - 6.0 = 30.0
Type 'y' to continue with 30.0, or type 'n' to start a new calculation: n
```
