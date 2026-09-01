def calculate_total(number_of_lab_tests, patient_type):
    subtotal = BASE_FEE + (number_of_lab_tests * LAB_TEST_RATE)

    if patient_type == "Subsidised":
        total = subtotal * 0.70
    else:
        total = subtotal

    return total

# Constants
BASE_FEE = 100
LAB_TEST_RATE = 10

# Input patient type
patient_type = input("Enter patient type (Subsidised / Private): ")

while patient_type not in ("Subsidised", "Private"):
    print("Invalid option, please re-enter")
    patient_type = input("Enter patient type (Subsidised / Private): ")

# Input number of lab tests
number_of_lab_tests = float(input("Enter number of lab tests: "))

while number_of_lab_tests <= 0 or number_of_lab_tests % 1 != 0:
    print("Invalid number, please re-enter a valid number")
    number_of_lab_tests = float(input("Enter number of lab tests: "))

# Calculate total
total = calculate_total(number_of_lab_tests, patient_type)

# Output
print("Patient Type:", patient_type)
print("Total: $", format(total, ".2f"))
