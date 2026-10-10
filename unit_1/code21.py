import random

target_number = random.randint(1, 100)
guess = 0

print("I have selected a number between 1 and 100. Try to guess it!")

while guess != target_number:
    guess = int(input("Enter your guess: "))
    
    if guess > target_number:
        print("Too high! Try again.")
    elif guess < target_number:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

