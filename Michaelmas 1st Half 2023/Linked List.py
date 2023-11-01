class Node:
    def __init__(self, data):
        self._data = data
        self._next_node = 0

    def get_data():
        return self._data

    def set_next_node(self, new_node):
        self._next_node = new_node
        return

        

class Stack:
    def __init__(self):
        self._data = []
        self._head_node = len(self._data)
        self._size = len(self._data)

    def push_to_stack(self, string):
        string = Node(string)
        string.set_next_node(self._head_node)
        self._data.append(string)
        self._size +=1
        return
    
    def pop_off_stack(self):
        returnnode = self._data[self._head_node]
        self._head_node = returnnode._next_node
        self._size -= 1
        return returnnode

    def return_size(self):
        return self._size
    
    def __str__(self):
        stringappendlist = ""
        for i in range (0,self._size):
            stringappendlist = stringappendlist + (self._data[i]._data)
        return stringappendlist
    
    def print_topofstack(self):
        print(self._data[self._head_node]._data)
stackofnodes = Stack()
done = False 
end = False
while end == False:
    while done == False:
        print("To add a new thing enter 1, to remove something enter 2, to print enter 3, to print the top of the list enter 4, to leave enter 5")
        choice = int(input("Enter here:  "))
        if choice > 0 and choice <6:
            done = True
    if choice == 1:
        stackofnodes.push_to_stack(input("Input what you want to add:   "))
    if choice == 2:
        stackofnodes.pop_off_stack()
    if choice == 3:
        print(stackofnodes)
    if choice == 4:
        stackofnodes.print_topofstack()
    if choice == 5:
        end = True
