from PIL import Image

class Xor:
    def __init__(self, image_file, output_directory, key):
        self.image_file = image_file
        self.output_directory = output_directory
        self.key = key

    def encrypt(self):
        image = Image.open(self.image_file)
        pixel_data = list(image.getdata())
        encrypted_pixel_data = []

        byte_key = 0xAA

        for pixel in pixel_data:
            encrypted_pixel = []
            for byte in pixel:
                encrypted_byte = byte ^ byte_key
                encrypted_pixel.append(encrypted_byte)
            encrypted_pixel_data.append(tuple(encrypted_pixel))
        
        # Create a new image with the encrypted pixel data
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixel_data)

        # Save the encrypted image
        encrypted_image.save("\\Users\\16825\\Pictures\\Encrypted\\encrypted_image.png")

        image.close()
        encrypted_image.close()