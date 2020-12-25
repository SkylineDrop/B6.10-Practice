class Rectangle:
    def __init__(self, w, h):
        self.width = w 
        self.height = h

    def rectangle_area(self):
        return self.width * self.height

small_rect = Rectangle(5, 7)
print(small_rect.rectangle_area())
