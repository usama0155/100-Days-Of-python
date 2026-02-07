# 🃏 Blackjack Capstone Project

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-green?style=for-the-badge)
![Bootcamp](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2011-orange?style=for-the-badge)

A console-based **Blackjack** game built with Python. This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** by **Angela Yu**. It demonstrates core programming concepts including functions, lists, loops, conditionals, and modular code structure.

## 🚀 Features

-   **Full Blackjack Rules**: Implements standard rules including Ace valuation (1 or 11), dealing cards, and scoring logic.
-   **Computer AI**: The computer plays automatically according to casino rules (must draw until score is 17 or higher).
-   **Dynamic Scoring**: Handles "Blackjack" (natural 21) and busts (>21) correctly.
-   **ASCII Art**: Uses the `art` module to display logos and win/lose messages for a better user experience.
-   **Replayability**: Users can play multiple rounds in a single session without restarting the script.

## 🎮 How to Play

- When prompted, type 'y' to start a new game or 'n' to exit.
- You will see your cards and the computer's first card.
- Type 'y' to Hit (get another card).
- Type 'n' to Stand (pass your turn).
- The game ends when someone gets a Blackjack, goes over 21, or both players stand. The winner is announced based on the final scores.

## 💻 Code Structure
### The project is organized into logical functions to ensure readability and maintainability:

- deal_cards(): Randomly selects a card from the deck.
- calculate_score(cards): Calculates the total score, handling the special case for Aces (11 vs 1). Returns 0 to represent a Blackjack.
- compare(u_score, c_score): Determines the winner based on game rules and returns the appropriate result message.
- play_game(): The main game loop that handles card dealing, user input, computer logic, and final result display.

## 📂 Project Context
This project was completed as Day 11 of the 100 Days of Code challenge. It serves as a capstone project for the beginner section of the course, consolidating knowledge of control flow and functions.
