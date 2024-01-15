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
            j = j + 1


def merge_sort(list_to_sort: list):
    length_of_list = len(list_to_sort)
    if length_of_list == (1 or 0):
        return
    half_length_list = length_of_list // 2
    List1 = [: half_length_list]
    List2 = [half_length_list :]
    merge_sort(List1)
    merge_sort(List2)
    merge_function(List1,List2,list_to_sort)

