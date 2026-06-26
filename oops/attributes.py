#constructor:all classes have a function called init function
#which is alawys executed when the object is being
#initiated
class Student:
    college_name = "Sherpur Govt College"#class attributes
    
       
       
   #parametarized constructor    
    def __init__(self,name,marks): #constructor
      print(self)
      self.name=name #object attributes
      self.marks=marks
      #precendence of object attribute>class attributes



      print("adding new studens in the database")
    
s1 = Student("Fatema",97)    
print(s1.name,s1.marks)
s2 = Student("tanha",87) 
print(s2.name,s2.marks)   
print(s2.college_name)

