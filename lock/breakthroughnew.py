import random
import os
import datetime

def Main():
    ThisGame = Breakthrough()
    ThisGame.PlayGame()


        
class Breakthrough():
    def __init__(self):
        self.__Deck = CardCollection("DECK")
        self.__Hand = CardCollection("HAND")
        self.__Sequence = CardCollection("SEQUENCE")
        self.__Discard = CardCollection("DISCARD")
        self.__Score = 0
        self.__Locks = []
        self.__GameOver = False
        self.__CurrentLock = Lock()
        self.__LockSolved = False
        self.__LoadLocks()
        self.__MulliganUsed = False
    
    def FindDate(self):
        date = str(datetime.datetime.now())
        date = date.replace(" ","_")
        date = date.replace(":","-")
        date = date[:-7]
        return date
    
    def SaveGame(self):
        file = open(f"SaveGame{self.FindDate()}.txt","x")
        file.write(f"{self.__Score} \n")
        file.write(f"{self.__CurrentLock.FormatChallenges()} \n")
        file.write(f"{self.__CurrentLock.FormatChallengesMet()} \n" )
        file.write(f"{self.__Deck.FormatCards()} \n")
        file.write(f"{self.__Hand.FormatCards()} \n")
        file.write(f"{self.__Discard.FormatCards()} \n")
        file.close()
        return 

    def PlayGame(self):
        if len(self.__Locks) > 0:
            self.__SetupGame()
            while not self.__GameOver:
                self.__LockSolved = False
                while not self.__LockSolved and not self.__GameOver:
                    print()
                    print("Current score:", self.__Score)
                    print(self.__CurrentLock.GetLockDetails())
                    print(self.__Sequence.GetCardDisplay())
                    print(self.__Hand.GetCardDisplay())
                    MenuChoice = self.__GetChoice()
                    if MenuChoice == "D":
                        print(self.__Discard.GetCardDisplay())
                    elif MenuChoice == "S":
                        self.SaveGame()
                    elif MenuChoice =="Q":
                        print("Bye Bye")
                        print(f"Your Score is {self.__Score + self.__Deck.GetNumberOfCards()}")
                    elif MenuChoice == "M":
                        self.__CollectAllCards()
                        print("New Decks are:")
                        print(self.__CurrentLock.GetLockDetails())
                        print(self.__Sequence.GetCardDisplay())
                        print(self.__Hand.GetCardDisplay())
                    elif MenuChoice == "U":
                        CardChoice  = self.__GetCardChoice()
                        DiscardOrPlay = self.__GetDiscardOrPlayChoice()
                        if DiscardOrPlay == "D":
                            self.__MoveCard(self.__Hand, self.__Discard, self.__Hand.GetCardNumberAt(CardChoice - 1))
                            self.__GetCardFromDeck(CardChoice)
                        elif DiscardOrPlay == "P":
                            self.__PlayCardToSequence(CardChoice)
                    if self.__CurrentLock.GetLockSolved() or MenuChoice == "Q":
                        self.__LockSolved = True
                        self.__GameOver = True
                        self.__ProcessLockSolved()
                    self.__Deck.AllProbabilityState()
                    print(self.__CurrentLock.FormatChallenges())
                self.__GameOver = self.__CheckIfPlayerHasLost()
        else:
            print("No locks in file.")

    def _indefinet():
        while not KeyboardInterrupt:
            print("")
    def __ProcessLockSolved(self):
        self.__Score += 10
        print("Lock has been solved.  Your score is now:", self.__Score)
        while self.__Discard.GetNumberOfCards() > 0:
            self.__MoveCard(self.__Discard, self.__Deck, self.__Discard.GetCardNumberAt(0))
        self.__Deck.Shuffle()
        self.__CurrentLock = self.__GetRandomLock()

    def __CheckIfPlayerHasLost(self):
        if self.__Deck.GetNumberOfCards() == 0:
            print("You have run out of cards in your deck.  Your final score is:", self.__Score)
            return True
        else:
            return False
    
    def __SetupGame(self):
        Choice = input("Enter L to load a game from a file, anything else to play a new game:> ").upper()
        if Choice == "L":
            if not self.__LoadGame("game1.txt"):
                self.__GameOver = True
        else:
            self.__CreateStandardDeck()
            self.__Deck.Shuffle()
            for Count in range(5):
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))
            self.__AddDifficultyCardsToDeck()
            self.__Deck.Shuffle()
            self.__CurrentLock = self.__GetRandomLock()
    
    def __PlayCardToSequence(self, CardChoice):
        if self.__Sequence.GetNumberOfCards() > 0:
            if self.__Hand.GetCardDescriptionAt(CardChoice - 1)[0] != self.__Sequence.GetCardDescriptionAt(self.__Sequence.GetNumberOfCards() - 1)[0]:
                self.__Score += self.__MoveCard(self.__Hand, self.__Sequence, self.__Hand.GetCardNumberAt(CardChoice - 1))
                self.__GetCardFromDeck(CardChoice)
        else:
            self.__Score += self.__MoveCard(self.__Hand, self.__Sequence, self.__Hand.GetCardNumberAt(CardChoice - 1))
            self.__GetCardFromDeck(CardChoice)
        if self.__CheckIfLockChallengeMet():
            print()
            print("A challenge on the lock has been met.")
            print()
            self.__Score += 5

    def __CollectAllCards(self):
        self.__MulliganUsed = True
        newdeck = CardCollection("Temp")
        cur_deck_cards = self.__Deck.GetNumberOfCards()-1
        cur_sequence_cards = self.__Sequence.GetNumberOfCards()-1
        cur_hand_cards = self.__Hand.GetNumberOfCards()-1
        cur_discard_cards = self.__Discard.GetNumberOfCards()-1
        for i in range(0,cur_deck_cards):
            newdeck._Cards.append(self.__Deck._Cards.pop())
        for i in range(0,cur_sequence_cards):
            newdeck._Cards.append(self.__Sequence._Cards.pop())
        for i in range(0,self.__Hand.GetNumberOfCards()-1):
            newdeck._Cards.append(self.__Hand._Cards.pop())
        for i in range(0,self.__Discard.GetNumberOfCards()-1):
            newdeck._Cards.append(self.__Discard._Cards.pop())
        newdeck.Shuffle()
        for i in range(0,cur_hand_cards):
            current_card = newdeck._Cards.pop()
            if current_card._CardType == "Dif":
                self.__Discard._Cards.append(current_card)
                cur_discard_cards = cur_discard_cards-1
                cur_hand_cards= cur_hand_cards-1
            else:
                self.__Hand._Cards.append(current_card)
        for i in range(0,cur_deck_cards):
            self.__Deck._Cards.append(newdeck._Cards.pop())
        for i in range(0,cur_sequence_cards):
            self.__Sequence._Cards.append(newdeck._Cards.pop())
        for i in range(0,cur_discard_cards):
            self.__Discard._Cards.append(newdeck._Cards.pop())
        



    def __CheckIfLockChallengeMet(self):
        SequenceAsString = ""
        for Count in range(self.__Sequence.GetNumberOfCards() - 1, max(0, self.__Sequence.GetNumberOfCards() - 3) -1, -1):
            if len(SequenceAsString) > 0:
                SequenceAsString = ", " + SequenceAsString
            SequenceAsString = self.__Sequence.GetCardDescriptionAt(Count) + SequenceAsString
            if self.__CurrentLock.CheckIfConditionMet(SequenceAsString):
                return True
        return False
    
    def __SetupCardCollectionFromGameFile(self, LineFromFile, CardCol):
        if len(LineFromFile) > 0:
            SplitLine = LineFromFile.split(",")
            for Item in SplitLine:
                if len(Item) == 5:
                    CardNumber = int(Item[4])
                else:
                    CardNumber = int(Item[4:6])
                if Item[0: 3] == "Dif":
                    CurrentCard = DifficultyCard(CardNumber)
                    CardCol.AddCard(CurrentCard)
                else:
                    CurrentCard = ToolCard(Item[0], Item[2], CardNumber)
                    CardCol.AddCard(CurrentCard)
    
    def __SetupLock(self, Line1, Line2):
        SplitLine = Line1.split(";")
        for Item in SplitLine:
            Conditions = Item.split(",")
            self.__CurrentLock.AddChallenge(Conditions)
        SplitLine = Line2.split(";")
        for Count in range(0, len(SplitLine)):
            if SplitLine[Count] == "Y":
                self.__CurrentLock.SetChallengeMet(Count, True)
    
    def __LoadGame(self, FileName):
        try:
            with open(FileName) as f:          
                LineFromFile = f.readline().rstrip()
                self.__Score = int(LineFromFile)
                LineFromFile = f.readline().rstrip()
                LineFromFile2 = f.readline().rstrip()
                self.__SetupLock(LineFromFile, LineFromFile2)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Hand)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Sequence)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Discard)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Deck)
                return True
        except:
            print("File not loaded")
            return False

    def __LoadLocks(self):
        FileName = "locks.txt"
        self.__Locks = []
        try:
            with open(FileName) as f: 
                LineFromFile = f.readline().rstrip()
                while LineFromFile != "":
                    Challenges = LineFromFile.split(";")
                    LockFromFile = Lock()
                    for C in Challenges:
                        Conditions = C.split(",")
                        LockFromFile.AddChallenge(Conditions)
                    self.__Locks.append(LockFromFile)
                    LineFromFile = f.readline().rstrip()
        except:
            print("File not loaded")
        
    def __GetRandomLock(self):
        return self.__Locks[random.randint(0, len(self.__Locks) - 1)]

    def __GetCardFromDeck(self, CardChoice):
        if self.__Deck.GetNumberOfCards() > 0:
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":
                CurrentCard = self.__Deck.RemoveCard(self.__Deck.GetCardNumberAt(0))
                print()
                print("Difficulty encountered!")
                print(self.__Hand.GetCardDisplay())
                self.__Deck.DisplayStats()
                print("To deal with this you need to either lose a key ", end='')
                Choice = input("(enter 1-5 to specify position of key) or (D)iscard five cards from the deck:> ")
                print()
                self.__Discard.AddCard(CurrentCard)
                CurrentCard.Process(self.__Deck, self.__Discard, self.__Hand, self.__Sequence, self.__CurrentLock, Choice, CardChoice)
        while self.__Hand.GetNumberOfCards() < 5 and self.__Deck.GetNumberOfCards() > 0:
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":
                self.__MoveCard(self.__Deck, self.__Discard, self.__Deck.GetCardNumberAt(0))
                print("A difficulty card was discarded from the deck when refilling the hand.")
            else:
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))
        if self.__Deck.GetNumberOfCards() == 0 and self.__Hand.GetNumberOfCards() < 5:
            self.__GameOver = True

    def __GetCardChoice(self):
        Choice = None
        while Choice is None:
            try: 
                Choice = int(input("Enter a number between 1 and 5 to specify card to use:> "))
            except:
                pass
        return Choice

    def __GetDiscardOrPlayChoice(self):
        Choice = input("(D)iscard or (P)lay?:> ").upper()
        return Choice

    def __GetChoice(self):
        print()
        if self.__MulliganUsed:
            Choice = input("(D)iscard inspect, (U)se card, (S)ave Game:> ").upper()
        else:
            Choice = input("(D)iscard inspect, (U)se card, (M)ulligan, (S)ave Game:> ").upper()
        return Choice
    
    def __AddDifficultyCardsToDeck(self):
        for Count in range(5):
            self.__Deck.AddCard(DifficultyCard())

    def __CreateStandardDeck(self):
        for Count in range(5):
            NewCard = ToolCard("P", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "c")
            self.__Deck.AddCard(NewCard)
        for Count in range(3):
            NewCard = ToolCard("F", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "c")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "c")
            self.__Deck.AddCard(NewCard)
    
    def __MoveCard(self, FromCollection, ToCollection, CardNumber):
        Score  = 0
        if FromCollection.GetName() == "HAND" and ToCollection.GetName() == "SEQUENCE":
            CardToMove = FromCollection.RemoveCard(CardNumber)
            if CardToMove is not None:
                ToCollection.AddCard(CardToMove)
                Score = CardToMove.GetScore()
        else:
            CardToMove = FromCollection.RemoveCard(CardNumber)
            if CardToMove is not None:
                ToCollection.AddCard(CardToMove)
        return Score

