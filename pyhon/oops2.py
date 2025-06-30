class student:
    college="IIIT PUNE" # class attribute
    # we cant use two consructors

    def __init__(self,name,cgpa):
        print("i am parametrised constructor")
        self.name=name# aoject attribute
        self.cgpa=cgpa
        print("i am",name,"with the",cgpa)
    # methods
    def sum(self,a,b):
        return(a+b)
    

s2=student("mahitha",9.0)
print(s2.college)
# function calling
print(s2.sum("hello ","mahitha"))
        
