def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

print("Select operation:")
print("+")
print("-")
print("×")
print("/")

while True:
    choice = input("Enter choice (+,-,x,/): ")

    if choice in ('+', '-', 'x', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print("Result:", add(num1, num2))
        elif choice == '-':
            print("Result:", subtract(num1, num2))
        elif choice == 'x':
            print("Result:", multiply(num1, num2))
        elif choice == '/':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() == 'no':
        break
    elif next_calculation.lower == 'yes':
        continue
