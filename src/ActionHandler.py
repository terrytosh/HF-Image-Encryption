from Xor import Xor
from AES_picture import AES_picture
from PixelShuffler import PixelShuffler
from SuccessMessage import SuccessMessage
from DataLog import DataLog

class ActionHandler:
    def __init__(self, image_file, output_directory, action, algorithm, key, output_file):
        self.selected_image_file = image_file
        self.output_directory = output_directory
        self.action = action
        self.algorithm = algorithm
        self.key = key
        self.output_file = output_file
        self.success_msg = SuccessMessage(algorithm, action)
        self.data_log = DataLog(image_file, action, algorithm, output_directory, output_file)
        # print("ActionHandler variables:", self.selected_image_file, self.output_directory, self.action, self.algorithm, self.key, self.output_file)
    
    def handle_encryption(self):
        # print("Handling encryption with", self.algorithm)

        if self.algorithm == "XOR":
            xor = Xor(self.selected_image_file, self.output_directory, self.key, self.output_file)
            xor.encrypt()
            self.success_msg.show_success_message()

        if self.algorithm == "AES":
            aes = AES_picture(self.selected_image_file, self.output_directory, self.key, self.output_file)
            aes.encrypt_image()
        elif self.algorithm == "Pixel Shuffling":
            ps = PixelShuffler(self.selected_image_file, self.output_directory, self.key, self.output_file)
            ps.shuffle()
            self.success_msg.show_success_message()
        
        self.data_log.write_entry_to_file()
    
    def handle_decryption(self):
        if self.algorithm == "XOR":
            xor = Xor(self.selected_image_file, self.output_directory, self.key, self.output_file)
            xor.decrypt()
            self.success_msg.show_success_message()

        if self.algorithm == "AES":
            aes = AES_picture(self.selected_image_file, self.output_directory, self.key, self.output_file)
            aes.decrypt_image()
        elif self.algorithm == "Pixel Shuffling":
            ps = PixelShuffler(self.selected_image_file, self.output_directory, self.key, self.output_file)
            ps.unshuffle()
            self.success_msg.show_success_message()
        
        self.data_log.write_entry_to_file()