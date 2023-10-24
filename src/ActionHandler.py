class ActionHandler:
    def __init__(self, image_file, output_directory, action, algorithm, key):
        self.selected_image_file = image_file
        self.output_directory = output_directory
        self.action = action
        self.algorithm = algorithm
        self.key = key