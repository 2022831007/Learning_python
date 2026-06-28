# ==================================================
#                ABSTRACTION
# ==================================================
# Abstract class defines WHAT to do.
# Child classes define HOW to do it.
# ==================================================
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


d = Dog()
d.sound()

c = Cat()
c.sound()
# from abc import ABC, abstractmethod


# # Abstract Class
# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass


# # Child Class
# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.1416 * self.radius * self.radius


# # Child Class
# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# c = Circle(5)
# r = Rectangle(4, 6)

# print("Circle Area:", c.area())
# print("Rectangle Area:", r.area())
# #another example
# # from abc import ABC, abstractmethod


# # class Animal(ABC):

# #     @abstractmethod
# #     def sound(self):
# #         pass


# # class Dog(Animal):

# #     def sound(self):
# #         print("Bark")


# # class Cat(Animal):

# #     def sound(self):
# #         print("Meow")


# # d = Dog()
# # d.sound()

# # c = Cat()
# # c.sound()