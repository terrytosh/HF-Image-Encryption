from PIL import Image
import hashlib
import os

class Xor:
    def __init__(self, image_file, output_directory, key, output_file):
        self.image_file = image_file
        self.output_directory = output_directory
        self.key = key
        self.output_file = output_file
    
    def get_file_extension(self, file_path):
        # Split the file path into the root and extension
        root, extension = os.path.splitext(file_path)
        # Return the extension (including the dot)
        return extension

    def encrypt(self):
        image = Image.open(self.image_file)
        pixel_data = list(image.getdata())
        encrypted_pixel_data = []

        salt = b'\xe2\xa1\x14\xfd\x07\x99A\xa3\xe4\xfc?\xcft(\xf4w'

        key_length = len(pixel_data)
        derived_key = hashlib.pbkdf2_hmac('sha256', self.key.encode(), salt, 100, key_length)

        for pixel in pixel_data:
            encrypted_pixel = []
            for byte, key_byte in zip(pixel, derived_key):
                encrypted_byte = byte ^ key_byte
                encrypted_pixel.append(encrypted_byte)
            encrypted_pixel_data.append(tuple(encrypted_pixel))
        
        # Create a new image with the encrypted pixel data
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixel_data)

        file_extension = self.get_file_extension(self.image_file)
        self.output_file += file_extension

        # Save the encrypted image
        encrypted_image.save(os.path.join(self.output_directory, self.output_file))

        # print(self.output_directory)

        image.close()
        encrypted_image.close()
    
    def decrypt(self):
        image = Image.open(self.image_file)
        pixel_data = list(image.getdata())
        decrypted_pixel_data = []

        salt = b'\xe2\xa1\x14\xfd\x07\x99A\xa3\xe4\xfc?\xcft(\xf4w'

        key_length = len(pixel_data)
        derived_key = hashlib.pbkdf2_hmac('sha256', self.key.encode(), salt, 100, key_length)

        for pixel in pixel_data:
            decrypted_pixel = []
            for byte, key_byte in zip(pixel, derived_key):
                decrypted_byte = byte ^ key_byte
                decrypted_pixel.append(decrypted_byte)
            decrypted_pixel_data.append(tuple(decrypted_pixel))
        
        # Create a new image with the decrypted pixel data
        decrypted_image = Image.new(image.mode, image.size)
        decrypted_image.putdata(decrypted_pixel_data)

        file_extension = self.get_file_extension(self.image_file)
        self.output_file += file_extension

        # Save the decrypted image
        decrypted_image.save(os.path.join(self.output_directory, self.output_file))

        image.close()
        decrypted_image.close()