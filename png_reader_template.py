
import binascii

PNG_SIGNATURE = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

class Chunk:
    def __init__(self, type, length, data, crc):
        self.type = type
        self.length = length
        self.data = data
        self.crc = crc

    def __repr__(self):
        return f'type: {self.type}, length: {self.length}, data: {self.data[0:10]}...'

class Header(Chunk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.width = int.from_bytes(self.data[0:4], byteorder='big')
        self.height = int.from_bytes(self.data[4:8], byteorder='big')
        self.bit_depth = int.from_bytes(self.data[8:9], byteorder='big')
        self.colour_type = int.from_bytes(self.data[9:10], byteorder='big')
        self.compression_method = int.from_bytes(self.data[10:11], byteorder='big')
        self.filter = int.from_bytes(self.data[11:12], byteorder='big')
        self.interlace_method = int.from_bytes(self.data[12:13], byteorder='big')

    def display_info(self):
        print(f'size: {self.width}x{self.height}, bit depth: {self.bit_depth}, colour type: {self.colour_type}')


def read_png_chunks(filename):
    with open(filename, 'rb') as png_file:
        # read signature bytes
        signature = png_file.read(8)
        # Check that signature is valid
        if signature != PNG_SIGNATURE:
            raise Exception("Invalid PNG signature")

        # loop reading one chunk at a time
        while True:
            # Read the chunk length 4 byte integer, big-endian - use int.from_bytes()
            length = int.from_bytes(png_file.read(4),byteorder="big")
            # Read the chunk type 4 byte ascii - decode('utf8')
            chunk_type = png_file.read(4).decode("utf8")
            # Read the chunk data. The length is the number you read earlier
            chunk_data = png_file.read(length)
            # Read the crc checksum. 4 byte integer
            crc = int.from_bytes(png_file.read(4),byteorder="big")
            # Check crc
            crc_check = binascii.crc32(chunk_type.encode('utf8')+chunk_data)
            if crc_check != crc:
                raise Exception("Invalid chunk")

            chunk = Chunk(chunk_type, length, chunk_data, crc)
            # Display the chunk that you've just read
            print(chunk)

            # If it's a header chunk do more stuff with it. If it's the end of the file, break the loop
            if chunk.type == 'IHDR':
                header = Header(chunk_type, length, chunk_data, crc)
                header.display_info()
            elif chunk.type == 'IEND':
                break

read_png_chunks('landscape.png')