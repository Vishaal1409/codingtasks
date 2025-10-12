import csv
def find_ai_in_csv(file_path):
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row_idx, row in enumerate(reader):
                for col_idx, cell in enumerate(row):
                    if 'ai' in cell.lower():  # check for 'ai' in any cell
                        results.append((row_idx, col_idx, cell))
        return results
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied while reading file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
if __name__ == "__main__":
    path = input("Enter the CSV file path: ")
    matches = find_ai_in_csv(path)

    if matches:
        print("\nCells containing 'ai':")
        for row, col, value in matches:
            print(f"Row {row}, Column {col}: {value}")
    else:
        print("\nNo cells with 'ai' found in the file.")