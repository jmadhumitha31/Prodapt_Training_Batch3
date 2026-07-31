class Doctor:

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def __getitem__(self, time_slot):
        for appointment in self.appointments:
            if appointment.time_slot == time_slot:
                return appointment
        return "Appointment not found"

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"