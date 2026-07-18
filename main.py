from utils import print_header  

def main():
    while True:
        try:
            print_header("Forge")
            print()
            print()
            print("1. Tasks")
            print("2. Habits (Coming Soon)")
            print("3. Goals (Coming Soon)")
            print("4. Journal (Coming Soon)")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                pass
            elif choice == "2":
                print("Habits Coming soon...")
                break
            elif choice == "3":
                print("Goals Coming soon...")
                break
            elif choice == "4":
                print("Journal Coming soon...")
                break   
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()