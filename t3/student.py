class Student:
    def __init__(self, fio, course, group):
        self.fio = fio
        self.course = course
        self.group = group

    def __lt__(self, other):
        if self.course != other.course:
            return self.course < other.course
        elif self.group != other.group:
            return self.group < other.group
        else:
            return self.fio < other.fio

    def __str__(self):
        return f"{self.fio} Course: {self.course} Group: {self.group}"