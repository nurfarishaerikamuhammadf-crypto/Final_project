from datetime import datetime, date, timedelta

GD = "GD"
SPECIALIST = "Specialist"

# Get department
print("Please input your department:")
staff_department = input()

while staff_department not in (GD, SPECIALIST):
    print("Error, please retry")
    staff_department = input()

# Get appointment date
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

# Confirm booking
print("Confirm booking (Y/N):")
confirmation = input().upper()

while confirmation not in ("Y", "N"):
    print("Please enter Y or N:")
    confirmation = input().upper()

if confirmation == "Y":
    print("Booking confirmed")
else:
    print("Booking cancelled")