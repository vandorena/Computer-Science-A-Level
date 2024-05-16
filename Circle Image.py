from PIL import Image
import math
import random

image = Image.new("RGB",(200,200))

pixels = image.load()
colors = random.randint(0,200)
randoms = random.randint(0,3)
for r in range(0,100):
    if randoms == 3:
        color = (colors,r-50,r-100)
    elif randoms == 2:
        color = (r-50,colors,r-100)
    else:
        color = (random.randint(0,200),random.randint(0,200),random.randint(0,200))
    for a in range(0,36000):
        rad = math.radians(a/100)
        pixels[(int(r*math.cos(rad))+100),int(r*math.sin(rad)+100)] = color

image.show()