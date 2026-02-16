def main():
    # create an empty lsit for the activities
    activities = []

    # create another empty list for the finished activities
    activitiesFinished = []

    while True:
        menu()
        choice = input("Choose from the options given above (1-5): ")

        if choice == "1":
            print("The table of activities:")
            print(activities)

        elif choice == "2":
            print("Finished activities:")
            print(activitiesFinished)

        elif choice == "3":
            new_activity = input("Add a new activity")
            activities.append(new_activity)
            print("new activity added")

        elif choice == "4":
            print("activities:")
            print()
            print(activities)
            remove = input("Choose an activity to remove")

            if remove in activities:
                activities.remove(remove)
                print("Activity removed successfully")

            else:
                print("Chosen activity could not be found")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()