import os

filename = "data.txt"

def create_file():
    content = input("Enter content for the file: ")
    with open(filename, "w") as file:
        file.write(content)
    print("File created successfully.")

def read_file():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print("File content:\n" + file.read())
    else:
        print("File does not exist.")

def append_to_file():
    if os.path.exists(filename):
        content = input("Enter content to append: ")
        with open(filename, "a") as file:
            file.write(content)
        print("Content appended successfully.")
    else:
        print("File does not exist.")

def delete_file():
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

def menu():
    print("\n--- File Manager ---")
    print("1. Create a File")
    print("2. Read File Content")
    print("3. Append Content")
    print("4. Delete File")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        create_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        append_to_file()
    elif choice == "4":
        delete_file()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
