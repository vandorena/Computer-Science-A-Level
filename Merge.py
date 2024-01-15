#def merge_sort(Array1,Array2):
#    array = [0] * (len(Array1) + len (Array2))
 #   i = 0
  #  j = 0
   # sorted_array = False
    #while sorted_array == False:
     #   if Array1[i] >= Array2[j]:
      #      array.append(Array1[i])
       #     i = i + 1
        #else:
         #   array.append(Array2[j])
          #  j = j + 1
   #     if len(array) == (len(Array1) + len(Array2)):
    #        sorted_array = True
     #       
   # print(array)

#ar1 = [ 6,9,10]
#ar2 = [2,5,9,11]
#merge_sort(ar1,ar2)


def merge_function(list1 :list,list2 :list,mergedlist:list):
    i = 0
    j = 0
    while (i + j) < len(mergedlist):
        if j == len(list2) or (i < len(list1) and list1[i] < list2[j]):
            mergedlist[i + j] = list1[i]
            i = i + 1
        else:
            mergedlist[i + j] = list2[j]

