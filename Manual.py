from PairNumberExtractor import PairNumberExtractor
pairNumberExtractor = PairNumberExtractor()
class Manual:
    def __init__(self):
        self.MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
        self.MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
    def color_pair_to_string(self,major_color, minor_color):
        return f'{major_color} {minor_color}'
    def color_mapping(self,major_color, minor_color):
        color_names = self.color_pair_to_string(major_color, minor_color)
        color_number = pairNumberExtractor.get_pair_number_from_color(major_color, minor_color)
        return f'{color_names} {color_number}'


