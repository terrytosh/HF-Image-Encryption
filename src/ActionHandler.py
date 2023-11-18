from Xor import Xor
from SuccessMessage import SuccessMessage

class ActionHandler:
    def __init__(self, image_file, output_directory, action, algorithm, key, output_file):
        self.selected_image_file = image_file
        self.output_directory = output_directory
        self.action = action
        self.algorithm = algorithm
        self.key = key
        self.output_file = output_file
        self.success_msg = SuccessMessage(algorithm, action)
        # print("ActionHandler variables:", self.selected_image_file, self.output_directory, self.action, self.algorithm, self.key, self.output_file)
    
    def handle_encryption(self):
        # print("Handling encryption with", self.algorithm)

        if self.algorithm == "XOR":
            xor = Xor(self.selected_image_file, self.output_directory, self.key, self.output_file)
            xor.encrypt()
            self.success_msg.show_success_message()
    
    def handle_decryption(self):
        if self.algorithm == "XOR":
            xor = Xor(self.selected_image_file, self.output_directory, self.key, self.output_file)
            xor.decrypt()
            self.success_msg.show_success_message()