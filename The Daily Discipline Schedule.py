def menu ():
    print("\n == Main Menu ==")
    print("1. The table of activities")
    print("2. Finished activities")
    print("3. Add a new activity to the list")
    print("4. Remove an activity from the list")
    print("5. Exit the program")
    print("="*10)


def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            print("Show a table of activities")
        elif choice == "2":
            print("Show finished activities")
        elif choice == "3":
            print("Add new activity")
        elif choice == "4":
            print("Remove activity")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()