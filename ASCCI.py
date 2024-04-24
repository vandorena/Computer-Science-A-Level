from PIL import Image
from random import randint
back_image = Image.open("ayo.webp")#input background
back_image = back_image.convert("HSV")
back_image = Image.Image.resize(back_image,size=[100,100])
back_image_pixels = back_image.load()
listt = []

for y in range(0,back_image.size[0]):
    listappend = []
    for x in range(0,back_image.size[1]):
        if x == 0 and y==0:
            hsv_bounds = back_image_pixels[x,y]
            bright_lower_1 = hsv_bounds[2]-40
            bright_higher_1 = hsv_bounds[2]+30
            bright_higher_2 = hsv_bounds[2]+80
        if back_image_pixels[x,y][2] > bright_lower_1 and back_image_pixels[x,y][2] < bright_higher_1:
            listappend.append("/")
        elif back_image_pixels[x,y][2] <= bright_lower_1:
            listappend.append(".")
        elif back_image_pixels[x,y][2] >= bright_higher_1 and back_image_pixels[x,y][2] < bright_higher_2:
            listappend.append("#")
        else:
            listappend.append("@")
    listt.append(listappend)

file = open("asciiview.txt", "w")
for i in range(0,len(listt)):
    cur_string = ""
    for x in range(0,len(listt[i])):
        cur_string+=listt[i][x]
    file.write(cur_string)
    file.write("\n")
file.close()
        