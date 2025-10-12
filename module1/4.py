def create_matrix_and_get_value():
    try:
        n = int(input("Enter the value of n (for n x n matrix): "))
        print(f"Enter {n*n} elements row by row:")
        matrix = []
        for i in range(n):
            row = list(map(int, input(f"Enter {n} elements for row {i+1}: ").split()))
            if len(row) != n:
                print("Error: Each row must have exactly n elements.")
                return
            matrix.append(row)
        print("\nMatrix:")
        for row in matrix:
            print(row)
        i = int(input(f"\nEnter row index i (0 to {n-1}): "))
        j = int(input(f"Enter column index j (0 to {n-1}): "))
        print(f"\nValue at position ({i},{j}) = {matrix[i][j]}")
    except ValueError:
        print("Invalid input! Please enter integers only.")
    except IndexError:
        print("Index out of range! Please enter valid indices.")
    except Exception as e:
        print("An unexpected error occurred:", e)
if __name__ == "__main__":
    create_matrix_and_get_value()