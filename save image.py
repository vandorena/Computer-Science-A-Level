from PIL import Image

def save_otl_image(image: Image.Image, filename: str):
    pixels = image.load()
    width, height = image.size
    with open(filename, 'w') as file:
        pass
    print(f'Image saved to OTL format.\nSize: {width}x{height}\nFilename: {filename}')


def load_otl_image(filename: str) -> Image.Image:
    with open(filename, 'r') as file:
        meta_data_str = file.readline().strip().split(' ')
        print(meta_data_str)
        width = int(meta_data_str[0])
        height = int(meta_data_str[1])
        return_image = Image.new('RGB', (width,height))
        pixels = return_image.load()
        for y in range(0,height):
            for x in range(0,width):
                cur_list = file.readline().strip().split(' ')
                pixels[x,y] = (int(cur_list[0]),int(cur_list[1]),int(cur_list[2]))
        ## Complete the code
        
    return return_image

loaded_image = load_otl_image('image.otl')
loaded_image.save('temp.png')