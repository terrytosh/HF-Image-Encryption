from Xor import Xor

class ActionHandler:
    def __init__(self, image_file, output_directory, action, algorithm, key):
        self.selected_image_file = image_file
        self.output_directory = output_directory
        self.action = action
        self.algorithm = algorithm
        self.key = key
        print("ActionHandler variables:", self.selected_image_file, self.output_directory, self.action, self.algorithm, self.key)
    
    def handle_encryption(self):
        print("Handling encryption with", self.algorithm)

        if self.algorithm == "xor":
            xor = Xor(self.selected_image_file, self.output_directory, self.key)
            xor.encrypt()
    
    def handle_decryption(self):
        print("Handling decryption with", self.algorithm)