
class carreg:
    def carregsplitter(carreg):
        splittedlist = []
        for i in range(0,len(carreg)): 
            splittedlist.append(carreg[i])
        return splittedlist

    def checkupper(character):
        checkup = character.isupper()
        return checkup

    def checklower(character):
        checkup = character.islower()
        return checkup

    def checknumber(character):
        checkup = character.isnumeric()
        return checkup
    
    def isspace(character):
        if character == " ":
            return True
        else:
            return False

    def carregcheck(carlistchar):
        check = True
        while check == True:
            for i in range (0,1):
                check = carreg.checkupper(carlistchar[i])
                if check == False:
                    return check
            for i in range (0,1):
                check = carreg.checknumber(carlistchar[i+2])
                if check == False:
                    return check
            check = carreg.isspace(carlistchar[4])
            if check == False:
                return check
            for i in range (0,2):
                check = carreg.checkupper(carlistchar[i+5])
            if check == False:
                return check
            return check
        return check

carregis = input("Input your cars registration: ")
carregis = carreg.carregsplitter(carregis)
if carreg.carregcheck(carregis) == True:
    print(f"the registration you entered is correctly formatted")
else:
    print(f"You inputted the numberplate wrong")