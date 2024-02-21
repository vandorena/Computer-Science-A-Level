holder = False
while not holder:
    correct = False
    while not correct:
        try:
            fractionalnumber = float(input("Enter a decimal float"))
            correct = True
        except ValueError:
            pass
    binarystr = ""
    Fholder = fractionalnumber
    Rholder = Fholder
    count = 0
    while count < 10:
        Rholder = Rholder*2
        stringRholder = str(Rholder)
        binarystr += stringRholder[0]
        if stringRholder[0] == "1":
            Rholder = float(stringRholder[0:])
            Fholder = Rholder
        else:
            Fholder = Rholder
        count += 1
    print(binarystr)

