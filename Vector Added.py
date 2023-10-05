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

def createvector(dimensions):
    vectorlist = []
    if dimensions == 2:
        vectorlist.append(int(input("What is your i vector")))
        vectorlist.append(int(input("What is your j vector")))
    elif dimensions == 3:
        vectorlist.append(int(input("Enter your i vector")))
        vectorlist.append(int(input("Enter your j vector")))
        vectorlist.append(int(input("Enter your k vector")))
    return vectorlist

def listsplitter(list):
    rdvectorlist = []
    ndVectorlist = []
    idkvectorlist = []
    for i in range (0,len(list)):
        if len(list[i]) == 2:
            ndVectorlist.append(list[i])
        elif len(list[i]) == 3:
            rdvectorlist.append(list[i])
        else:
            idkvectorlist.append(list[i])
    concatenatedlist = [ndVectorlist,rdvectorlist,idkvectorlist]
    return concatenatedlist



overallvectorlist = []        
for i in range (0,int(input("How many vectors do you want to input: "))):
    dimensions = int(input("For a 3d vector enter 3, for a 2d vector enter 2: "))
    newvector = createvector(dimensions)
    print(f"I have added {newvector} to the list")
    overallvectorlist.append(newvector)
newoverallvectorlist = listsplitter(overallvectorlist)
NDVECTORS = newoverallvectorlist[0]
RDVECTORS = newoverallvectorlist[1]
ERRORVECTORS = newoverallvectorlist[2]
print(f"Your 2d Vectors are {NDVECTORS}")
print(f"Your 3d vectors are {RDVECTORS}")
print(f"Your error list is {ERRORVECTORS}")
print("")


choicelistrecur = False
while choicelistrecur == False:
    print("What do you want to do with those vectors?")
    print("If you want to do some addition of the vectors enter 1: ")
    print("If you want to find the magnitude of the vectors enter 2: ")
    print("If you want to do some multiplication of the vectors enter 3: ")
    choiceuser = int(input(""))
    if choiceuser == 1 or choiceuser == 2 or choiceuser == 3:
        choicelistrecur = True

    dimensionchoicerecur = False

    while dimensionchoicerecur == False:
        print("to work with the 2d vectors entered earlier, input 1")
        print("to work with the 3d vectors entered earlier input 2")
        dimensioonchoice = int(input(""))
        if dimensioonchoice == 1 or dimensioonchoice == 2:
            dimensionchoicerecur = True

    if choiceuser == 1:
        #add
        choicelistrecur = True
        if dimensioonchoice == 1:
            for i in range(0,len(NDVECTORS)):
                Vector(NDVECTORS[i])
        else:
            for i in range(0,len(RDVECTORS)):
                Vector(RDVECTORS[i])


    elif choiceuser == 2:
        choicelistrecur = True
        #magnitude
    elif choiceuser == 3:
        # multiply
        choicelistrecur = True