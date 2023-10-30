import re

def verticiemaker(nameofnode):
   verticiereturnlist = []
   node1infunction = input("Enter the name of the first node of the verticie: ")
   node2infunction = input("Enter the name of the second node of the verticie: ")
   reversible = int(input("Enter 1 if the verticie is two way: "))
   nameofnode = Verticie(node1infunction,node2infunction,reversible)
   verticiereturnlist.append(nameofnode)

class Nodedictionary:
    def __init__(self):
      Nodedictionary.data = []
    
    def adddictionary(self,node):
       Nodedictionary.data.append(node.nodename)



class Node:
    
    def __init__(self,name):
       Node.linkednodes = []
       Node.nodename = str(name)
       Nodedictionary.adddictionary(self)
    
    def addverticies(self):
      numberverticies = int(input("How many nodes do you want to add?"))
      for i in range (1,numberverticies):
         nameofnewnode = input("What do you want to call this new Verticie to be called?: ")
         verticiemaker(nameofnewnode)
                  



class Verticie:
   
   def __init__(self,node1,node2,reversible):
      Verticie.node1 = node1
      Verticie.node2 = node2
      if reversible == 1:
         Verticie(node2, node1, 0)

def createnode(newnodename):
   newnode = Node(str(newnodename))
   newnode.addverticies()


      

hello = Node("street1")
print(hello.nodename)
createnode("happy")