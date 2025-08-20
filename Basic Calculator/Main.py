# Basic Calculator

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Available operations: +, -, *, /")

    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Invalid operator! Please try again.")
            continue

        print("Result:", result)

        choice = input("Do you want to calculate again? (yes/no): ").lower()
        if choice != "yes":
            print("Goodbye!")
            break


# Start the calculator
calculator()
