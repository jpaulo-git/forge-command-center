import os

def print_header(title):
    # Prints a header with the given title
    print("\n========================")
    print(f"         {title}")
    print("========================")

def clear_screen():
    # Clears the screen
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    # Pauses the screen
    input("\nPress Enter to continue...")