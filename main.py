# main.py
from manifest import AircraftManifest

def display_menu():
    print("""
    *** TUFFY TITAN AIRCRAFT MANIFEST

    1. Print Seating Chart
    2. Print Passenger Manifest
    3. Purchase Ticket
    4. Cancel Ticket
    5. Check In
    6. Check Bags
    7. Board Aircraft
    8. Exit
    """)

def print_seating_chart(manifest):
    # Display the seating chart based on the provided manifest
    rows = 9
    cols = 3
    seats = [["-" for _ in range(cols)] for _ in range(rows)]

    for passenger in manifest:
        seat = passenger[0]
        if not any(char.isdigit() for char in seat):
            continue
        row = int(seat[:-1]) - 1
        col = ord(seat[-1].upper()) - 65
        seats[row][col] = "x"

    print("** SEATING CHART **")
    print("     A  B  C")
    print("    =======")
    for i, row in enumerate(seats, start=1):
        print(f"{i} | {'  '.join(row)}")

def print_passenger_manifest(manifest):
    # Display the passenger manifest based on the provided manifest
    print("** PASSENGER MANIFEST **")
    print("Last Name   First Name   Seat   Checked-In   No. Bags   Boarded")
    print("=" * 65)
    for passenger in manifest:
        last_name = passenger[2]
        first_name = passenger[1]
        seat = passenger[0]
        checked_in = "Yes" if passenger[3] else ""
        bags = passenger[4] if passenger[4] != 0 else ""
        boarded = "Yes" if passenger[5] else ""
        print(f"{last_name.ljust(11)}   {first_name.ljust(11)}   {seat.center(4)}   {checked_in.center(11)}   {str(bags).center(9)}   {boarded.center(7)}")

def main():
    initial_manifest_data = [
        # Provided initial data to be added here
    ]

    aircraft = AircraftManifest(initial_manifest_data)

    while True:
        display_menu()
        choice = input("Enter menu choice: ")

        if choice == '1':
            print_seating_chart(aircraft.manifest)
        elif choice == '2':
            print_passenger_manifest(aircraft.manifest)
        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            seat = input("Enter seat: ")
            success = aircraft.purchase_ticket(first_name, last_name, seat)
            if success:
                print("Success")
            else:
                print("Fail")
        elif choice == '4':
            seat = input("Enter seat: ")
            success = aircraft.cancel_ticket(seat)
            if success:
                print("Success")
            else:
                print("Fail")
        elif choice == '5':
            seat = input("Enter seat: ")
            success = aircraft.check_in(seat)
            if success:
                print("Success")
            else:
                print("Fail")
        elif choice == '6':
            seat = input("Enter seat: ")
            no_bags = int(input("Number of bags: "))
            success = aircraft.check_bags(seat, no_bags)
            if success:
                print("Success")
            else:
                print("Fail")
        elif choice == '7':
            seat = input("Enter seat: ")
            success = aircraft.board_aircraft(seat)
            if success:
                print("Success")
            else:
                print("Fail")
        elif choice == '8':
            filename = 'aircraft_manifest.json'
            aircraft.save_to_json(filename)
            print("Data saved to", filename)
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
