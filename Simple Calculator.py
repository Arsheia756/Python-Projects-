def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error! Division by zero."

def reminder(n1, n2):
    if n2 != 0:
        return n1 % n2
    else:
        return "Error! Division by zero."

print("=================================================")
print("              WELCOME TO THE                     ")
print("                 SIMPLE                         ")
print("                CALCULATOR                       ")
print("=================================================")

print("Select operation: (+ , - , * , / , %)")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Reminder")
print("6. Exit")

choice = int(input("Enter your choice (1/2/3/4/5/6): "))
if choice == 6:
    print("Exiting the calculator. Thank you!")
else:
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))

    if choice == 1:
        print(f"Result: {add(number1, number2)}")
    elif choice == 2:
        print(f"Result: {subtract(number1, number2)}")
    elif choice == 3:
        print(f"Result: {multiplication(number1, number2)}")
    elif choice == 4:
        print(f"Result: {division(number1, number2)}")
    elif choice == 5:
        print(f"Result: {reminder(number1, number2)}")
    else:
        print("Invalid input...")
