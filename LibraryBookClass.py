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
        self.pointer = len(Libraryarray.CDlist) + 1
        self.datapackage = [self._Title,self._Maker,self._Playtime,self._Album,self._Genre,self.pointer]
        Libraryarray.CDlistAppend(self.datapackage)
        

    def DisplayDetails(self):
        print(f"Title is: {self._Title}, Artist: {self._Maker}, Album: {self._Album}, Genre: {self._Genre} Loan Status: {self.Onloan}, Date and Time Acquired: {self._DateAcquired}, Playtime is {self._Playtime} seconds")

class Book(LibaryStock):
    def __init__(self, Title, Maker, ISBN ,genre):
        super().__init__(Title, Maker, genre)
        self._ISBN = ISBN
        self.pointer = len(Libraryarray.Booklist) + 1
        self.datapackage = [self._Title,self._Maker,self._ISBN,self._Genre,self.pointer]
        Libraryarray.BooklistAppend(self.datapackage)
    
    def DisplayDetails(self):
        print(f"Title is : {self._Title}, Author is: {self._Maker}, Genre is: {self._Genre}, Loan Status: {self.Onloan}, Date and Time Acquired: {self._DateAcquired}, ISBN Reference: {self._ISBN}")

class LibraryArray:
    def __init__(self):
        self.Booklist = []
        self.CDlist = []

    def BooklistAppend(self,data):
        self.Booklist.append(data)
    
    def CDlistAppend(self,data):
        self.CDlist.append(data)

Libraryarray = LibraryArray()

def newitem():
    holderforfirstwhileloop = False
    while not holderforfirstwhileloop:
        wronginputfordigitchoice = False
        while not wronginputfordigitchoice:
            print ("Enter 1 to add a new CD, enter 2 to add a new Book")
            print ("")
            userchoicebetweencdandbook = int(input())
            if userchoicebetweencdandbook == (1 or 2):
                wronginputfordigitchoice = True
        if userchoicebetweencdandbook == 1:
            secondwhileloopholder = False
            while not secondwhileloopholder:
                titles = input("Enter the title: ")
                maker = input("Enter the artist name: ")
                album = input("Enter the album here: ")
                genre = input ("Enter the genre here: ")
                playtime = input ("enter the time in seconds here") # I could try to do more with the datetime module but atm i dont feel like the added complexity would add necessary value
                print(f"please check over the following, and click enter if they are correct")
                print(f"your title is: {titles}, your artist is {maker}, your album is {album}, your genre is {genre} and your playtime is {playtime} seconds")
                print(f"is this correct?")
                correct = input("")
                if correct == "":
#gotta add stuff here
                    secondwhileloopholder = True
        else:
            secondwhileloopholder = False
            while not secondwhileloopholder:
                titles = input("Enter the title: ")
                maker = input("Enter the author name: ")
                album = input("Enter the album here: ")
                genre = input ("Enter the genre here: ")
                playtime = input ("enter the time in seconds here") # I could try to do more with the datetime module but atm i dont feel like the added complexity would add necessary value
                print(f"please check over the following, and click enter if they are correct")
                print(f"your title is: {titles}, your artist is {maker}, your album is {album}, your genre is {genre} and your playtime is {playtime} seconds")
                print(f"is this correct?")
                correct = input("")
                if correct == "":
                    secondwhileloopholder = True