class Challenge():
    def __init__(self):
        self._Met = False
        self._Condition = []
    
    def GetMet(self): 
        return self._Met

    def GetCondition(self):
        return self._Condition

    def SetMet(self, NewValue):
        self._Met = NewValue

    def SetCondition(self, NewCondition):
        self._Condition = NewCondition

class Lock():
    def __init__(self):
        self._Challenges = []
        
    def AddChallenge(self, Condition):
        C = Challenge()
        C.SetCondition(Condition)
        self._Challenges.append(C)

    def FormatChallenges(self):
        string = ""
        for i in range(0,len(self._Challenges)):
            for j in range(0,len(self._Challenges[i].GetCondition())):
                string += f"{self._Challenges[i].GetCondition()[j]},"
            string == f";"
        string = string[:-1]
        return string

    def __ConvertConditionToString(self, C):
        ConditionAsString = ""
        for Pos in range(0, len(C) - 1):
            ConditionAsString += C[Pos] + ", "
        ConditionAsString += C[len(C) - 1]
        return ConditionAsString

    def GetLockDetails(self):
        LockDetails = "\n" + "CURRENT LOCK" + "\n" + "------------" + "\n"
        for C in self._Challenges:
            if C.GetMet():
                LockDetails += "Challenge met: "
            else:
                LockDetails += "Not met:       "
            LockDetails += self.__ConvertConditionToString(C.GetCondition()) + "\n"
        LockDetails += "\n"
        return LockDetails

    def GetLockSolved(self):
        for C in self._Challenges:
            if not C.GetMet():
                return False
        return True
    
    def CheckIfConditionMet(self, Sequence):
        for C in self._Challenges:
            if not C.GetMet() and Sequence == self.__ConvertConditionToString(C.GetCondition()):
                C.SetMet(True)
                return True
        return False

    def SetChallengeMet(self, Pos, Value):
        self._Challenges[Pos].SetMet(Value)

    def FormatChallengesMet(self):
        string = ""
        for c in range(0,len(self._Challenges)):
            string +=  str(self._Challenges[c].GetMet())[0] + ";"
        string = string[:-1]
        string = string.replace("T", "Y")
        string = string.replace("F","N")
        return string
    
    def GetChallengeMet(self, Pos): 
        return self._Challenges[Pos].GetMet()
    
    def GetNumberOfChallenges(self): 
        return len(self._Challenges)

