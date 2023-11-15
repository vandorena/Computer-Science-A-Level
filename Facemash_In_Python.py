# note this is just to try to recreate facemash (Predecessor to facebook)
import re as regex

class Person:
    def __init__(self,name):
        self.attractive_index = 0
        self._name = ""
        self.rank = 0
        self._picture = name

class List:
    def __init__(self):
        self.data = []

    def new_match(self,Person_1,Person_2):
        match = [Person_1,Person_2]
        self.data.append(match)


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

