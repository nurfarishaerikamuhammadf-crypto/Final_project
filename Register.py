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