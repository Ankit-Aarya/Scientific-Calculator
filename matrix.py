def get_matrix(rows, cols):
    """Function to get a matrix from user input."""
    matrix = []
    print(f"Enter the elements of the matrix (row by row):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Error: You must enter {cols} elements for row {i + 1}.")
            return None
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    """Function to multiply two matrices."""
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])
    
    if cols_matrix1 != rows_matrix2:
        print("Error: Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    
    # Matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):  # or k in range(rows_matrix2)
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Main function to run the program
def main():
    # Input for the first matrix
    rows1 = int(input("Enter the number of rows for the first matrix: "))
    cols1 = int(input("Enter the number of columns for the first matrix: "))
    matrix1 = get_matrix(rows1, cols1)

    if matrix1 is None:
        return  # Exit if there was an error in matrix input

    # Input for the second matrix
    rows2 = int(input("Enter the number of rows for the second matrix: "))
    cols2 = int(input("Enter the number of columns for the second matrix: "))
    matrix2 = get_matrix(rows2, cols2)

    if matrix2 is None:
        return  # Exit if there was an error in matrix input

    # Multiply matrices
    result = multiply_matrices(matrix1, matrix2)

    if result is not None:
        print("Result of matrix multiplication:")
        for row in result:
            print(row)

if __name__ == "__main__":
    main()



