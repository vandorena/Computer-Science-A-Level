
name_list = ['Ed', 'William', 'Toby', 'Freddie', 'Rohan', 'Ian', 'Matthew', 'Gavin', 'Lenny', 'Thomas', 'Jake']


for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)

print(f"the third name is {name_list[2]}")
print(f"The last seven names are: ")
for i in range (0,7):
    print(name_list.pop())