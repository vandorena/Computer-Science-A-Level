
from PIL import Image
import numpy

def grey_scale(image):
    width, height = image.size
    gray_image = Image.new('RGB', image.size)
    input_pixels = image.load()
    gray_pixels = gray_image.load()
    for y in range(height):
        for x in range(width):
            r, g, b = input_pixels[x, y][0:3]
            p = int(.299*r + .587*g + .114*b)
            gray_pixels[x, y] = p, p, p
    return gray_image

horizontal_edge_kernal = [[-10, 0, 10], [-10,0,10], [-10,0,10]]
vertical_edge_kernal = [[-10, -10, -10], [0,0,0], [10,10,10]]
#gaussian_blur_kernal = [[1,2,1],[2,4,2],[1,2,1]]
gaussian_blur_kernal = [[1,2,3,2,1],[2,4,6,4,2],[3,6,9,6,3],[2,4,6,4,2],[1,2,3,2,1]]

def apply_kernal(image: Image, kernal):
    assert len(kernal) == len(kernal[0]), "Invalid kernal"
    image = image.convert('L')
    new_image = Image.new('L', image.size)
    width, height = image.size
    kernal_half_width = len(kernal) // 2
    input_pixels = image.load()
    new_pixels  = new_image.load()
    for pixel_y in range(kernal_half_width, height - kernal_half_width):
        for pixel_x in range(kernal_half_width, width - kernal_half_width):
            pixel_sum = 0
            for k_x in range(-kernal_half_width, kernal_half_width+1):
                for k_y in range(-kernal_half_width, kernal_half_width+1):
                    kernal_value = kernal[k_y + kernal_half_width][k_x + kernal_half_width]
                    pixel_value = input_pixels[pixel_x + k_x, pixel_y + k_y]
                    pixel_sum += kernal_value * pixel_value
            kernal_sum = sum([sum(s) for s in kernal])
            new_pixels[pixel_x, pixel_y] = pixel_sum // (kernal_sum+1)

    return new_image

def edge_detect(image, threshold=False):
    image = grey_scale(image)
    image.save('grey_temp.png')
    width, height = image.size

    new_image = Image.new('RGB', image.size)
    input_pixels = image.load()
    new_pixels = new_image.load()

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            x_gradient = input_pixels[x+1, y][0] - input_pixels[x, y][0]
            y_gradient = input_pixels[x, y+1][0] - input_pixels[x, y][0]
            new_colour = int((x_gradient ** 2 + y_gradient ** 2) ** 0.5)
            new_pixels[x, y] = new_colour, new_colour, new_colour
            if threshold:
                if new_colour > threshold:
                    new_colour = 255
                else:
                    new_colour = 0
            new_pixels[x, y] = new_colour, new_colour, new_colour


    return new_image

# original_image = Image.open("Spongebob.png")
original_image = Image.open("car.jpg")

# original_image.show()
# edge_detect(original_image, 50).save('test.png')
blurred = apply_kernal(original_image, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)

blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
blurred = apply_kernal(blurred, gaussian_blur_kernal)
# blurred.save('test.png')
apply_kernal(blurred, horizontal_edge_kernal).save('test.png')