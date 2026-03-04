import json

def menu():
    print("\n===== MAIN MENU =====")

activities = []
activitiesFinished = []

print("Good day, user! This program allows you to store all the acivities that you have in a list.\nWhen you have your list, you can choose to view the list of all your pending and finished activities,\nadd and remove activities, or exit the program.")

try:
    with open("activities.json", "r") as f:
        data = json.load(f)

    activities = data['activities']
    activitiesFinished = data["finishedActivities"]

    while True:

        for activity in data:
            if activity == data["activities"]:
                activityToDO = activity
            elif activity == data["finishedActivities"]:
                activityDone = activity

        #MAIN MENU
        menu()
        print("1 - List of Activities")
        print("2 - Finished Activities")
        print("3 - Add a New Activity")
        print("4 - Remove an Activity")
        print("5 - Exit")

        choice = input("Choose from the options given above (1-5): ")
        print()

        # Print out the current activities in the list
        if choice == "1":
            print("List of Activities:")
            if not activities:
                print("No activities found.")
            else:
                for activity in activities:
                    print(activity)

        # Print out the activities that are finished
        elif choice == "2":
            print("Finished Activities:")
            if not activitiesFinished:
                print("No finished activities.")
            else:
                for activity in activitiesFinished:
                    print(activity)

        # Add a new activity to the list
        elif choice == "3":
            new_activity = input("Add a new activity: ")
            activities.append(new_activity)

            with open("activities.json", 'w') as file:
                json.dump(data, file, indent=4)

            print("New activity added.")

        # Remove an activity from the list
        elif choice == "4":
            print("Activities:")

            if not activities:
                print("No activities to remove.")
            else:
                for activity in activities:
                    print(activity)

            remove = input("Choose an activity to remove: ")

            if remove in activities:
                activities.remove(remove)
                print("Activity removed successfully.")
            else:
                print("Activity could not be found.")

        # End the program
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")