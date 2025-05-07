def menu():
    print("\nMenu:")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")

    choice_str = input("Enter your choice (1-3): ")

scores = []

while True:
    choice_str = menu()

    if not choice_str.isdigit():
        print("Invalid input. Please enter a number between 1 and 3.")
        continue

    choice = int(choice_str)

    if choice == 3:
        print("Exiting the program.")
        break

    if choice == 1:
        subject = input("Enter the subject name: ")
        while True:
          score_str = input("Enter the score: ")
          if not score_str.isdigit():
              print("Invalid input. Please enter a valid number for the score.")
              continue
          score = int(score_str)
          scores.append(score)
          break
    elif choice == 2:
        if not scores:
            print("No scores added yet.")
        else:
            average = sum(scores) / len(scores)
            print("Average score:", average)
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
