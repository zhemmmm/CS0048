print("\nSimple Calculator")

def menu():
    print("\nMENU:")
    print(" 1. Add")
    print(" 2. Subtract")
    print(" 3. Multiply")
    print(" 4. Divide")
    print(" 5. Exit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cant divide by zero"
    else:
        return a / b

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            num1 = float(input(" Enter first number: "))
            num2 = float(input(" Enter second number:  "))
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == "2":
            num1 = float(input(" Enter first number: "))
            num2 = float(input(" Enter second number:  "))
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == "3":
            num1 = float(input(" Enter first number: "))
            num2 = float(input(" Enter second number:  "))
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == "4":
            num1 = float(input(" Enter first number: "))
            num2 = float(input(" Enter second number:  "))
            result = divide(num1, num2)
            print(f"Result: {result}")
        elif choice == "5":
            print("Thank you for using the calculator.")
            break
        else:
            print("Invalid Choice. Choose from (1-5) pls.")

main()
