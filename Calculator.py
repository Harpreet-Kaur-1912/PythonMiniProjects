def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

while True:
    user_action = input("\nChoose an operation (add, subtract, multiply, divide) or type 'exit' to quit: ").lower()

    if user_action == "exit" or user_action == "quit":
        print("Goodbye! 👋")
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if user_action == "add":
        print("Result:", add(x, y))
    elif user_action == "subtract":
        print("Result:", subtract(x, y))
    elif user_action == "multiply":
        print("Result:", multiply(x, y))
    elif user_action == "divide":
        print("Result:", divide(x, y))
    else:
        print("Invalid operation. Please try again.")
