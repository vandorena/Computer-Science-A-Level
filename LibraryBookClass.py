import datetime
import time
class LibaryStock:

    def __init__(self,Title,Maker,genre):
        self._Title = Title
        self._Maker = Maker
        self.Onloan = False
        self._DateAcquired = datetime.datetime.now()
        self.Overdue = False
        self._Genre = genre

    def setloan(self):
        self.Onloan = True
        self.datelended = datetime.datetime.now()

    def Returnloan(self):
        self.Onloan = False

class CD(LibaryStock):

    def __init__(self, Title, Maker, album, genre, playtime):
        super().__init__(Title, Maker, genre)
        self._Playtime = playtime
        self._Album = album
        

    def DisplayDetails(self):
        print(f"Title is: {self._Title}, Artist: {self._Maker}, Album: {self._Album}, Genre: {self._Genre} Loan Status: {self.Onloan}, Date and Time Acquired: {self._DateAcquired}, Playtime is {self._Playtime} seconds")

class Book(LibaryStock):
    def __init__(self, Title, Maker, ISBN):
        super().__init__(Title, Maker)
        self._ISBN = ISBN
    
    def DisplayDetails(self):
        print(f"Title is : {self._Title}, Author is: {self._Maker}, Genre is: {self._Genre}, Loan Status: {self.Onloan}, Date and Time Acquired: {self._DateAcquired}, ISBN Reference: {self._ISBN}")




book1 = Book("hi", "ds", 45)

book1.DisplayDetails()
time.sleep(67)
book1.DisplayDetails()