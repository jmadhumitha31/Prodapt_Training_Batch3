class Clinic:

    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def __len__(self):
        total = 0
        for doctor in self.doctors:
            total += len(doctor.appointments)
        return total