class Wagon:
    def __init__(self):
        self._OwnerName = input("Enter the Owner's Name: ")
        self._Weight = float(input("Enter the Weight: "))
        self._NumberOfWheels = int(input("Enter the number of wheels: "))

class ClosedWagon(Wagon):
    def __init__(self):
        super().__init__()
        self._Height = input("Enter the height: ")
        self._NumberOfDoors = int(input("Enter the number of doors: "))
        self.SuitableForFoodstuffs = False

class OpenWagon(Wagon):
    def __init__(self):
        super().__init__()
        self._Height = input("Enter the height: ")
        self._NumberOfDoors = int(input("Enter the number of doors: "))
        self.SuitableForFoodstuffs = False

class RefrigeratedWagon(ClosedWagon):
    def __init__(self):
        super().__init__()
        self.fridgeopen = False
        self.fridgetemperature = 0

class Siding:
    def __init__(self):
        self.data = [None]*30
        self.toppointer = -1
    def push(self,newitem):
        if self.toppointer == 29:
            raise NotEnoughSpace
        else:
            self.toppointer += 1
            self.data[self.toppointer] = newitem
    def pop(self):
        returnitem = self.data[self.toppointer]
        self.toppointer -= 1
        return returnitem

    
    
    