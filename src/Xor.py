from PIL import Image

class Xor:
    def __init__(self, image_file, output_directory, key):
        self.image_file = image_file
        self.output_directory = output_directory
        self.key = key

    def encrypt(self):
        img = Image.open(self.image_file)
        img_data = img.tobytes()

        key_length = len(self.key)
        # Ensure the key matches the image data length
        if key_length < len(img_data):
            # Pad the key with zeros to match the image data length
            self.key = self.key.ljust(len(img_data), '\x00')
        elif key_length > len(img_data):
            # Truncate the key to match the image data length
            self.key = self.key[:len(img_data)]
        else:
            # Key length matches the image data length
            self.key = self.key
        
        self.byte_key = self.key.encode("utf-8")
        encrypted_data = bytes(img_byte ^ key_byte for img_byte, key_byte in zip(img_data, self.byte_key))
        encrypted_image = Image.frombytes(img.mode, img.size, encrypted_data)
        encrypted_image_path = self.output_directory + "/encrypted_image.jpg"
        encrypted_image.save(encrypted_image_path)