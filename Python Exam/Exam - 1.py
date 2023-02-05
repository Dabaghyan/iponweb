from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta


class Patient:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return "Patient - {}{}\nAge - {}\nGender - {}".format(self.name, self.surname, self.age, self.gender)


    def __ne__(self, other):
        if self.name == other.name and self.surname == other.surname and self.age == other.age and self.gender == other.gender:
            return False
        else:
            return True



class Doctor:
    def __init__(self, name, surname, schedule: dict):
        self.name = name
        self.surname = surname
        self.schedule = schedule

    def __repr__(self):
        return "Doctor: {} {}\nSchedule:{}".format(self.name, self.surname, self.schedule)

    def register_patient(self, new_patient: Patient, date_time: datetime):
        # working_day_starts = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 10, 0, 0)
        # working_day_ends = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 18, 0, 0)
        if new_patient in self.schedule.values():
            print('Patient {} is already registered'.format(new_patient))
        elif new_patient not in self.schedule.values() and date_time.time() not in self.schedule.keys():
            self.schedule.__setitem__(str(date_time.time()), new_patient)


    def is_free(self, date_time: datetime):
        if str(date_time.time()) not in self.schedule.keys():
            print('Doctor is free on this hours')
        else:
            print('Doctor is not free on this hours')

    def is_registered(self, other_patient):
        if other_patient in self.schedule.values():
            print("The patient is already registered")
        else:
            print("The patient is not registered")


p = Patient("John", "Doe", 30, "male")
p1 = Patient("John", "Doe", 30, "male")
print(p)
d1 = datetime(2023, 4,5, 12,0,0)
print(p.__ne__(p1))


# d = Doctor("Anna", "Hakobyan", {})
# print(d)
# d.register_patient(p1, d1)
# print(d)
# d.is_free(d1)
# d.is_registered(p)
# d.is_registered(p1)






