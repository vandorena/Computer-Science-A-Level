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
        self._data = [None]*30
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e) #im lazy

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    def pop(self): 
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop() # im lazy
    
    
    