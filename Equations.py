import numpy as np
import sympy as sp

def get_matrix(size):
    """Function to get a square matrix from user input."""
    matrix = []
    print(f"Enter the elements of the {size}x{size} matrix (row by row):")
    for i in range(size):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != size:
            print(f"Error: You must enter {size} elements for row {i + 1}.")
            return None
        matrix.append(row)
    return np.array(matrix)

def calculate_determinant():
    """Function to calculate the determinant of a matrix."""
    size = int(input("Enter the size of the square matrix (e.g., 2 for 2x2): "))
    matrix = get_matrix(size)

    if matrix is None:
        return  # Exit if there was an error in matrix input

    det = np.linalg.det(matrix)
    print(f"Determinant of the matrix is: {det}")

def solve_quadratic():
    """Function to solve a quadratic equation of the form ax^2 + bx + c = 0."""
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        return

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        print(f"The roots are real and different: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The root is real and repeated: {root}")
    else:
        real_part = -b / (2*a)
        imaginary_part = np.sqrt(-discriminant) / (2*a)
        print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

def solve_cubic():
    """Function to solve a cubic equation of the form ax^3 + bx^2 + cx + d = 0."""
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))

    if a == 0:
        print("Coefficient 'a' cannot be zero for a cubic equation.")
        return

    # Using sympy to solve the cubic equation
    x = sp.symbols('x')
    cubic_eq = a * x**3 + b * x**2 + c * x + d
    solutions = sp.solve(cubic_eq, x)
    
    print("The solutions to the cubic equation are:")
    for sol in solutions:
        print(sol)

def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Calculate Determinant of a Matrix")
        print("2. Solve Quadratic Equation")
        print("3. Solve Cubic Equation")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculate_determinant()
        elif choice == '2':
            solve_quadratic()
        elif choice == '3':
            solve_cubic()
        elif choice == '4':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid input. Please select a valid option.")

if __name__ == "__main__":
    main()
