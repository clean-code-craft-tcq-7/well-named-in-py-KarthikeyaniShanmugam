class ColorPairStringCreator:
    def __init__(self):
        self.MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
        self.MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
    def color_pair_to_string(major_color, minor_color):
        return f'{major_color} {minor_color}'
