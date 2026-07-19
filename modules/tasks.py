import utils as u

def task_menu():
    while True:
        u.clear_screen()

        u.print_header("Tasks")
        print()
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Back")
        print()

        choice = input("What would you like to do? ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            u.clear_screen()
            return
        else:
            u.clear_screen()
            print("Invalid choice. Please try again.")
            u.pause()

def add_task():
    u.clear_screen()
    print("    === Add Task ===")
    print("== Feature Coming Soon ==")
    u.pause()
    
def delete_task():
    u.clear_screen()
    print("   === Delete Task ===")
    print("== Feature Coming Soon ==")
    u.pause()

def complete_task():
    u.clear_screen()
    print("  === Complete Task ===")
    print("== Feature Coming Soon ==")
    u.pause()

def view_tasks():
    u.clear_screen()
    print("   === View Tasks ===")
    print("== Feature Coming Soon ==")
    u.pause()


