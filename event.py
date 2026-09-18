import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="event_management"
)

cursor = db.cursor()

while True:

    print("\n----- EVENT MANAGEMENT SYSTEM -----")
    print("1. Add Event")
    print("2. View Events")
    print("3. Update Event")
    print("4. Delete Event")
    print("5. Add Participant")
    print("6. View Participants")
    print("7. Update Participant")
    print("8. Delete Participant")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    # Add Event
    if choice == 1:

        name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        venue = input("Enter venue: ")
        organizer = input("Enter organizer name: ")

        sql = "insert into events(event_name,event_date,venue,organizer) values(%s,%s,%s,%s)"
        values = (name, date, venue, organizer)

        cursor.execute(sql, values)
        db.commit()

        print("Event added successfully")


    # View Events
    elif choice == 2:

        cursor.execute("select * from events")

        data = cursor.fetchall()

        if len(data) == 0:
            print("No events found")
        else:
            for i in data:
                print("-------------------------")
                print("Event ID    :", i[0])
                print("Event Name  :", i[1])
                print("Event Date  :", i[2])
                print("Venue       :", i[3])
                print("Organizer   :", i[4])


    # Update Event
    elif choice == 3:

        id = int(input("Enter event id: "))

        name = input("Enter new event name: ")
        date = input("Enter new event date (YYYY-MM-DD): ")
        venue = input("Enter new venue: ")
        organizer = input("Enter new organizer: ")

        sql = "update events set event_name=%s,event_date=%s,venue=%s,organizer=%s where event_id=%s"
        values = (name, date, venue, organizer, id)

        cursor.execute(sql, values)
        db.commit()

        print("Event updated successfully")


    # Delete Event
    elif choice == 4:

        id = int(input("Enter event id: "))

        sql = "delete from events where event_id=%s"

        cursor.execute(sql, (id,))
        db.commit()

        print("Event deleted successfully")


    # Add Participant
    elif choice == 5:

        name = input("Enter participant name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        event_id = int(input("Enter event id: "))

        sql = "insert into participants(participant_name,email,phone,event_id) values(%s,%s,%s,%s)"
        values = (name, email, phone, event_id)

        cursor.execute(sql, values)
        db.commit()

        print("Participant added successfully")


    # View Participants
    elif choice == 6:

        cursor.execute("select * from participants")

        data = cursor.fetchall()

        if len(data) == 0:
            print("No participants found")
        else:
            for i in data:
                print("-------------------------")
                print("Participant ID   :", i[0])
                print("Participant Name :", i[1])
                print("Email            :", i[2])
                print("Phone            :", i[3])
                print("Event ID         :", i[4])


    # Update Participant
    elif choice == 7:

        id = int(input("Enter participant id: "))

        name = input("Enter new participant name: ")
        email = input("Enter new email: ")
        phone = input("Enter new phone number: ")
        event_id = int(input("Enter new event id: "))

        sql = "update participants set participant_name=%s,email=%s,phone=%s,event_id=%s where participant_id=%s"
        values = (name, email, phone, event_id, id)

        cursor.execute(sql, values)
        db.commit()

        print("Participant updated successfully")


    # Delete Participant
    elif choice == 8:

        id = int(input("Enter participant id: "))

        sql = "delete from participants where participant_id=%s"

        cursor.execute(sql, (id,))
        db.commit()

        print("Participant deleted successfully")


    # Exit
    elif choice == 9:

        print("Thank you for using Event Management System")
        break


    else:
        print("Invalid choice")


cursor.close()
db.close()