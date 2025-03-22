# Deductive Logic Game - Guess the Secret Number

## Introduction
This is a Python-based deductive logic game where the player must guess a secret three-digit number based on hints provided after each guess. The game challenges the player to logically deduce the secret number within 10 attempts.

## Game Rules
- The program generates a **random three-digit secret number** (e.g., "631").
- The player has **10 attempts** to guess the number.
- After each guess, the program provides feedback:
  - **👌 (Correct)** → A correct digit in the correct place.
  - **👍 (Ok)** → A correct digit in the wrong place.
  - **❌ (Wrong)** → No correct digits.
- The game ends when:
  - The player correctly guesses the secret number 🎉.
  - The player exhausts all 10 attempts.

## How to Play
1. Run the Python script.
2. Enter a **3-digit number** when prompted.
3. Analyze the feedback after each guess to refine your next guess.
4. Continue until you either **guess correctly** or **run out of attempts**.

## Example Interaction
```
Welcome to the Guessing Game!
Try to guess the 3-digit secret number. You have 10 attempts.

Attempt 1/10 - Enter a 3-digit number: 123
❌ 👍 👍

Attempt 2/10 - Enter a 3-digit number: 124
❌ ❌ 👍

Attempt 3/10 - Enter a 3-digit number: 631
👌 👌 👌
🎉 You Got IT! The secret number was: 631
```


## License
This project is free to use and modify for learning and personal use.

## Author
- **Aiman** 

