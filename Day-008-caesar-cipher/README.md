# 🔐 Caesar Cipher - Encode & Decode

> **Day 08** of the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by **Angela Yu**

---

## 📖 About

A command-line Caesar Cipher tool that allows users to **encrypt** and **decrypt** messages using a shift-based substitution technique. The Caesar Cipher is one of the oldest and simplest encryption methods, where each letter in the message is shifted by a fixed number of positions in the alphabet.

## 🚀 How It Works

### Encoding
Each letter in the plaintext is shifted **forward** by the specified number of positions in the alphabet.

Example: "hello" with shift 5 → "mjqqt"

### Decoding
Each letter in the ciphertext is shifted **backward** by the specified number of positions to recover the original message.

Example: "mjqqt" with shift 5 → "hello"


## 🛠️ Features

- **Encode** messages with a custom shift value
- **Decode** messages by providing the shift used during encoding
- Handles **non-alphabetic characters** (spaces, punctuation, numbers) — they remain unchanged
- Supports **wrap-around** using modulo operation (e.g., shifting `z` by 1 gives `a`)
- **Loop functionality** — encode/decode multiple messages without restarting the program
- **Input validation** for choosing encode/decode mode

## Usage

Do you Want to encode or decode? encode
Enter you message: hello world
Number of shift: 5
Your encrypt message is:
mjqqt btwqi

Type 'yes' if you want to go again. otherwise 'no': yes

Do you Want to encode or decode? decode
Enter Message to decode: mjqqt btwqi
Enter shift that is used to encode the message: 5
Your decrypt message is:
hello world

Type 'yes' if you want to go again. otherwise 'no': no

## 📚 Concepts Practiced
- Functions — modular code with encoder(), decoder(), choose_type(), and main()
- Loops — for loops for character iteration and while loops for program flow
- String manipulation — indexing, concatenation, and the .lower() / .strip() methods
- Modulo operator (%) — for alphabet wrap-around
- Conditional statements — if/elif/else for input handling
- User input handling — interactive CLI experience
## ⚠️ Limitations
- Only works with lowercase English letters (a–z)
- Does not encrypt numbers or special characters (they are preserved as-is)
- Shift value must be an integer
