#method that dont use the self parameter(work at class level)
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
    @staticmethod #decorator,no need self parameter
    def hello():
       print("ABC college")
    def welcome(self): #methods
      print("welcome student",self.name)

    def get_marks(self):
         return self.marks
    
    print("adding new studens in the database")
    
s1 = Student("Fatema",97)    
print(s1.name,s1.marks)
s2 = Student("tanha",87) 
print(s2.name,s2.marks)   
print(s2.college_name)
s1.welcome()
print(s1.get_marks())
s1.hello()


