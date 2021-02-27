# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(Add/Sub/Mul/Div): ")

    # Check if choice is one of the four options
    if choice in ("Add", "Sub", "Mul", "Div"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "Add":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == "Sub":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == "Mul":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == "Div":
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
