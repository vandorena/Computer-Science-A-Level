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
            raise Exception("NotEnoughSpace")
        else:
            self.toppointer += 1
            self.data[self.toppointer] = newitem
    def pop(self):
        if self.toppointer > 0:
            returnitem = self.data[self.toppointer]
            self.toppointer -= 1
            return Exception("returnitems")
        else:
            raise Exception("emptysiding")

class WagonArray:
    def __init__(self):
        self.wagon_list = []

    def Append(self,data):
        self.wagon_list.append(data)

    def _print_wagon_list(self,integer):
        try:
            if integer == 1:
                print(self.wagon_list)
        except TypeError:
            print("There was an error, add to the lists")

    def _wagonsort(self):
        try:
            for i in range (0,len(self.wagon_list)):
                for j in range(0,len(self.wagon_list)-i-1):
                    if self.wagon_list[i] > self.wagon_list[j+1]:
                        self.wagon_list[j], self.wagon_list[j+1] = self.wagon_list[j+1] ,self.wagon_list[j]
        except TypeError:
            print("There was an error sorting the wagon list")

    
    