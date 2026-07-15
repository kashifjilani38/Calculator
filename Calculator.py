print("===== SIMPLE CALCULATOR =====")

# Enter first two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Enter first operator
operator = input("Enter operator (+, -, *, /): ")

# Perform first calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
        exit()
    result = num1 / num2
else:
    print("Invalid operator!")
    exit()

print(f"{num1} {operator} {num2} = {result}")

# Continue calculations
while True:
    operator = input(
        "\nEnter operator (+, -, *, /) to continue or any other key to exit: "
    )

    if operator not in ["+", "-", "*", "/"]:
        print("Calculator Closed.")
        break

    try:
        number = float(input("Enter next number: "))

        previous = result

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number
        elif operator == "*":
            result *= number
        elif operator == "/":
            if number == 0:
                print("Error! Division by zero is not allowed.")
                continue
            result /= number

        print(f"{previous} {operator} {number} = {result}")

    except ValueError:
        print("Invalid number! Try again.")