import random

def generate_secret_number():
    return str(random.randint(100, 999))  # Generate a 3-digit random number

def get_feedback(secret, guess):
    feedback = []
    for i in range(3):
        if guess[i] == secret[i]:  
            feedback.append("👌")  # Correct digit in correct place
        elif guess[i] in secret:
            feedback.append("👍")  # Correct digit in wrong place
        else:
            feedback.append("❌")  # No correct digits
    return " ".join(feedback)

def play_game():
    secret_number = generate_secret_number()
    attempts = 10

    print("Welcome to the Guessing Game!")
    print("Try to guess the 3-digit secret number. You have 10 attempts.")

    for attempt in range(1, attempts + 1):
        guess = input(f"\nAttempt {attempt}/{attempts} - Enter a 3-digit number: ")

        if not guess.isdigit() or len(guess) != 3:
            print("Invalid input! Please enter a 3-digit number.")
            continue
        
        feedback = get_feedback(secret_number, guess)
        print(feedback)  

        if guess == secret_number:
            print("🎉 You Got IT! The secret number was:", secret_number)
            return  

    print("\nGame Over! The secret number was:", secret_number)

# Start the game
play_game()
