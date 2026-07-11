# Import the random module to generate random numbers
import random

# Generate a random number between 1 and 20
number = random.randint(1, 20)

# Counter for number of attempts
tries = 0

# Game introduction
print("🎲 Guessing Game 🎲")
print("I've picked a number between 1 and 20 😏")
print("If you lose, you're a clown!\n")

# Main game loop
while True:
    # Get user input
    guess = input("What's your guess? (or q to quit): ")

    # Check if user wants to quit
    if guess.lower() == "q":
        print("🏃‍♂️ You ran away?! Fine 😆")
        break

    # Validate that input is a number
    if not guess.isdigit():
        print("❌ Enter a number, genius!")
        continue

    # Convert input to integer
    guess = int(guess)
    tries += 1  # Increment attempt counter

    # Check if guess is too low, too high, or correct
    if guess < number:
        print("📉 Too low! Go higher")
    elif guess > number:
        print("📈 Too high! Go lower")
    else:
        # Correct guess!
        print(f"🎉 Well done! You got it in {tries} tries")
        break

    # Funny messages based on number of attempts
    if tries == 3:
        print("Come on, are you even trying?!")
    elif tries == 5:
        print("😂 Seriously? Still trying?")
    elif tries == 7:
        print("Bro, just give up before I come over there")

# Pause before exiting
input("\nPress Enter to exit")
