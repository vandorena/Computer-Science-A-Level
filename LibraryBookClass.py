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
        self.datedue = datetime.datetime.now() + self._maxloantime
    
    def Returnloan(self):
        self.Onloan = False
        self.datedue = datetime.datetime.now()

class CD(LibaryStock):

    def __init__(self, Title, Maker, album, genre, playtime):
        super().__init__(Title, Maker, genre)
        self._Playtime = playtime
        self._Album = album
        self.pointer = len(Libraryarray.CDlist) + 1
        self.datapackage = [self._Title,self._Maker,self._Playtime,self._Album,self._Genre,self.pointer,self]
        Libraryarray.CDlistAppend(self.datapackage)
        Libraryarray._cdsort()
        self._maxloantime = datetime.timedelta(days= 7)
        

    def DisplayDetails(self):
        print(f"Title is: {self._Title}, Artist: {self._Maker}, Album: {self._Album}, Genre: {self._Genre} Loan Status: {self.Onloan}, Date and Time Acquired: {self._DateAcquired}, Playtime is {self._Playtime} seconds")

class Book(LibaryStock):
    def __init__(self, Title, Maker, ISBN ,genre):
        super().__init__(Title, Maker, genre)
        self._ISBN = ISBN
        self.pointer = len(Libraryarray.Booklist) + 1
        self.datapackage = [self._Title,self._Maker,self._ISBN,self._Genre,self.pointer,self]
        Libraryarray.BooklistAppend(self.datapackage)
        Libraryarray._booksort()
        self._maxloantime = datetime.timedelta(days=14)
    
    
    
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

    def _printsinglelist(self,integer):
        try:
            if integer == 1:
                for i in range(0,len(self.biglist[1])):
                    print(self.biglist[1][i])
            elif integer == 2:
                for i in range(0,len(self.Booklist)):
                    print(self.Booklist[i])
            elif integer == 3:
                for i in range(0,len(self.CDlist)):
                    print(self.CDlist[i])
        except TypeError:
            print("There was an error, add to the lists")

    def printalllist(self):
        print(f" the biglist is: {self.biglist}")
        print(f"the cd list is {self.CDlist}")
        print(f"The Book List is: {self.Booklist}")

    def _cdsort(self):
        try:
            for i in range (0,len(self.CDlist)):
                for j in range(0,len(self.CDlist)-i-1):
                    if self.CDlist[i][1] > self.CDlist[j+1][1]:
                        self.CDlist[j], self.CDlist[j+1] = self.CDlist[j+1] ,self.CDlist[j]
        except TypeError:
            print("There was an error sorting the CD list")
    
    def _booksort(self):
        try:
            for i in range (0,len(self.Booklist)):
                for j in range(0,len(self.Booklist)-i-1):
                    if self.Booklist[i][1] > self.Booklist[j+1][1]:
                        self.Booklist[j], self.Booklist[j+1] = self.Booklist[j+1] ,self.Booklist[j]
        except TypeError:
            print("There was an error sorting the book list")
    
    def _biglistsort(self):
        try:
            for i in range (0,len(self.biglist[1])):
                for j in range(0,len(self.biglist[1])-i-1):
                    if self.biglist[1][i][1] > self.biglist[1][j+1][1]:
                        self.biglist[1][j], self.biglist1[1][j+1] = self.biglist[1][j+1] ,self.biglist[1][j]
        except TypeError:
            print("There was an error sorting the big list")

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
                isbn_while_loop_holder = False
                isbn_while_loop_hold_check = False
                while not isbn_while_loop_holder or not isbn_while_loop_hold_check:
                    Isbn = input("Enter the ISBN here: ")
                    try:
                        if len(Isbn) == 13:
                            isbn_while_loop_holder = True
                        if ISBNChecker(Isbn) == True:
                            isbn_while_loop_hold_check = True
                    except:
                        raise ValueError
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

def manualsort():
    userchoiceboolholder = False
    while not userchoiceboolholder:
        print("Enter 1 to sort the cd list, or 2 to sort the book list, or enter 3 to sort the encompassinglist")
        cdorbooklist = int(input(""))
        if cdorbooklist == 1 or cdorbooklist == 2 or cdorbooklist == 3:
            userchoiceboolholder = True
    if cdorbooklist == 1:
        Libraryarray._cdsort()
    elif cdorbooklist == 2:
        Libraryarray._booksort()
    else:
        Libraryarray._biglistsort()

