def checker(number,list,base):
    
    if base ==2:
        if (number // 2) == 0:
            #print (list)
            return
        else:
            holder = number % 2
            number = number // 2
            list.append(holder)
            checker(number,list,2)
            return list
    elif base == 16:
        if (number // base) == 0:
            return
        else:
            holder = number % 16
            number = number // 2
            if holder > 9:
                if holder == 10:
                    holder = "A"
                elif holder == 11:
                    holder = "B"
                elif holder == 12:
                    holder = "C"
                elif holder == 13:
                    holder = "D"
                elif holder == 14:
                    holder  = "E"
                elif holder == 15:
                    holder = "F"
            list.append(str(holder))
            checker(number,list,16)
            return list


def reverser(list):
    holder = []
    while len(list) != 0:
        temp = list.pop()
        holder.append(temp)
    return holder

number = int(input("input a decimal number"))
list = []
choice = int(input("For Binary Enter, 2 for Hex enter 1:"))
if choice == 2:
    print(f"Your Decimal Number in Binary is {reverser(checker(number,list,2))}")
else:
    print(f"Your Decimal Number in HEX is {reverser(checker(number,list,16))}")
    