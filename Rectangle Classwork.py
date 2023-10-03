class rectangle:
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
    
width = input("oi, Input the width here: ")
height = input("oi, Input the height here: ")
rectangle(width,height)
print(f"{rectangle.get_area} this is the area of the quadrilateral (i cant believe you dont know how to do this already)")
print(f"{rectangle.get_perimeter} this is the perimeter of the quadrilateral")
print(f"{rectangle.get_diagnol} is the length of the diagnol of the quadrilateral")
