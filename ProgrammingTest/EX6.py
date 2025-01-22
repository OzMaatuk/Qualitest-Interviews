# Give an abstract implementation for the following structure:
# Company - number of employees, CEO, revenue.
# Tester - age, gender, name, expirience, qualification, speciality(SW/HW).
# Automation Developer - age, gender, name, expirience, qualification, speciality(SW/HW).
# HR - age, gender, name, expirience, qualification.
# Accountant -  age, gender, name, expirience, license.

from typing import Any


class Company:
    def __init__(self, num_of_emp: int, ceo: str, revenue: int):
        self.num_of_emp = num_of_emp
        self.ceo = ceo
        self.revenue = revenue

    def __str__(self) -> str:
        return f"Company.\nnum_of_emp: {self.num_of_emp}, ceo: {self.ceo}, revenue: {self.revenue}"


class Person:
    def __init__(self, age: int, gender: str, name: str, expirience: int):
        self.age = age
        self.gender = gender
        self.name = name
        self.expirience = expirience

    # def __getattribute__(self, __name: str) -> Any:
    # Implemented by default in Python and no custom change are needed,

    # def __setattr__(self, __name: str, __value: Any) -> None:
    # Implemented by default in Python and no custom change are needed,

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}, expirience: {self.expirience}"


class TechPerson(Person):
    def __init__(self, age: int, gender: str, name: str, expirience: int, qualification: str, speciality: str):
        super().__init__(age, gender, name, expirience)
        self.qualification = qualification
        self.speciality = speciality

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "speciality":
            if __value not in ["SW", "HW"]:
                raise ValueError('speciality member should be only "SW"/"HW"')
        return super().__setattr__(__name, __value)

    def __str__(self) -> str:
        return (
            super().__str__()
            + f", qualification: {self.qualification}, speciality: {self.speciality}"
        )


class Tester(TechPerson):
    def __str__(self) -> str:
        return "Tester.\n" + super().__str__()


class Automation(TechPerson):
    def __str__(self) -> str:
        return "Automation Developer.\n" + super().__str__()


class HR(Person):
    def __init__(self, age: int, gender: str, name: str, expirience: int, qualification: str):
        super().__init__(age, gender, name, expirience)
        self.qualification = qualification

    def __str__(self) -> str:
        return "HR.\n" + super().__str__() + f", qualification: {self.qualification}"


class Accountant(Person):
    def __init__(self, age: int, gender: str, name: str, expirience: int, license: str):
        super().__init__(age, gender, name, expirience)
        self.license = license

    def __str__(self) -> str:
        return "Accountant.\n" + super().__str__() + f", license: {self.license}"



c = Company(10, "ABC", 10000)
print(c)
print()

accountant = Accountant(60, "male", "SDF", 15, "None")
print(accountant)
print()

hr = HR(20, "male", "TRE", 4, "IDK")
print(hr)
print()

auto = Automation(30, "m", "YUI", 5, "None", "SW")
print(auto)
print()

tester = Tester(30, "m", "QWE", 8, "QUALI", "HW")
print(tester)
print()

try:
    invalid = Tester(30, "m", "QWE", 8, "QUALI", "None")
except(ValueError):
    print("Correct error was raised.")