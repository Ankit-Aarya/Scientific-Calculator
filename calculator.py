import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    else:
        return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive values."
    else:
        return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def cube_root(x):
    return math.pow(x, 1/3)

def calculator():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Cube root")
    
    while True:
        choice = input("Enter choice (1-10): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"√{num} = {square_root(num)}")

        elif choice == '7':
            num = float(input("Enter number: "))
            base = input("Enter base (default is 10): ")
            base = float(base) if base else 10
            print(f"log({num}) = {logarithm(num, base)}")

        elif choice in ['8', '9', '10']:
            angle = float(input("Enter angle in degrees: "))
            if choice == '8':
                print(f"sin({angle}) = {sine(angle)}")
            elif choice == '9':
                print(f"cos({angle}) = {cosine(angle)}")
            elif choice == '10':
                print(f"tan({angle}) = {tangent(angle)}")

        elif choice == "11":
            num = float(input("Enter a number: "))
            print(f"{num}^1/3 = {cube_root(num)}")

        else:
            print("Invalid input. Please select a valid option.")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
