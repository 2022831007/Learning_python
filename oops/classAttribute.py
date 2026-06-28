class Person:
    name = "anynomous"
    type="CSE"
    # def changeName(self,name):#it will print the person name,not the changeable name  
    #     self.name=name  
    def changeName(self,name):#it will print the changeable name,not the class name
        Person.name=name
   #another way to print the changeable name even though call the class's object
    def changing(self,type):
        self.__class__.type="SWE"
        #self.__class__.
        #Person.
     
     
p1 = Person()
p1.changeName("Fatema") 
p1.changing("SWE") 
print(p1.name) 
# print(Person.name)   #it will print the Person class name,not the changeable name  
print(Person.name)
print(Person.type)