from PIL import Image


## Open the images in grayscale mode (i.e.black and white)

# original_image = Image.open("landscape.png").convert('L')
original_image = Image.open("car.jpg").convert('L')
original_image = Image.open("car.jpg").convert('L')

print(original_image.format, original_image.size, original_image.mode)

width, height = original_image.size
modified_image = Image.new('L', original_image.size)
edge_image = Image.new('L', original_image.size)


pixels = original_image.load()          # The original image
modified_pixels = modified_image.load() # Applying the "convolution"
edge_pixels = edge_image.load()         # Just looking at edges

for y in range(1, height - 1):
    for x in range(1, width - 1):
        # Find compare the pixels on left and right of the pixel we are looking at.
        #result_pixel_left = pixels[x-1, y]
        #result_pixel_right = pixels[x+1, y]
        #current_pixel = pixels[x,y]
        #if result_pixel_left > (current_pixel *1.45) or result_pixel_left  < (current_pixel *0.4):
         #   modified_pixels[x,y] = (255)   # This just copies the image
        #else:
         #   modified_pixels[x,y] = pixels[x,y]
        result_pixel = int(pixels[x-1,y] *0.25 - pixels[x+1,y]*0.25 + pixels[x,y+1]*0.25 - pixels[x,y-1]*0.25)
        if abs(result_pixel) >10:
            edge_pixels[x,y] = 255
        else:
            edge_pixels[x,y] = 0




original_image.show()
modified_image.show()
edge_image.show()