# Secret Auction Program (100 Days of Python Project)

## Overview

This Python program simulates a "secret auction" where multiple bidders can place their bids without others knowing the amounts. After all participants have entered their bids, the program reveals the winner with the highest bid. This project is a practical exercise from Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

## Features

*   **Interactive Bidding:** Guides users through entering their name and bid via the command line.
*   **Secret Bidding:** Simulates clearing the screen between bidders to keep individual bids private until the auction concludes.
*   **Winner Determination:** Automatically identifies the highest bidder and announces them as the winner.
*   **Simple & Intuitive:** A straightforward, console-based application.


### Interaction

Once the program starts:

1.  It will welcome you and prompt for the first bidder's name and bid.
2.  After a bid is entered, it will ask if there are other bidders.
    *   Type `'yes'` (or any variation like 'YES', 'y', etc.) to allow another person to bid. The screen will "clear" to maintain secrecy for the next bidder.
    *   Type `'no'` (or 'NO', 'n', etc.) when all participants have placed their bids.
3.  Finally, the program will reveal the winner and their highest bid.

### Example Interaction

Welcome to secret auction program.
What's your name: Alice
What's your bid: $120
Are there other bidders? Type 'yes' OR 'no': yes

... (screen clears, simulating a fresh terminal for the next bidder) ...

What's your name: Bob
What's your bid: $150
Are there other bidders? Type 'yes' OR 'no': yes

... (screen clears) ...

What's your name: Charlie
What's your bid: $110
Are there other bidders? Type 'yes' OR 'no': no
Winner is Bob With highest bid of $150


## Code Structure

*   `getting_data()`: A function responsible for taking a bidder's name and bid input.
*   `getting_top_bidder(auction_db)`: Takes the dictionary of all bids, processes it to find the maximum bid, and prints the winner.
*   `main()`: The main control flow function that manages the bidding loop, collects data, and calls the winner determination.
*   `auction_db = {}`: A dictionary used to store `name: bid` pairs.
*   `print("\n"*30)`: This line is used to simulate clearing the screen by printing many newlines, effectively pushing previous entries out of view.
