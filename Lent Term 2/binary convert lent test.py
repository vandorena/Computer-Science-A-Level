def convert_to_binary():
    holder_list = []
   
    number = int(input("Input a decimal number, which you would like to convert into binary:  "))
    while number != 0:
        current_result = number // 2
        if current_result != (number/2):
            holder_list.append("1")
           
        else:
            holder_list.append("0")
            
        number = current_result
    #print(holder_list)
    output = ""
    while len(holder_list) != 0:
        output += holder_list.pop()
    print(output)
    return

convert_to_binary()