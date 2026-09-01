def assign_triage_room():
    while True:
        severity_input = input("Enter severity of condition (1-10): ")

        # Check if input is a whole number (digit) and within the 1-10 range
        if severity_input.isdigit() and 1 <= int(severity_input) <= 10:
            severity = int(severity_input)
            break
        else:
            print("Error: Please enter a whole number between 1 and 10.")

    if 1 <= severity <= 4:
        assigned_room = "Waiting Room"
    elif 5 <= severity <= 7:
        assigned_room = "Room 1"
    elif 8 <= severity <= 10:
        assigned_room = "Room 2"

    print("----- Triage Summary -----")
    print(f"Severity Level: {severity}")
    print(f"Assigned Room: {assigned_room}")


# Run the function
assign_triage_room()