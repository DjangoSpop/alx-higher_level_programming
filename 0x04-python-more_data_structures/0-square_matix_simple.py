#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    # Create a new matrix to store the squared values
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Iterate through the input matrix and compute the square of each element
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix

# Example usage:
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(input_matrix)
for row in result:
    print(row)

