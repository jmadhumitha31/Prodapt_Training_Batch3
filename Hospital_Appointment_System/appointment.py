class Appointment:

    def __init__(self, patient, time_slot, duration_minutes):
        self.patient = patient
        self.time_slot = time_slot
        self.duration_minutes = duration_minutes

    @property
    def duration_minutes(self):
        return self.__duration

    @duration_minutes.setter
    def duration_minutes(self, value):
        if value < 10 or value > 120:
            raise ValueError("Duration must be between 10 and 120 minutes.")
        self.__duration = value

    def __str__(self):
        return f"{self.patient.name} - {self.time_slot} ({self.duration_minutes} mins)"

