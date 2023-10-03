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
    

rectangle(10,21)

