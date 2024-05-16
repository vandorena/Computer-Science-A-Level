from PIL import Image
from random import randint
image = Image.open("dinghy.jpg")

#image.show()
#print(f"Format: {image.format} size {image.size} mode {image.mode}")

grainlevel = int(input())
new_image  = Image.new("RGB", (image.size[0],image.size[1]))
pixels = image.load()
pixelother = new_image.load()
list_of_values = []
for y in range(image.size[1]-1):
    for x in range(image.size[0]-1):
        rgb = pixels[x,y]
        print(rgb)
        #pixelother[y-1,x] = rgb
        pixelother[x,y] = (int(rgb[0]*(randint(1,grainlevel)**-1)),int(rgb[1]*0.78*(randint(1,grainlevel)**-1)),int(rgb[2]*(randint(1,grainlevel)**-1)))
                                                                                                    

new_image.show()
print(f"{new_image.size}")
