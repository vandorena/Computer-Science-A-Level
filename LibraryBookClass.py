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
        self.biglist = []

    def BooklistAppend(self,data):
        self.Booklist.append(data)
        self.biglist = [self.Booklist,self.CDlist]
    
    def CDlistAppend(self,data):
        self.CDlist.append(data)
        self.biglist = [self.Booklist,self.CDlist]
    
    def printalllist(self):
        print(f" the biglist is: {self.biglist}")
        print(f"the cd list is {self.CDlist}")
        print(f"The Book List is: {self.Booklist}")

    def _cdsort(self):
        for i in range (0,len(self.CDlist)):
            for j in range(0,len(self.CDlist)-i-1):
                if self.CDlist[j[1]] > self.CDlist[j+1[1]]:
                    self.CDlist[j], self.CDlist[j+1] = self.CDlist[j+1] ,self.CDlist[j]
    
    def _booksort(self):
        for i in range (0,len(self.Booklist)):
            for j in range(0,len(self.Booklist)-i-1):
                if self.Booklist[j[1]] > self.Booklist[j+1[1]]:
                    self.Booklist[j], self.Booklist[j+1] = self.Booklist[j+1] ,self.Booklist[j]


    def booksort(self):


Libraryarray = LibraryArray()

def _newitem():
    holderforfirstwhileloop = False
    while not holderforfirstwhileloop:
        wronginputfordigitchoice = False
        while not wronginputfordigitchoice:
            print ("Enter 1 to add a new CD, enter 2 to add a new Book")
            print ("")
            userchoicebetweencdandbook = int(input())
            if userchoicebetweencdandbook == 1 or userchoicebetweencdandbook ==2 :
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
                    returnitem = CD(titles,maker,album,genre,playtime)
#gotta add stuff here
                    secondwhileloopholder = True
                    return returnitem
        else:
            secondwhileloopholder = False
            while not secondwhileloopholder:
                titles = input("Enter the title: ")
                maker = input("Enter the author name: ")
                Isbn = input("Enter the ISBN here: ")
                genre = input ("Enter the genre here: ")
                #playtime = input ("enter the time in seconds here") # I could try to do more with the datetime module but atm i dont feel like the added complexity would add necessary value
                print(f"please check over the following, and click enter if they are correct")
                print(f"your title is: {titles}, your author is {maker}, your ISBN is {Isbn}, your genre is {genre}")
                print(f"is this correct?")
                correct = input("")
                if correct == "":
                    returnitem = Book(titles,maker,Isbn,genre)
                    secondwhileloopholder = True
                    return returnitem

def sort():
    userchoiceboolholder = False
    while not userchoiceboolholder:
        print("Enter 1 to sort the cd list, or 2 to sort the book list")
        cdorbooklist = int(input(""))
        if cdorbooklist == 1 or cdorbooklist == 2:
            userchoiceboolholder = True
    if cdorbooklist == 1:
            


item1 = _newitem()
item2 = _newitem()
item3 = _newitem()
Libraryarray.printalllist()