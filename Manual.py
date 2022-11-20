from PairNumberExtractor import PairNumberExtractor
pairNumberExtractor = PairNumberExtractor()
class Manual:
    def __init__(self):
        self.MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
        self.MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
    def color_pair_to_string(self,major_color, minor_color):
        return f'{major_color} {minor_color}'
    def reference_manual(self):
        for major_color in self.MAJOR_COLORS:
            for minor_color in self.MINOR_COLORS:
                color_names = self.color_pair_to_string(major_color, minor_color)
                color_number = pairNumberExtractor.get_pair_number_from_color(major_color, minor_color)
                print(f'{color_names} {color_number}')
