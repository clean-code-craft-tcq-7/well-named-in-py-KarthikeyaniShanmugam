class PairNumberExtractor:
    def __init__(self):
        self.MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
        self.MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
    def get_pair_number_from_color(self,major_color, minor_color):
        try:
            major_index = self.MAJOR_COLORS.index(major_color)
        except ValueError:
            raise Exception('Major index out of range')
        try:
            minor_index = self.MINOR_COLORS.index(minor_color)
        except ValueError:
            raise Exception('Minor index out of range')
        return major_index * len(self.MINOR_COLORS) + minor_index + 1
