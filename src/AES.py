from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AES:
    def __init__(self, image_file, output_directory, key):
        self.image_file = image_file
        self.output_directory = output_directory
        self.key = key

    def encrypt(self):
        image_input = open(self.image_file)
        
        input_data = image_input.read()
        image_input.close()

        salt = get_random_bytes(16)
        print("Salt: ", salt)

        key_length = len(input_data)
        derived_key = PBKDF2(self.key.encode(), salt, dkLen=key_length)

        cipher = AES.new(derived_key, AES.MODE_CBC)
        cipher_data = cipher.encrypt(pad(input_data, AES.block_size))

        with open('AES_encrypted.bin', 'wb') as f:
            f.write(cipher.iv)
            f.write(cipher_data)

        with open('AES_Key.bin', 'wb') as f:
            f.write(derived_key)

    def decrypt(self):
        with open('AES_Key.bin', 'rb') as f:
            derived_key = f.read()
        
        with open('AES_encrypted.bin', 'rb') as f:
            iv = f.read(16)
            decrypt_data = f.read()
        
        cipher = AES.new(derived_key, AES.MODE_CBC, iv=iv)
        original = unpad(cipher.decrypt(decrypt_data), AES.block_size)


