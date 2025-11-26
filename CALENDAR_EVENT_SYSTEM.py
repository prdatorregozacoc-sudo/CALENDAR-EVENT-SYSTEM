import datetime

USER = "admin"
PASS = "1234"

events = {}
event_no = 1

# Validate datetime format
def valid_dt(dt):
    try:
        datetime.datetime.strptime(dt, "%m/%d/%Y %H-%M-%S")
        return True
    except:
        return False

# LOGIN FUNCTION
def login():
    while True:
        print("===== CALENDAR EVENT SYSTEM ====")
        print("============ LOGIN =============")
        username = input("Username: ")
        password = input("Password: ")
        if username == USER and password == PASS:
            print("\nLogged in successfully!\n")
            break
        else:
            print("\nUsername or Password is Incorrect!\n")

# INITIAL LOGIN
login()

# MENU LOOP
while True:
    print("==== MENU ====")
    print("1. Add Event")
    print("2. View Events")
    print("3. Edit Event")
    print("4. Delete Event")
    print("5. Log Out")
    print("6. Exit")

    choice = input("\nChoice: ")

    # ADD EVENT
    if choice == "1":
        print("\n==== Add Event ====")
        title = input("Enter Event Title: ")

        # DATE LOOP WITH FUTURE DATE CHECK
        while True:
            dt = input("Enter Event Date & Time (MM/DD/YYYY HH-MM-SS): ")
            if not valid_dt(dt):
                print("\nDate & Time Format is Incorrect! Try again.\n")
                continue
            event_time = datetime.datetime.strptime(dt, "%m/%d/%Y %H-%M-%S")
            if event_time <= datetime.datetime.now():
                print("\nDate & Time cannot be in the past! Enter a future date.\n")
                continue
            break

        people = input("Enter People in this Event: ")
        description = input("Enter Event Description: ")

        events[event_no] = {
            "title": title,
            "datetime": dt,
            "people": people,
            "description": description
        }
        event_no += 1
        print("\nEvent Added Successfully!\n")

    # VIEW EVENTS
    elif choice == "2":
        if not events:
            print("\nNo events.\n")
            continue

        print("\n==== View Events ====\n")
        for n, e in events.items():
            print(f"Event #{n}")
            print(f"Title: {e['title']}")
            print(f"Date & Time: {e['datetime']}")
            print(f"People: {e['people']}")
            print(f"Description: {e['description']}\n")

    # EDIT EVENT
    elif choice == "3":
        if not events:
            print("\nNo events to edit.\n")
            continue
        while True:
            print("\n==== EDIT EVENT ====")
            for n, e in events.items():
                print(f"\nEvent #{n}")
                print(f"Title: {e['title']}")
                print(f"Date & Time: {e['datetime']}")
                print(f"People: {e['people']}")
                print(f"Description: {e['description']}")
            event_number = input("\nEnter Event # to Edit: ")
            if event_number.isdigit() and int(event_number) in events:
                event_number = int(event_number)
                e = events[event_number]

                e["title"] = input("New Event Title: ")

                # NEW DATE LOOP WITH FUTURE CHECK
                while True:
                    new_dt = input("New Date & Time (MM/DD/YYYY HH-MM-SS): ")
                    if not valid_dt(new_dt):
                        print("Date & Time Format is Incorrect! Try again.\n")
                        continue
                    new_time = datetime.datetime.strptime(new_dt, "%m/%d/%Y %H-%M-%S")
                    if new_time <= datetime.datetime.now():
                        print("Date & Time cannot be in the past! Enter a future date.\n")
                        continue
                    e["datetime"] = new_dt
                    break

                e["people"] = input("Enter New People in this Event: ")
                e["description"] = input("Enter New Event Description: ")

                print(f"\nEvent #{event_number} Updated Successfully!\n")
                break
            else:
                print("\nEvent # doesn't exist. Try again.\n")

    # DELETE EVENT
    elif choice == "4":
        if not events:
            print("\nNo events to delete.\n")
            continue
        while True:
            print("\n==== DELETE EVENT ====")
            for n, e in events.items():
                print(f"\nEvent #{n}")
                print(f"Title: {e['title']}")
                print(f"Date & Time: {e['datetime']}")
                print(f"People: {e['people']}")
                print(f"Description: {e['description']}")
            event_number = input("\nEnter Event # to Delete: ")
            if event_number.isdigit() and int(event_number) in events:
                event_number = int(event_number)
                break
            print("\nEvent # doesn't exist. Try Again.\n")
        confirm = input("Delete event? Yes or No: ").lower()
        if confirm == "yes":
            del events[event_number]
            print("\nEvent Deleted Successfully!\n")
            # REORDER EVENTS
            new_events = {}
            new_num = 1
            for key in sorted(events.keys()):
                new_events[new_num] = events[key]
                new_num += 1
            events = new_events
            event_no = new_num
        else:
            print("\nEvent Deletion Cancelled.\n")

    # LOG OUT
    elif choice == "5":
        print("\nLogging out...\n")
        login()

    # EXIT
    elif choice == "6":
        print("\n===== Goodbye! =====\n")
        break

    else:
        print("\nInvalid Input.\n")
