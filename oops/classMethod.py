class Person:
    name = "anynomous" 
    @classmethod
    def changeName(cls,name): #cls is not self,it actually refering to the class
       cls.name=name

p1 = Person()
p1.changeName("Fatema")
print(p1.name)
print(Person.name)