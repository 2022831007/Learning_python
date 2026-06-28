#define a circle with radius r using the constructor
#define an Area() method of the class which allows you to calculate the to perimeter of the circle
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def Area(self):
#         return (22/7)*self.radius ** 2
    
#     def perimter(self):
#         return 2*(22/7)*self.radius

# c1= Circle(21)
# print(c1.Area())
# print(c1.perimter())
#define  employee class with attribute role,department&salary,this class also has a show
#details() method,create an Enginerr class that inherits properties from Employess class
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("Role = ",self.role)
        print("Department = ",self.dept)
        print("salary = ",self.salary)  

e1 = Employee("Manager","SWE","180000")
e1.showDetails()
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")

eng1 = Engineer("Fatema",22)
eng1.showDetails()
#craete a class called order which stores item and its price
#use Dunder Function --gt--()to conevy that:
#order1>order2 if price of order1>price of order2
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2) :
           return self.price>ordr2.price

ordr1 = Order("chips",20)
ordr2 = Order("tea",10)
print(ordr1>ordr2)
