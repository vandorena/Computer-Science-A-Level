BAD_WORDS = ['poo', 'frack', 'poppycock', 'dunderhead', 'lordy']

def censor(sentence: str):
   sentence = sentence.split()
   for i in range(0,len(sentence)):
      if sentence[i].lower() in BAD_WORDS:
         letter_count = len(sentence[i]) - 2
         sentence[i] = sentence[i][0] + "*"*letter_count + sentence[i][-1]
      else:
         count =0
         try:
            for j in range(0,len(sentence[i])):
                for x in range(0,len(BAD_WORDS)):
                    if sentence[i][j] == BAD_WORDS[x][j]:
                        count +=1
                    elif i != 0 and sentence[i][j] == BAD_WORDS[x][j-1]:
                        count +=1
                    elif i != len(sentence[i]) and sentence[i][j] == BAD_WORDS[x][j+1]:
                        count +=1
         except IndexError:
            count = 0
         if count > 0.75*len(sentence):
            letter_count = len(sentence[i]) - 2
            sentence[i] = sentence[i][0] + "*"*letter_count + sentence[i][-1]
            
   for i in range(0,len(sentence)):
      if i == 0:
         result = sentence[i]
      #elif i == len(sentence) -1:
       #  result += " " + sentence[i] +"."
      else:
         result += " " + sentence[i]
   return result
    