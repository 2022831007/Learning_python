class Student:
    def __init__(self,name):
        self.name=name

s1 = Student("Fatema")
print(s1.name)
del s1 #delete the s1 object
print(s1)