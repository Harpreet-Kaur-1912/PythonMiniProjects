import os

expenses = []

def load_expenses():
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            for line in file:
                name, amount = line.strip().split(',')
                expenses.append((name, float(amount)))
def save_expenses():
    with open('expenses.txt', 'w') as file:
        for name, amount in expenses:
            file.write(f"{name}, {amount}\n")

def show_expenses():
    if not expenses:
        print("No expenses added yet")
    else:
        for index, (name, amount) in enumerate(expenses, start=1):
            print(f"{index}-{name}: {amount}")
        total = sum (amount for _, amount in expenses)
        print(f" Total expenses: {total}")
print (" Welcome to Expense Tracker ")

load_expenses()

while True:
    action = input("What would you like to do?  add, show, delete or exit ").strip().lower()
    if action == "add":
     name = input("What is your expenses? eg. groceries  ")
     try:
         amount=float(input("What is your expenses amount? eg. groceries  "))
         expenses.append((name,amount))
         print("expenses added successfully")
         save_expenses()
     except ValueError:
         print("Enter an Valid input")

    elif action == "show":
     show_expenses()

    elif action == "delete":
        if not expenses:
            print("No expenses added yet")
        else:
            show_expenses()
        try:
            number = int(input(" enter the number of expense to delete:  "))
            if 1 <= number <= len(expenses):
                removed = expenses.pop(number - 1)
                save_expenses()
                print(f"{removed} was removed")
            else:
                print("Enter an Valid input")
        except ValueError:
            print("Enter an Valid input")



    elif action == "exit":
     print("Goodbye")
     break

    else:
     print("Invalid input")





