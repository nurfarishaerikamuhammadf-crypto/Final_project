from datetime import datetime, date, timedelta
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

GD = "GD"
SPECIALIST = "Specialist"
BASE_FEE = 100
LAB_TEST_RATE = 10
patient = {"name": "", "age": 0, "id": ""}

def calculate_total(number_of_lab_tests, patient_type):
    subtotal = BASE_FEE + number_of_lab_tests * LAB_TEST_RATE
    return subtotal * 0.70 if patient_type == "Subsidised" else subtotal

@app.route("/")
def index():
    return render_template("index.html", patient=patient)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        pid = request.form.get("id", "").strip()
        try: age = int(request.form.get("age", "0"))
        except ValueError: age = 0
        if name and age > 0 and pid:
            patient.update(name=name, age=age, id=pid)
            return render_template("result.html", title="Patient Registered",
                message="Patient registered successfully.",
                details=[f"Name: {name}", f"Age: {age}", f"ID: {pid}"])
        error = "Please enter valid information."
    return render_template("register.html", error=error)

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if not patient["name"]: return redirect(url_for("register"))
    error = None
    if request.method == "POST":
        dept = request.form.get("department", "")
        d = request.form.get("appointment_date", "")
        confirm = request.form.get("confirmation", "")
        try:
            appt = datetime.strptime(d, "%Y-%m-%d").date()
            if dept not in (GD, SPECIALIST): error = "Please select GD or Specialist."
            elif not date.today() <= appt <= date.today()+timedelta(days=7):
                error = "Please enter a date within the next 7 days."
        except ValueError: error = "Please use a valid date."
        if not error:
            msg = "Booking confirmed!" if confirm == "Y" else "Booking cancelled."
            return render_template("result.html", title="Appointment",
                message=msg, details=[f"Department: {dept}", f"Date: {d}"])
    return render_template("appointment.html", error=error,
        min_date=date.today().isoformat(),
        max_date=(date.today()+timedelta(days=7)).isoformat())

@app.route("/billing", methods=["GET", "POST"])
def billing():
    if not patient["name"]: return redirect(url_for("register"))
    error = None
    if request.method == "POST":
        ptype = request.form.get("patient_type", "")
        try: tests = int(request.form.get("number_of_lab_tests", ""))
        except ValueError: tests = -1
        if ptype not in ("Subsidised", "Private"):
            error = "Please select a valid patient type."
        elif tests < 0:
            error = "Invalid number. Please enter a whole number of 0 or more."
        else:
            total = calculate_total(tests, ptype)
            return render_template("result.html", title="Billing Summary",
                message=f"Total: ${total:.2f}",
                details=[f"Patient: {patient['name']}", f"Patient Type: {ptype}",
                         f"Lab Tests: {tests}"])
    return render_template("billing.html", error=error)

@app.route("/triage", methods=["GET", "POST"])
def triage():
    if not patient["name"]: return redirect(url_for("register"))
    error = None
    if request.method == "POST":
        try: severity = int(request.form.get("severity", ""))
        except ValueError: severity = 0
        if not 1 <= severity <= 10:
            error = "Please enter a whole number between 1 and 10."
        else:
            room = "Waiting Room" if severity <= 4 else "Room 1" if severity <= 7 else "Room 2"
            return render_template("result.html", title="Triage Summary",
                message=f"Assigned Room: {room}",
                details=[f"Patient: {patient['name']}", f"Severity: {severity}"])
    return render_template("triage.html", error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
