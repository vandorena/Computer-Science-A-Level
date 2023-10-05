import random
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = (self.width *2) + (self.height*2)
        return self.perimeter
    
    def get_diagnol(self):
        self.widthsquared = self.width * self.width
        self.heightsquared = self.height * self.height
        self.totalsquared = self.widthsquared + self.heightsquared
        self.diagnol = self.totalsquared ** 0.5
        return self.diagnol
    
    def showsides(self):
        print(f"The width is {self.width}")
        print(f"The length is {self.height}")

def testfunction():    
   # width = int(input("oi, Input the width here: "))
   # height = int(input("oi, Input the height here: "))
    width = random.randint(1,1000)
    height = random.randint(1,1000)
    tested = Rectangle(width,height)
    print(f"{Rectangle.get_area(tested)} this is the area of the quadrilateral (i cant believe you dont know how to do this already)")
    print(f"{Rectangle.get_perimeter(tested)} this is the perimeter of the quadrilateral")
    print(f"{Rectangle.get_diagnol(tested)} is the length of the diagnol of the quadrilateral")
    Rectangle.showsides(tested)

for i in range(0,random.randint(1,100000)):
    testfunction()
    print(i)
