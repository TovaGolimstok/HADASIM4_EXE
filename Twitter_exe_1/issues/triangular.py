class Triangular:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return self.width + self.height * 2

    def is_even(self):
        return self.width % 2 == 0

    def can_print_triangular(self):
        return not self.is_even() and self.width < self.height * 2