class Card():
    _NextCardNumber = 0
    
    def __init__(self):
        self._CardNumber = Card._NextCardNumber
        Card._NextCardNumber += 1
        self._Score = 0

    def GetScore(self):
        return self._Score

    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        pass

    def GetCardNumber(self): 
        return self._CardNumber

    def GetDescription(self):
        if self._CardNumber < 10:
            return " " + str(self._CardNumber)
        else:
            return str(self._CardNumber)

class ToolCard(Card):
    def __init__(self, *args):
        self._ToolType = args[0]   
        self._Kit = args[1]
        if len(args) == 2:
            super(ToolCard, self).__init__()
        elif len(args) == 3:
            self._CardNumber = args[2]
        self.__SetScore()
        
    def __SetScore(self):
        if self._ToolType == "K":
            self._Score = 3
        elif self._ToolType == "F":
            self._Score = 2
        elif self._ToolType == "P":
            self._Score = 1
            
    def GetDescription(self):
        return self._ToolType + " " + self._Kit

class DifficultyCard(Card):
    def __init__(self, *args):
        self._CardType = "Dif"   
        if len(args) == 0:
            super(DifficultyCard, self).__init__()
        elif len(args) == 1:
            self._CardNumber = args[0]
        
    def GetDescription(self):
        return self._CardType

    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        ChoiceAsInteger = None
        try:
            ChoiceAsInteger = int(Choice)
        except:
            pass
        if ChoiceAsInteger is not None:
            if ChoiceAsInteger >= 1 and ChoiceAsInteger <= 5:
                if ChoiceAsInteger >= CardChoice:
                    ChoiceAsInteger -= 1
                if ChoiceAsInteger > 0:
                    ChoiceAsInteger -= 1
                if Hand.GetCardDescriptionAt(ChoiceAsInteger)[0] == "K":
                    CardToMove = Hand.RemoveCard(Hand.GetCardNumberAt(ChoiceAsInteger))
                    Discard.AddCard(CardToMove)
                    return
        Count = 0
        while Count < 5 and Deck.GetNumberOfCards() > 0:
            CardToMove = Deck.RemoveCard(Deck.GetCardNumberAt(0))
            Discard.AddCard(CardToMove)
            Count += 1

