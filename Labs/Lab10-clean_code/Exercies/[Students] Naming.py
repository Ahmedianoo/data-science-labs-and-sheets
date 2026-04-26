class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left_point, width, height):
        self.top_left_point = top_left_point
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def update_height(self, height):
        self.height = height

    def update_width(self, width):
        self.width = width

    def update_top_left_point(self, top_left_point):
        self.top_left_point = top_left_point

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def print_coordinates(self):
        top_right = self.top_left_point.x + self.width
        bottom_left = self.top_left_point.y + self.height
        print("End Point X-Axis (Top Right): " + str(top_right))
        print("End Point Y-Axis (Bottom Left): " + str(bottom_left))


def build_rectangle():
    top_left_point = Point(50, 100)
    rectangle = Rectangle(top_left_point, 90, 10)
    return rectangle


rectangle1 = build_rectangle()
rectangle2 = build_rectangle()

print(rectangle1.calculate_area())
rectangle1.print_coordinates()

rectangle2.update_height(3)