import math
class Vector:
    def __init__(self,Vector1):
        self.dimensions = len(Vector1)
        if self.dimensions == 2:
            self.xvector = Vector1[0]
            self.yvector = Vector1[1]
            self.value = Vector1
        elif self.dimensions == 3:
            self.xvector = Vector1[0]
            self.yvector = Vector1[1]
            self.zvector = Vector1[2]
           

    def __add__(self, ndVector):
        if self.dimensions == 2:
            newobject = Vector([self.xvector + ndVector.xvector,self.yvector + ndVector.yvector])
        elif self.dimensions == 3:
            newobject = Vector([self.xvector + ndVector.xvector, self.yvector + ndVector.yvector, self.zvector + ndVector.zvector])
        return newobject
    
    def __eq__(self, ndVector):
        if self.xvector == ndVector.xvector and self.yvector == ndVector.yvector and self.dimensions == 2:
            return True
        elif self.xvector == ndVector.xvector and self.yvector == ndVector.yvector and self.zvector == ndVector.zvector and self.dimensions == 3:
            return True
        else:
            return False
        
    def multiply(self,ndVector):
        if self.dimensions == 2:
            newobject = Vector([self.xvector * ndVector.xvector, self.yvector * ndVector.yvector])
        elif self.dimensions == 3:
            newobject = Vector([self.xvector * ndVector.xvector , self.yvector * ndVector.yvector, self.zvector * ndVector.zvector])
        return newobject
    
    def magnitudecombinedvector(self,ndVector):
        
        addedvectors = Vector.__add__(ndVector)
        isquared = addedvectors[0] ** 2
        jsquared = addedvectors[1] ** 2
        if self.dimensions == 2:
            both = isquared + jsquared
            magnitude = both ** 0.5
        elif self.dimensions == 3:
            ksquared = addedvectors[2] * 2
            all = isquared + jsquared +ksquared
            magnitude = all ** 0.5
        return magnitude
    
    def magnitudesingle(self):
        isquared = self.xvector ** 2
        jsquared = self.yvector ** 2
        if self.dimensions == 3:
            ksquared = self.zvector ** 2
            addedall = isquared + jsquared + ksquared
        elif self.dimensions == 2:
            addedall = isquared + jsquared
        magnitude = addedall ** 0.5
        return magnitude
    
    def magnitudetriple(self,ndVector,rdVector):
        vectoradd1 = Vector.__add__(self,ndVector)
        vectoradded = Vector.__add__(vectoradd1,rdVector)
        magnitude = Vector.magnitudesingle(vectoradded)
        return magnitude
    
VectorUno = Vector([10,21])
VectorDos = Vector([122,22])

vectoradded = VectorUno + VectorDos
print(vectoradded.value)
print(VectorUno == VectorDos)