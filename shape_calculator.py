class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + self.width + ", height=" + self.height + ")"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return ((self.width**2) + (self.height**2))**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        string = ""
        for _ in range(self.height):
            string += "*" * self.width + "\n"

        return string

    def get_amount_inside(self, rect):
        w = int(self.width / rect.width)
        h = int(self.height / rect.height)

        return (h if h > w else w) if w > 0 and h > 0 else 0


class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return "Square(side=" + self.width + ")"

    def set_side(self, side):
        self.height = side
        self.width = side


# rect = Rectangle(4, 8)

# print(rect.get_amount_inside(Rectangle(4, 4)))
