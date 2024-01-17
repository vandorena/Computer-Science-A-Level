def ISBNChecker():
    ISBN = []
    for i in range(0,13):
        print("Enter next digit of ISBN")
        ISBNInput = int(input(""))
        ISBN.append(ISBNInput)
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
        print("Valid ISBN")
    else:
        print("Invalid ISBN")

ISBNChecker()