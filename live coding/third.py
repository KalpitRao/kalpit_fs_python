#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default. Hints:To override a method in super class, we can define a method with the same name in the super class.

class Shape:
    area=0
    def __init__(self,length):
        self.length = length

class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        a = (self.length * self.length)
        print('The area of the shape is :',a)

        
