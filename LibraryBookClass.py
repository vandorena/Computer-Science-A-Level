import datetime
import time
class LibaryStock:

    def __init__(self,Title,Maker):
        self._Title = Title
        self._Maker = Maker
        self.Onloan = False
        self._DateAcquired = datetime.datetime.now()
        self.Overdue = False

    def setloan(self):
        self.Onloan = True
        self.datelended = datetime.datetime.now()

    def Returnloan(self):
        self.Onloan = False

class CD(LibaryStock):

    def __init__(self, Title, Maker, playtime):
        super().__init__(Title, Maker)
        self._Playtime = playtime

    def DisplayDetails(self):
        print(f"{self._Title}, {self._Maker}, {self.Onloan}, {self._DateAcquired}, Playtime is {self._Playtime} seconds")

class Book(LibaryStock):
    def __init__(self, Title, Maker, ISBN):
        super().__init__(Title, Maker)
        self._ISBN = ISBN
    
    def DisplayDetails(self):
        print(f"{self._Title}, {self._Maker}, {self.Onloan}, {self._DateAcquired}, {self._ISBN}")




book1 = Book("hi", "ds", 45)

book1.DisplayDetails()
time.sleep(67)
book1.DisplayDetails()