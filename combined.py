# class method
class student:
    name="mahitha"
    def __init__(self,name):
        self.name=name
# as the consructor is defined in that way it need to be installiezed when it is called
s1=student("kavitha")
print(student.name)
print(s1.name)

#2
# Single Inheritance
class Student:
    def __init__(self):
        self.college = input("Enter your college name: ")
        self.year = input("Enter your academic year: ")
        print("Student Initialized:", self.college, self.year)

class core(Student):
    def __init__(self):
        super().__init__()  # Call parent constructor first
        self.branch = input("Enter branch of the student: ")
        self.mis = input("Enter MIS number: ")
        print("Core Student Initialized:", self.branch, self.mis)

   
class noncore(core):
    def __init__(self):
        super().__init__()
        self.subject=input("define different domains of the core subject:")
      
    def details(self):
        print("College:", self.college)
        print("Year:", self.year)
        print("Branch:", self.branch)
        print("MIS:", self.mis)
        print("subject:", self.subject)
        

# Create object
s1 = noncore()
s1.details()


# Single Inheritance
class Student:
    def __init__(self):
        self.college = input("Enter your college name: ")
        self.year = input("Enter your academic year: ")
        print("Student Initialized:", self.college, self.year)

class Core(Student):
    def __init__(self):
        super().__init__()  # Call parent constructor first
        self.branch = input("Enter branch of the student: ")
        self.mis = input("Enter MIS number: ")
        print("Core Student Initialized:", self.branch, self.mis)

    def details(self):
        print("College:", self.college)
        print("Year:", self.year)
        print("Branch:", self.branch)
        print("MIS:", self.mis)

# Create object
s1 = Core()
s1.details()


#single  inheritance
class student:
    college="IIIT PUNE"
    year="2024-28"
    def details(self):
        print(self.college,self.year)
class core(student):
    def __init__(self):
        self.branch=input("enter branch of a student:")
        self.mis=input("enter mis number of you:")
s1=core()
print(s1.branch,s1.mis,s1.college,s1.year)
s1.details()


class student:
    __name="mahitha"
    def __hello(self):
        print("I am",self.__name)
  
    def welcome(self):
        print("Hello welcome to IIIT PUNE")
        self.__hello()
s1=student()
s1.welcome()
# deleteing the object we can also delete attributes
class student:
    name="mahitha"
s1=student()
print(s1.name)
del s1
print(s1.name)