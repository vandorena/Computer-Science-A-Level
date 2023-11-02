import re

class Node:
    
    def __init__(self,name):
       Node.linkednodes = []
       Node.nodename = str(name)
    
    def addlinkednodes(self):
      numberlinkednodes = int(input("How many nodes do you want to add?"))
      for i in range(1,numberlinkednodes):
        happy = True
        nameholder = input("Enter the name of the corresponding node")
        weightholderstr = input("enter the distance between the node and the linked node")
        unpackedweightholder = [*weightholderstr]
        searchweightholder = re.search("[^0-9]", weightholderstr)
        while happy is not False:
            if searchweightholder == None:
               happy = True
            else:
               for i in range(0,len(searchweightholder)):
                  
                  unpackedweightholder.remove[searchweightholder[i]]

        weightholderstr = ""
        weightholderstr = weightholderstr.join(unpackedweightholder)
        print(weightholderstr)
                  




def createnode(newnodename):
   newnode = Node(str(newnodename))
   newnode.addlinkednodes()
   

hello = Node("street1")
print(hello.nodename)
print(hello.linkednodes)
createnode("happy")