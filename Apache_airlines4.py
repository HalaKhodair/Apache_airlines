#importing a module to generate random booking refrences 
import random
#importing a module to access uppercase letters and digits 
import string
#tracking all used booking references to ensure uniqueness
booking_references = set()
#creating a passenger database as a list of dictionaries
passenger_database = []
#defining a function that generates 8 unique characters for booking reference 
def generate_booking_reference():
    while True:
#generating 8 random character if upper case strings 
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
#using the if statement to ensure that the booking reference has not been used yet to add it in the list
        if reference not in booking_references:
            booking_references.add(reference)
            return reference
#defining a function to initialising the airplane seating layout
def apache_airlines():
#creating a list for the seats with 80 rows and 6 columns, where F represents free seats
    airplane = [['F' for _ in range(6)] for _ in range(80)]
#using the for loop to set the 4th column in each row to X, where it represents aisles 
    for row in range(80):
        airplane[row][3] = 'X'  
#using the for loop to set the 5th and 6th column of row 39 and 40 to S, where it represents storage 
    for row in [39, 40]:  
        airplane[row][4] = 'S'  
        airplane[row][5] = 'S' 
    return airplane
#storing the airplane layout using a golbal variable
airplane = apache_airlines()
#defining a function that checks the seat availability 
def check_availability():
    try:
#asking the user to input the seat number and letter
        seat = input("Enter seat to check, (#letter): ").upper()
#converting the seat's number part to a zero-based row index
        row = int(seat[:-1]) - 1
#convert the seat's letter part to a column index
        col = ord(seat[-1]) - ord('A')
##using the if statement to check if the input is within the range        
        if not (0 <= row < 80 and 0 <= col < 6):
            print("Invalid seat")
            return
#getting the seat condition and printing a message to check availability
        status = airplane[row][col]
        if status == 'F':
            print(f"Seat {seat} is available")
        elif status == 'R':
            print(f"Seat {seat} has already been booked")
        elif status == 'X':
            print(f"Seat {seat} is an aisle and cannot be booked.")
        elif status == 'S':
            print(f"Seat {seat} is a storage area and cannot be booked.")
    except:
        print("Invalid input, use format like '1A'.")
#defining a function to book a seat
def book_seat():
    try:
#asking a user to input the seat they want to book
        seat = input("Enter seat to book (#letter): ").upper()
#converting the seat's number part to a zero-based row index
        row = int(seat[:-1]) - 1
#convert the seat's letter part to a column index
        col = ord(seat[-1]) - ord('A')
#checking if the row and column are valid
        if not (0 <= row < 80 and 0 <= col < 6):
            print("Invalid seat")
            return
#generating a booking reference if seat is free to book
        if airplane[row][col] == 'F':
            booking_ref = generate_booking_reference()
#collecting passenger details
            passport = input("Enter passport number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
#adding the passenger's data to the database 
            passenger_database.append({
                "BookingRef": booking_ref,
                "Passport": passport,
                "FirstName": first_name,
                "LastName": last_name,
                "SeatRow": row + 1,
                "SeatCol": chr(col + ord('A'))})
#updating seat with booking reference
            airplane[row][col] = booking_ref
            print(f"Seat {seat} booked successfully. Booking reference: {booking_ref}")
        else:
            print("Seat unavailable.")
    except:
        print("Invalid input format.")
#defining a function that frees a seat when it is booked 
def free_seat():
    try:
#asking the user to inout a seat to free 
        seat = input("Enter seat to free (#letter): ").upper()
#converting the seat's number part to a zero-based row index
        row = int(seat[:-1]) - 1
#convert the seat's letter part to a column index
        col = ord(seat[-1]) - ord('A')
#getting the current seat value 
        current = airplane[row][col]
#checking if the seat is available by using the if statement 
        if current not in ['F', 'X', 'S']:  # If seat is booked (not free or aisle or storage)
            airplane[row][col] = 'F'
#removing the passenger details from database
            for passenger in passenger_database:
                if passenger["SeatRow"] == row + 1 and passenger["SeatCol"] == chr(col + ord('A')):
                    passenger_database.remove(passenger)
                    break
#removing the booking refrence after seat has been freed 
            booking_references.discard(current)
            print(f"Seat {seat} has been freed and booking data removed.")
        else:
            print(f"Seat {seat} is not currently booked.")
    except ValueError:
        print("Invalid input format. Please use a valid seat format like '1A'.")
#defining a program that shows the current seating status
def show_status():
    print("Seat Status:")
#printing headings for the columns and a separator line
    print("     A B C   D E F")
    print("     " + "-" * 19)
#using a for loop to iterate through each row and displaying the seat status 
#using enumerate function to get the index and the seating data for each row in the list
    for i, row in enumerate(airplane):
#joining the first 3 seats and the last 3 seats for better display
        row_display = ' '.join(row[:3]) + '   ' + ' '.join(row[3:])
        print(f"{i+1:3} | {row_display}")
    
#defining a function that prints a seat summary    
def seat_summary(airplane):
#initialising each counter 
    free = 0
    booked = 0
#using the for loop to iterate through each seat in each row 
    for row in airplane:
        for seat in row:
            if seat == 'F':
                free += 1
            elif seat == 'R':
                booked += 1
#printing the seat summary
    print(f"Free seats: {free}")
    print(f"Booked seats: {booked}")
#defining a function that displays the full seat layout 
def display_seat_layout():
    print(" Seat Layout :")
#using the for loop to iterate through the 80 rows
    for i in range(80):  
        row_str = f"Row {i+1:3}: "
        for seat in airplane[i]:
            if seat == 'F':
                row_str += '[F] '
            elif seat == 'X':
                row_str += '[X] '
            elif seat == 'S':
                row_str += '[S] '
            else:
                row_str += '[R] '  
        print(row_str)
    print()
#defining a function that shows all the booked passenger's data
def display_passenger_data():
    if not passenger_database:
        print("No passengers booked yet.")
        return
    print("Passenger Database:")
    for passenger in passenger_database:
        print(f"{passenger['BookingRef']}: {passenger['FirstName']} {passenger['LastName']} - Seat {passenger['SeatRow']}{passenger['SeatCol']}, Passport: {passenger['Passport']}")
    print()
#defining a function that confirms exit from the booking system 
def confirm_exit():
    while True:
#asking the user if they want to exit the program and saving their data 
        choice = input("Are you sure you want to exit? (Y/N): ").upper()
        if choice == 'Y':
            save = input("Save data before exiting? (Y/N): ").upper()
            if save == 'Y':
                print("Data saved successfully.")
            return True
        elif choice == 'N':
            return False
        else:
            print("Please enter Y or N.")
#defining a function that runs the seat booking system 
def main():
#asking the user to choose an option
    while True:
        print("====== APACHE AIRLINES BOOKING SYSTEM ======")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking status")
        print("5. Display seat layout")
        print("6. Seat Summary")
        print("7. Show passenger database")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            check_availability()
        elif choice == '2':
            book_seat()
        elif choice == '3':
            free_seat()
        elif choice == '4':
            show_status()
        elif choice == '5':
            display_seat_layout()
        elif choice == '6':
            seat_summary(airplane)
        elif choice == '7':
            display_passenger_data()
        elif choice == '8':
            if confirm_exit():
                print("Thank you for using Apache Airlines Booking System. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")
#running the main function to start the Apache airlines booking system 
if __name__ == "__main__":
    main()
