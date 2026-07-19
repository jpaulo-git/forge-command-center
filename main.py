import utils as u
from modules.tasks import task_menu   

def main():
# Entry point for the Forge application
# Displays the menu and routes users to each module

    while True:
        try:
            u.clear_screen()

            u.print_header("Forge")
            print()
            print("1. Tasks")
            print("2. Habits (Coming Soon)")
            print("3. Goals (Coming Soon)")
            print("4. Journal (Coming Soon)")
            print("5. Exit")
            print()

            choice = input("Enter your choice: ")

            if choice == "1":
                u.clear_screen()
                task_menu()
            elif choice == "2":
                u.clear_screen()
                print("     === Habits ===")
                print("== Feature Coming Soon ==")
                u.pause()
            elif choice == "3":
                u.clear_screen()
                print("     === Goals ===")
                print("== Feature Coming Soon ==")
                u.pause()
            elif choice == "4":
                u.clear_screen()
                print("     === Journal ===")
                print("== Feature Coming Soon ==")
                u.pause()  
            elif choice == "5":
                u.clear_screen()
                print("Exiting...")
                break
            else:
                u.clear_screen()
                print("Invalid choice. Please try again.")
                u.pause()
    
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()