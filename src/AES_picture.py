from PIL import Image
from Crypto.Cipher import AES
from Crypto import Random
import os
import io
import hashlib

class AES_picture:
    def __init__(self, image_file, output_directory, key, output_file):
        self.image_file = image_file
        self.output_directory = output_directory
        self.key = key
        self.output_file = output_file

    def encrypt_image(self):
        input_file = open(self.image_file, "rb")
        input_data = input_file.read()
        input_file.close()

        salt = b'\xe2\xa1\x14\xfd\x07\x99A\xa3\xe4\xfc?\xcft(\xf4w'
        derived_key = hashlib.pbkdf2_hmac('sha256', self.key.encode(), salt, 100, 32)
        iv = Random.new().read(16)

        cfb_cipher = AES.new(derived_key, AES.MODE_CFB, iv)
        enc_data = cfb_cipher.encrypt(input_data)
        
        dest_file = os.path.join(self.output_directory, self.output_file+".enc")
        enc_file = open(dest_file, "wb")
        enc_file.write(iv)
        enc_file.write(enc_data)
        enc_file.close()
        print("success")

    def decrypt_image(self):
        enc_file2 = open(self.image_file, "rb")
        iv = enc_file2.read(16)
        enc_data2 = enc_file2.read()
        
        enc_file2.close()

        salt = b'\xe2\xa1\x14\xfd\x07\x99A\xa3\xe4\xfc?\xcft(\xf4w'
        derived_key = hashlib.pbkdf2_hmac('sha256', self.key.encode(), salt, 100, 32)
        cfb_decipher = AES.new(derived_key, AES.MODE_CFB, iv)
        plain_data = (cfb_decipher.decrypt(enc_data2))
        imageStream = io.BytesIO(plain_data)
        imageFile = Image.open(imageStream)
        dest_file = os.path.join(self.output_directory, self.output_file+".jpg")
        imageFile.save(dest_file)

