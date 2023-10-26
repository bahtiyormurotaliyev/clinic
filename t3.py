from NosuchDoctor import NoSuchDoctor
from Doctor import Doctor


class Person:
    def __init__(self, ssn):
        self.ssn = ssn
        self.doctor = None

    def assignPatientToDoctor(self, doctor_id):
        found = False
        for doctor in Doctor.doctors:
            if doctor.id == doctor_id:
                found = True
                self.doctor = doctor
                doctor.patients.append(self)
                break
        if not found:
            raise NoSuchDoctor("Berilgan ID bilan shifokor topilmadi.")

    def getDoctor(self):
        return self.doctor
