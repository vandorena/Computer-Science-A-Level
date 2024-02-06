word_one = input("Input the first word: ")
word_two = input("Input the second word: ")
length_word_one = len(word_one)
word_one_match_counter = 0
word_one_list = []
word_two_list = []
for i in range(0,len(word_two)):
    word_two_list.append(word_two[i])
for i in range(0,len(word_one)):
    word_one_list.append(word_one[i])
holder = False
while not holder:
    for i in range(0,len(word_one_list)):
        halter = False
        while not halter:
            for j in range(0,len(word_two_list)):
                try:
                    if word_one_list[-i] == word_two_list[-j]:
                        word_two_list.pop()
                        word_one_list.pop()
                        if len(word_one_list) == 0:
                            print("Word one can be made up of word two's letters ")
                            holder = True
            
                except IndexError:
                    halter = True
print("ignore if already validitated")
print("Word one cannot be made up of letters from word two")
