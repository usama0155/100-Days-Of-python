# Day 07 - The Hangman Game

## Overview
This is my solution for **Day 7** of the **100 Days of Code** Python Bootcamp by Dr. Angela Yu.

I built a fully functional **Hangman** game in Python. The player has to guess the hidden word letter by letter. The game includes lives, ASCII art stages, and win/lose conditions.

## Features
- Random word selection from a word list
- 6 lives system
- Visual hangman stages using ASCII art
- Tracks previously guessed letters
- Clear win and lose messages
- User-friendly interface in the console

## How to Play
1. Run the `main.py` file.
2. The game will display a series of underscores representing the hidden word.
3. Guess one letter at a time.
4. You have **6 lives**. Every wrong guess costs one life.
5. Guess the full word correctly before running out of lives to win!


## What I Learned
- How to use `while` loops for game loops
- Working with lists and string indexing
- Managing game state (lives, guessed letters, display)
- Using ASCII art to improve user experience
- Understanding the importance of proper variable naming and logic flow

## Challenges Faced
- Tracking correctly guessed letters and avoiding repeated guesses
- Building the display word dynamically in each round
- Properly handling game over conditions (win & lose)