def setloan():
    try:
        firstbooleanholder = False
        while not firstbooleanholder:
            for i in range(0,len(Libraryarray.biglist)):
                print(f"enter {i} to select the item called {Libraryarray.biglist[1][i][0]}")
            userchoice = int(input(""))
            if type(userchoice) != "string":
                firstbooleanholder = True
        Libraryarray.biglist[1][userchoice][-1].setloan()
    except TypeError:
        print("Error setting loan")

def returnloan():
    try:
        firstbooleanholder = False
        while not firstbooleanholder:
            for i in range(0,len(Libraryarray.biglist)):
                print(f"enter {i} to select the item called {Libraryarray.biglist[1][i][0]}")
            userchoice = input("")
            userchoice = int(userchoice)
            if type(userchoice) != "string" and len(userchoice) == 1 :
                firstbooleanholder = True
        Libraryarray.biglist[1][userchoice][-1].Returnloan()
    except TypeError:
        print("Error returning loan")

def runtimemenu():
    whileloopholder1 = False
    whileloopholder2 = False
    while not whileloopholder1:
        while not whileloopholder2:
            print("Welcome to Library Manager :)")
            print("Here you can check books in and out, as well as register books")
            print("To create a new item enter 1")
            print ("To Display all items details enter 2")
            print("To set a loan enter 3")
            print("To return a loan enter 4")
            print("To print a list enter 5")
            print("To print all lists enter 6")
            print("To show a single items details enter 7")
            print("To exit the program enter 8")
            print("enter the number corresponding to your choice below:")
            print("")
            userchoice = int(input(""))
            if userchoice <= 8 and userchoice >=1:
                whileloopholder2 = True
        if userchoice == 5:
            listdisplayfunction()
        elif userchoice == 4:
            returnloan()
        elif userchoice == 3:
            setloan()
        elif userchoice == 6:
            Libraryarray.printalllist()
        elif userchoice == 7:
            showsingledetailfunction()
        elif userchoice == 1:
            _newitem()
        elif userchoice == 2:
            showdetailfunction()
        elif userchoice == 8:
            whileloopholder1 = True
        userchoice = 0
        whileloopholder2 = False
        time.sleep(2)
        
        for i in range(0,3):
            print("")
            i += 1
        

         

def showdetailfunction():
    try:
        for i in range(0,len(len(Libraryarray.Booklist))):
            LibraryArray.Booklist[i].DisplayDetails()
    except TypeError:
        print("You need to add books to display the booklist")
    try:
        for i in range(0,len(Libraryarray.CDlist)):
            Libraryarray.CDlist[i].DisplayDetails()
    except TypeError:
        print("You need to add CDs to view the CDList")

def showsingledetailfunction():
    try:
        firstbooleanholder = False
        while not firstbooleanholder:
            for i in range(0,len(Libraryarray.biglist)):
                print(f"enter {i} to select the item called {Libraryarray.biglist[1][i][0]}")
            userchoice = input("")
            userchoice = int(userchoice)
            if type(userchoice) != "string" and len(userchoice) == 1 :
                firstbooleanholder = True
        Libraryarray.biglist[1][userchoice][-1].DisplayDetails()
    except TypeError:
        print("Please add items")



def listdisplayfunction():
    whileloopholder = False
    while not whileloopholder:
        print("To view the list of all items in the library enter 1, to view the list of all books in the library enter 2, to view the list of all cds in the library enter 3.")
        userinput = int(input(""))
        if userinput == 1 or userinput == 2  or userinput == 3:
            whileloopholder = True
    Libraryarray._printsinglelist(userinput)

def ISBNChecker(isben):
    ISBN = []
    for i in range(0,13):
        ISBN.append(isben)
    Calculateddigit = 0
    count = 0
    while count < 12:
        Calculateddigit = Calculateddigit + ISBN[count]
        count = count + 1
        Calculateddigit = Calculateddigit + ISBN[count] * 3
        count = count +1
    while Calculateddigit >= 10:
        Calculateddigit = Calculateddigit - 10
    Calculateddigit = 10 - Calculateddigit
    if Calculateddigit == 10:
        Calculateddigit = 0
    if Calculateddigit == ISBN[-1]:
        return True
    else:
        return False

runtimemenu()