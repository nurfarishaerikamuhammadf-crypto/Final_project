from datetime import datetime, date, timedelta


# =========================================================
# 1. PATIENT REGISTRATION
# =========================================================

print("Enter patient's basic details")

Name = input("Name: ")
Age = int(input("Age: "))
ID = input("ID: ")

while Name == "" or Age <= 0 or ID == "":
    print("Error: Please enter valid information.")

    print("Enter patient's basic details")
    Name = input("Name: ")
    Age = int(input("Age: "))
    ID = input("ID: ")

print("\nPatient Information:")
print("Name:", Name)
print("Age:", Age)
print("ID:", ID)
print("Patient registered successfully.")


# =========================================================
# 2. DEPARTMENT AND APPOINTMENT DATE
# =========================================================

GD = "GD"
SPECIALIST = "Specialist"

print("\nPlease input your department:")
staff_department = input()

while staff_department not in (GD, SPECIALIST):
    print("Error, please retry")
    staff_department = input()

print("Please input the appointment date (YYYY-MM-DD):")
appointment_input = input()

while True:
    try:
        appointment_date = datetime.strptime(
            appointment_input, "%Y-%m-%d"
        ).date()

        current_date = date.today()

        if appointment_date < current_date + timedelta(days=7):
            print("Error, please retry")
            appointment_input = input()
        else:
            break

    except ValueError:
        print("Error, please retry")
        appointment_input = input()


# =========================================================
# 3. CONFIRM BOOKING
# =========================================================

print("\nConfirm booking (Y/N):")
confirmation = input().upper()

while confirmation not in ("Y", "N"):
    print("Please enter Y or N:")
    confirmation = input().upper()

if confirmation == "Y":
    print("Booking confirmed")
else:
    print("Booking cancelled")


# =========================================================
# 4. CALCULATE LAB TEST TOTAL
# =========================================================

BASE_FEE = 100
LAB_TEST_RATE = 10


def calculate_total(number_of_lab_tests, patient_type):

    subtotal = BASE_FEE + (number_of_lab_tests * LAB_TEST_RATE)

    if patient_type == "Subsidised":
        total = subtotal * 0.70
    else:
        total = subtotal

    return total


# Input patient type
print("\nEnter patient type (Subsidised / Private):")
patient_type = input()

while patient_type not in ("Subsidised", "Private"):
    print("Invalid option, please re-enter")
    patient_type = input()

# Input number of lab tests
number_of_lab_tests = float(
    input("Enter number of lab tests: ")
)

while number_of_lab_tests <= 0 or number_of_lab_tests % 1 != 0:
    print("Invalid number, please re-enter a valid number")
    number_of_lab_tests = float(
        input("Enter number of lab tests: ")
    )

# Calculate total
total = calculate_total(
    int(number_of_lab_tests),
    patient_type
)

print("\nPatient Type:", patient_type)
print("Total: $", format(total, ".2f"))


# =========================================================
# 5. TRIAGE ROOM ASSIGNMENT
# =========================================================

print("\nEnter severity of condition (1-10):")
severity_input = input()

while True:

    try:
        severity = int(severity_input)

        if 1 <= severity <= 10:
            break
        else:
            print("Error: Please enter a whole number between 1 and 10.")
            severity_input = input()

    except ValueError:
        print("Error: Please enter a whole number between 1 and 10.")
        severity_input = input()


# Assign room based on severity
if 1 <= severity <= 4:
    assigned_room = "Waiting Room"

elif 5 <= severity <= 7:
    assigned_room = "Room 1"

elif 8 <= severity <= 10:
    assigned_room = "Room 2"


# Triage summary
print("\n----- Triage Summary -----")
print("Severity Level:", severity)
print("Assigned Room:", assigned_room)