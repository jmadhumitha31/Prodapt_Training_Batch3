from patient import Patient
from appointment import Appointment
from doctor import Doctor
from clinic import Clinic
from notification import SMSNotifier, EmailNotifier, MockNotifier

# Patients
p1 = Patient("John", 25, 101)
p2 = Patient("Alice", 30, 102)

# Doctors
d1 = Doctor("Ravi", "Cardiologist")
d2 = Doctor("Meena", "Dermatologist")

# Appointments
a1 = Appointment(p1, "10:00 AM", 30)
a2 = Appointment(p2, "11:00 AM", 45)

# Add appointments
d1.add_appointment(a1)
d2.add_appointment(a2)

# Clinic
clinic = Clinic("City Hospital")
clinic.add_doctor(d1)
clinic.add_doctor(d2)


# Magic Method __len__
print("Total Appointments:", len(clinic))

# Magic Method __getitem__
print(d1["10:00 AM"])

# Notifications
sms = SMSNotifier()
email = EmailNotifier()
mock = MockNotifier()

sms.send("Your appointment is confirmed.")
email.send("Doctor appointment booked.")
mock.send("Testing notification.")
