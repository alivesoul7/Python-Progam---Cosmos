def save_note():
    note = input("Type a note to save: ")
    with open("notes.txt", "w") as f:
        f.write(note)
    print("Note saved to notes.txt")

def read_file_by_name():
    filename = input("Enter a filename to read: ")
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Sorry, '{filename}' does not exist")

def repeat_note():
    note = input("Type note: ")
    try:
        times = int(input("How many times to repeat: "))
        with open("repeated_notes.txt","w") as f:
            for _ in range(times):
                f.write(note + "\n")
        print("Saved to repeated_notes.txt")

    except ValueError:
        print("Error: Please enter a valid whole number for the repetitions.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    save_note()
    read_file_by_name()
    repeat_note()


if __name__ == "__main__":
    main()