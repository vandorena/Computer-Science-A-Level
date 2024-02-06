word1 = input("Enter Word One: ")
word2 = input("Enter Word Two: ")
alphabetlist = [["A",None],["B", None],["C",None],["D", None],["E",None],["F", None],["G",None],["H", None],["I",None],["J", None],["K",None],["L", None],["M",None],["N", None],["O",None],["P", None],["Q",None],["R", None],["S",None],["T", None],["U",None],["V", None],["W",None],["X", None],["Y",None],["Z", None]]
alphabetlist2 = [["A",None],["B", None],["C",None],["D", None],["E",None],["F", None],["G",None],["H", None],["I",None],["J", None],["K",None],["L", None],["M",None],["N", None],["O",None],["P", None],["Q",None],["R", None],["S",None],["T", None],["U",None],["V", None],["W",None],["X", None],["Y",None],["Z", None]]

for i in range(0,len(word1)):
    for j in range(0,len(alphabetlist)):
        if word1[i] == alphabetlist[j][0]:
            alphabetlist[j][1] += 1

for i in range(0,len(word2)):
    for j in range(0,len(alphabetlist2)):
        if word2[i] == alphabetlist2[j][0]:
            alphabetlist2[j][1] += 1

trop = True
for i in range(0,26):
    if alphabetlist2[i][1] != alphabetlist[i][1]:
        print("Its not there")
        trop = False
if trop:
    print("Its in there")