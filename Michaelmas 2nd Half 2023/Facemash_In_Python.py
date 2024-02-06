# note this is just to try to recreate facemash (Predecessor to facebook)
import re as regex

class Person:
    def __init__(self,name):
        self.attractive_index = 0
        self._name = ""
        self.rank = 0
        self._picture = name
    
    def _rankup(self, increase):
        self.rank += increase

class List:
    def __init__(self):
        self.data = []
    

class Match:



def person_maker():
    name_pattern = "[A-Z][a-z]* [A-Z]?|[a-z]*"
    name_string_check = False
    while not name_string_check:
        print("What is their name?")
        name = input("")
        match_check = regex.match(name_pattern,name)
        if match_check == True:
            name_string_check = True
            print ("yea")

person_maker()

