class Doctor:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def addDoctor(self, doctor):
        self.doctors.append(doctor)

    def addPatient(self, patient):
        self.patients.append(patient)

    def idleDoctors(self):
        idle_doctors = []
        for doctor in self.doctors:
            if not doctor.getPatients():
                idle_doctors.append(doctor)
        return sorted(idle_doctors, key=lambda d: (d.surname, d.name))

    def busyDoctors(self):
        return sorted(self.doctors, key=lambda d: (d.surname, d.name), reverse=True)

    def doctorsByNumPatients(self):
        sorted_doctors = sorted(self.doctors, key=lambda d: len(d.getPatients()))
        return [f"{len(doctor.getPatients()):>3}: {doctor.id} {doctor.surname} {doctor.name}" for doctor in sorted_doctors]

    def countPatientsPerSpecialization(self):
        specialization_dict = {}
        for doctor in self.doctors:
            specialization = doctor.getSpecialization()
            if specialization not in specialization_dict:
                specialization_dict[specialization] = 0
            specialization_dict[specialization] += len(doctor.getPatients())
        sorted_specializations = sorted(specialization_dict.items(), key=lambda item: item[0])
        return [f"{count:>3} - {specialization}" for specialization, count in sorted_specializations]
