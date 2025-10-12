def get_matrix_from_user(rows, cols, name):
    matrix = []
    print(f"\nEnter elements for {name} ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix
def multiply_matrices(matrix1, matrix2):
    """Multiplies two matrices."""
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        print("Error: ")
        return None
    result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))
mat1 = get_matrix_from_user(rows1, cols1, "Matrix 1")
mat2 = get_matrix_from_user(rows2, cols2, "Matrix 2")
result = multiply_matrices(mat1, mat2)
if result:
    print("\nResult of matrix multiplication:")
    for row in result:
        print(row)