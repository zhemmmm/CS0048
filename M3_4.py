import random

def menu():
    print("\nMenu")
    print("1. Play Number Guessing Game")
    print("2. Exit")

    choice_str = input("Enter your choice (1-2): ")

while True:
    choice_str = menu()

    if not choice_str.isdigit():
        print("Invalid input. Please enter a number between 1 and 2.")
        continue

    choice = int(choice_str)

    if choice == 2:
        print("Exiting the program.")
        break
    elif choice == 1:
        number = random.randint(1, 100)
        attempts = 0
        while True:
            
            guess_str = input("Guess a number between 1 and 100: ")
            guess = int(guess_str)
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 2.")
