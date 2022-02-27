from unicodedata import name


class Student:
    schoolName = 'StXaviers'

    def __init__(self):
        self.name = 'Mark'
        self.phy = 80
        self.chem = 90
        self.bio = 40

std = Student()
std.name
std.Total()