class CardCollection():
    def __init__(self, N):
        self._Name = N
        self._Cards = []
        self._starterX = 0
        self._starterY = 0
        self._starterZ = 0
        self._NumPicks = 0
        self._NumFiles = 0
        self._NumKeys = 0
#New
    def ToolCardCheckerUpdater(self,c):
        if c.GetDescription()[0] == "K":
            self._NumKeys += 1
        elif c.GetDescription()[0] == "F":
            self._NumKeys += 1
        elif c.GetDescription()[0] == "P":
            self._NumKeys += 1
        return

    def ToolCardCheckerRemover(self,c):
        if c.GetDescription()[0] == "K":
            self._NumKeys -= 1
        elif c.GetDescription()[0] == "F":
            self._NumKeys -= 1
        elif c.GetDescription()[0] == "P":
            self._NumKeys -= 1
        return

    def FormatCards(self):
        string = ""
        for c in self._Cards:
            string += "".join(c.GetDescription())+";"
        string = string[:-1]
        return string

    def NumberState(self,x):
        cardsInState = 0
        for i in range(0,self.GetNumberOfCards()-1):
            if self._Cards[i].GetDescription()[0] == x:
                cardsInState += 1
        if x == "X" and self._starterX == 0:
            self._starterX = cardsInState
        elif x == "Y" and self._starterY == 0:
            self._starterY = cardsInState
        elif x == "Z" and self._starterZ == 0:
            self._starterZ = cardsInState
        return cardsInState
    
    def ProbabilityState(self,x):
        numerator = self.NumberState(x)
        result = 0
        if x == "X" and self._starterX != 0:
            result = (numerator / self._starterX)*100
        elif x == "Y" and self._starterY != 0:
            result = (numerator / self._starterY)*100
        elif x == "Z" and self._starterZ != 0:
            result = (numerator / self._starterZ)*100
        string_result = f"The Percentage of getting a {x} cards remaining is {result:.1f}%"
        return string_result
    
    def AllProbabilityState(self):
        print(self.ProbabilityState("X"))
        print(self.ProbabilityState("Y"))
        print(self.ProbabilityState("Z"))
        return


    
    def DisplayStats(self):
        print(f"The probability of picking a Key is {(self._NumKeys/self.GetNumberOfCards())*100 :.2f}%")
        print(f"The probability of picking a File is {(self._NumFiles/self.GetNumberOfCards())*100 :.2f}%")
        print(f"The probability of picking a Pick is {(self._NumPicks/self.GetNumberOfCards())*100 :.2f}%")
    
