from datetime import datetime, date, timedelta

# =========================
# CONSTANTS
# =========================

GD = "GD"
SPECIALIST = "Specialist"

BASE_FEE = 100
LAB_TEST_RATE = 10


# =========================
# PATIENT REGISTRATION
# =========================

def register_patient():
    print("\n===== PATIENT REGISTRATION =====")

    while True:
        Name = input("Name: ")

        try:
            Age = int(input("Age: "))
        except ValueError:
            Age = 0

        ID = input("ID: ")

        if Name != "" and Age > 0 and ID != "":
            break

        print("Error: Please enter valid information.")

    print("\nPatient Information:")
    print("Name:", Name)
    print("Age:", Age)
    print("ID:", ID)

    print("Patient registered successfully.")

    return Name, Age, ID


# =========================
# APPOINTMENT BOOKING
# =========================

def book_appointment():
    print("\n===== APPOINTMENT BOOKING =====")

    # Get department
    staff_department = input(
        "Please input your department (GD/Specialist): "
    )

    while staff_department not in (GD, SPECIALIST):
        print("Error, please retry.")
        staff_department = input(
            "Please input your department (GD/Specialist): "
        )

    # Get appointment date
    appointment_input = input(
        "Please input the appointment date (YYYY-MM-DD): "
    )

    while True:
        try:
            appointment_date = datetime.strptime(
                appointment_input, "%Y-%m-%d"
            ).date()

            current_date = date.today()

            if (
                appointment_date < current_date
                or appointment_date > current_date + timedelta(days=7)
            ):
                print("Error, please enter a date within the next 7 days.")
                appointment_input = input(
                    "Please enter appointment date (YYYY-MM-DD): "
                )
            else:
                break

        except ValueError:
            print("Error, please use YYYY-MM-DD format.")
            appointment_input = input(
                "Please enter appointment date (YYYY-MM-DD): "
            )

    # Confirm booking
    confirmation = input(
        "Confirm booking (Y/N): "
    ).upper()

    while confirmation not in ("Y", "N"):
        print("Please enter Y or N.")
        confirmation = input(
            "Confirm booking (Y/N): "
        ).upper()

    if confirmation == "Y":
        print("Booking confirmed!")
        return staff_department, appointment_date
    else:
        print("Booking cancelled.")
        return None, None


# =========================
# CALCULATE BILLING
# =========================

def calculate_total(number_of_lab_tests, patient_type):
    subtotal = BASE_FEE + (
        number_of_lab_tests * LAB_TEST_RATE
    )

    if patient_type == "Subsidised":
        total = subtotal * 0.70
    else:
        total = subtotal

    return total


def calculate_billing():
    print("\n===== LAB TEST BILLING =====")

    patient_type = input(
        "Enter patient type (Subsidised/Private): "
    )

    while patient_type not in ("Subsidised", "Private"):
        print("Invalid option, please re-enter.")
        patient_type = input(
            "Enter patient type (Subsidised/Private): "
        )

    while True:
        try:
            number_of_lab_tests = int(
                input("Enter number of lab tests: ")
            )

            if number_of_lab_tests >= 0:
                break
            else:
                print("Invalid number. Please enter 0 or more.")

        except ValueError:
            print("Invalid number. Please enter a whole number.")

    total = calculate_total(
        number_of_lab_tests,
        patient_type
    )

    print("\n===== BILLING SUMMARY =====")
    print("Patient Type:", patient_type)
    print("Number of Lab Tests:", number_of_lab_tests)
    print("Total: $", format(total, ".2f"))

    return patient_type, number_of_lab_tests, total


# =========================
# TRIAGE
# =========================

def assign_triage_room():
    print("\n===== TRIAGE ASSESSMENT =====")

    while True:
        try:
            severity = int(
                input("Enter severity of condition (1-10): ")
            )

            if 1 <= severity <= 10:
                break
            else:
                print(
                    "Error: Please enter a whole number "
                    "between 1 and 10."
                )

        except ValueError:
            print(
                "Error: Please enter a whole number "
                "between 1 and 10."
            )

    if 1 <= severity <= 4:
        assigned_room = "Waiting Room"
    elif 5 <= severity <= 7:
        assigned_room = "Room 1"
    else:
        assigned_room = "Room 2"

    print("\n===== TRIAGE SUMMARY =====")
    print("Severity Level:", severity)
    print("Assigned Room:", assigned_room)

    return severity, assigned_room


# =========================
# MAIN MENU
# =========================

def main():
    # Variables to store patient information
    Name = ""
    Age = 0
    ID = ""

    while True:
        print("\n")
        print("===================================")
        print("       PATIENT MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Register Patient")
        print("2. Book Appointment")
        print("3. Calculate Billing")
        print("4. Assign Triage Room")
        print("5. Exit")
        print("===================================")

        choice = input("Please select an option: ")

        # Option 1 - Register Patient
        if choice == "1":
            Name, Age, ID = register_patient()

        # Option 2 - Book Appointment
        elif choice == "2":
            if Name == "":
                print("\nPlease register the patient first.")
            else:
                book_appointment()

        # Option 3 - Calculate Billing
        elif choice == "3":
            if Name == "":
                print("\nPlease register the patient first.")
            else:
                calculate_billing()

        # Option 4 - Triage
        elif choice == "4":
            if Name == "":
                print("\nPlease register the patient first.")
            else:
                assign_triage_room()

        # Option 5 - Exit
        elif choice == "5":
            print("\nThank you for using the Patient Management System.")
            print("Goodbye!")
            break

        # Invalid menu option
        else:
            print("\nInvalid option. Please select 1-5.")


# =========================
# START PROGRAM
# =========================

main()