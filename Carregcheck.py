
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
        check = carreg.checkupper(carlistchar[0])
        check = carreg.checkupper(carlistchar[1])
        check = carreg.checknumber(carlistchar[2])
        check = carreg.checknumber(carlistchar[3])
        check = carreg.isspace(carlistchar[4])
        check = carreg.checkupper(carlistchar[5])
        check = carreg.checkupper(carlistchar[6])
        check = carreg.checkupper(carlistchar[7])
        return check
    return check

carregis = input("Input your cars registration: ")
carregis = carreg.carregsplitter(carregis)
if carregcheck(carregis) == True:
    print(f"the registration you entered is correctly formatted")
else:
    print(f"You inputted the numberplate wrong")