#-----   

    def GetName(self):
        return self._Name

    def GetCardNumberAt(self, X):
        return self._Cards[X].GetCardNumber()

    def GetCardDescriptionAt(self, X):
        return self._Cards[X].GetDescription()

    def AddCard(self, C):
        self._Cards.append(C)
        self.ToolCardCheckerUpdater(C)
    
    def GetNumberOfCards(self): 
        return len(self._Cards)

    def Shuffle(self):
        for Count in range(10000):
            RNo1 = random.randint(0, len(self._Cards) - 1)
            RNo2 = random.randint(0, len(self._Cards) - 1)
            TempCard = self._Cards[RNo1]
            self._Cards[RNo1] = self._Cards[RNo2]
            self._Cards[RNo2] = TempCard

    def RemoveCard(self, CardNumber):
        CardFound  = False
        Pos  = 0
        while Pos < len(self._Cards) and not CardFound:
            if self._Cards[Pos].GetCardNumber() == CardNumber:
                CardToGet = self._Cards[Pos]
                CardFound = True
                self._Cards.pop(Pos)
            Pos += 1
        self.ToolCardCheckerRemover(CardToGet)
        return CardToGet

    def __CreateLineOfDashes(self, Size):
        LineOfDashes = ""
        for Count in range(Size):
            LineOfDashes += "------"
        return LineOfDashes
    
    def GetCardDisplay(self):
        CardDisplay = "\n" + self._Name + ":"
        if len(self._Cards) == 0:
            return CardDisplay + " empty" + "\n" + "\n"
        else:
            CardDisplay += "\n" + "\n"
        LineOfDashes = ""
        CARDS_PER_LINE  = 10
        if len(self._Cards) > CARDS_PER_LINE:
            LineOfDashes = self.__CreateLineOfDashes(CARDS_PER_LINE)
        else:
            LineOfDashes = self.__CreateLineOfDashes(len(self._Cards))
        CardDisplay += LineOfDashes + "\n"
        Complete = False
        Pos  = 0
        while not Complete:
            CardDisplay += "| " + self._Cards[Pos].GetDescription() + " "
            Pos += 1
            if Pos % CARDS_PER_LINE == 0:
                CardDisplay += "|" + "\n" + LineOfDashes + "\n"
            if Pos == len(self._Cards):
                Complete = True
        if len(self._Cards) % CARDS_PER_LINE > 0:
            CardDisplay += "|" + "\n"
            if len(self._Cards) > CARDS_PER_LINE:
                LineOfDashes = self.__CreateLineOfDashes(len(self._Cards) % CARDS_PER_LINE)
            CardDisplay += LineOfDashes + "\n"
        return CardDisplay

if __name__ == "__main__":
    Main()