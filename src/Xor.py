from PIL import Image
import hashlib
import os

class Xor:
    def __init__(self, image_file, output_directory, key):
        self.image_file = image_file
        self.output_directory = output_directory
        self.key = key

    def encrypt(self):
        image = Image.open(self.image_file)
        pixel_data = list(image.getdata())
        encrypted_pixel_data = []

        salt = os.urandom(16)
        print("Salt: ", salt)

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
        
        encrypted_image.info['user_salt'] = salt
        print(encrypted_image.info['user_salt'])

        # Save the encrypted image
        encrypted_image.save("\\Users\\16825\\Pictures\\Encrypted\\encrypted_image.png")

        image.close()
        encrypted_image.close()
    
    def decrypt(self):
        image = Image.open(self.image_file)
        pixel_data = list(image.getdata())
        decrypted_pixel_data = []

        salt = image.info['user_salt']
        print("Salt: ", salt)

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

        # Save the decrypted image
        decrypted_image.save("\\Users\\16825\\Pictures\\Decrypted\\decrypted_image.png")

        image.close()
        decrypted_image.close()