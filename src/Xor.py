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
        root, extension = os.path.splitext(file_path)
        return extension

    def encrypt(self):
        image = Image.open(self.image_file)
        pixel_data = list(image.getdata())

        print("Original Pixel:", pixel_data[0])
        print("Original Pixel:", pixel_data[1])

        salt = b'\xe2\xa1\x14\xfd\x07\x99A\xa3\xe4\xfc?\xcft(\xf4w'
        key_length = len(pixel_data)
        derived_key = hashlib.pbkdf2_hmac('sha256', self.key.encode(), salt, 100, key_length)

        # print("Pixel Data Length: ", len(pixel_data))
        # print("Derived Key Length: ", len(derived_key))
        # print(type(derived_key))

        encrypted_pixel_data = []

        for pixel, byte_char in zip(pixel_data, derived_key):
            red, green, blue = pixel
            byte_value = int(byte_char)
            red ^= 22
            green ^= 22
            blue ^= 22
            encrypted_pixel_data.append((red, green, blue))
        
        print("Encrypted Pixel:", encrypted_pixel_data[0])
        print("Encrypted Pixel:", encrypted_pixel_data[1])
        
        # Create a new image with the encrypted pixel data
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixel_data)

        file_extension = self.get_file_extension(self.image_file)
        self.output_file += file_extension

        # Save the encrypted image
        encrypted_image.save(os.path.join(self.output_directory, self.output_file))

        image.close()
        encrypted_image.close()
    
    def decrypt(self):
        image = Image.open(self.image_file)
        pixel_data = list(image.getdata())

        salt = b'\xe2\xa1\x14\xfd\x07\x99A\xa3\xe4\xfc?\xcft(\xf4w'
        key_length = len(pixel_data)
        derived_key = hashlib.pbkdf2_hmac('sha256', self.key.encode(), salt, 100, key_length)

        decrypted_pixel_data = []

        print("Loading in Encrypted Pixel:", pixel_data[0])
        print("Loading in Encrypted Pixel:", pixel_data[1])

        for pixel, byte_char in zip(pixel_data, derived_key):
            red, green, blue = pixel
            byte_value = int(byte_char)
            red ^= 22
            green ^= 22
            blue ^= 22
            decrypted_pixel_data.append((red, green, blue))

        print("Decrypted Pixel:", decrypted_pixel_data[0])
        print("Decrypted Pixel:", decrypted_pixel_data[1])
        
        # Create a new image with the decrypted pixel data
        decrypted_image = Image.new(image.mode, image.size)
        decrypted_image.putdata(decrypted_pixel_data)

        file_extension = self.get_file_extension(self.image_file)
        self.output_file += file_extension

        # Save the decrypted image
        decrypted_image.save(os.path.join(self.output_directory, self.output_file))

        image.close()
        decrypted_image.close()