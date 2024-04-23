from PIL import Image
from random import randint
chroma_image = Image.open("")#input
back_image = Image.open("")#output

image = Image.new("HSV",(500,500))
image = chroma_image.convert("HSV")
image = image.resize(back_image.size)
chroma_pixels = image.load()
back_image = back_image.convert("HSV")
back_image_pixels = back_image.load()
for x in range(0,image.size[0]):
    for y in range(0,image.size[1]):
        if x == 0 and y==0:
            hsv_bounds = chroma_pixels[x,y]
            hue_lower = hsv_bounds[0]-20
            hue_higher = hsv_bounds[0]+20
            sat_lower = hsv_bounds[1]-50
            sat_higher = hsv_bounds[1] + 50
            bright_lower = hsv_bounds[2]-100
            bright_higher = hsv_bounds[2]+100
        if chroma_pixels[x,y][0] > hue_lower and chroma_pixels[x,y][0] < hue_higher and chroma_pixels[x,y][1] > sat_lower and chroma_pixels[x,y][1] < sat_higher and chroma_pixels[x,y][2] > bright_lower and chroma_pixels[x,y][2] < bright_higher:
            back_image_pixels[x,y] != chroma_pixels[x,y]
        else:
            back_image_pixels[x,y] = chroma_pixels[x,y]

back_image.show()

