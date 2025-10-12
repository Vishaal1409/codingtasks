def readTextFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    path = input("Enter the path of the text file: ")
    readTextFile(path)