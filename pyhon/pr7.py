class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        total = 0
        for mark in self.marks:
            total += mark
        print("Average is:", total // len(self.marks))

s1 = Student("mahitha", [10, 10, 10])
print(s1.name)
s1.avg()
