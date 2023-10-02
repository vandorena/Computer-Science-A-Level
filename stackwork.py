import random
def createstack(nameofstack):
    nameofstack = []
    return nameofstack
def appendtostack(nameofstack,appenditem):
    nameofstack.append(appenditem)
    return
def popoffstack(nameofstack):
    if len(nameofstack) > 1:
        item = nameofstack.pop()
        print (f"{item} has been removed from stack")
    else:
        print (f"stack consists of one item which is {nameofstack}")


#def weirdwaytostackappend(stack,stackheight,appendeditem):
 #   stacklen = len(stack)
  #  if stacklen < stackheight:
   #     stack[stacklen] = appendeditem
    #else:
     #   print("stack full")
    #return stack
#def weirdwaytostackpop(stack,amountofpop):
 #   if len(stack) > 0:
  #      for i in range(0,amountofpop):
  #          returneditem = stack(-i)
  #  else:
  #      print("stack empty")

#stack  = []
#stackheight = 100
#for i in range(0,70):
 #   weirdwaytostackappend(stack,stackheight,random.randint(0,10000))
#weirdwaytostackpop(stack, 8)

coolman = []
createstack(coolman)
for i in range (1, random.randint(20,1000000)):
    appendtostack(coolman, random.randint(10,12302132))
for i in range (0,len(coolman)):
    popoffstack(coolman)