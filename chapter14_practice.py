import matplotlib.pyplot as plt

class Shape:
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius += r

    def draw(self, obj):
        obj.draw()
        plt.axis('scaled')
        plt.show()

class Circle(Shape):
    def draw(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))

shape = Shape()
redCircle = Circle(10, 'red')

shape.draw(redCircle)

class Rect(Shape):
    def __init__(self, width, height, color):
        super().__init__(self, color=color)
        self.width = width
        self.height = height

    def draw(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), width=self.width, height=self.height, fc=self.color))

blueRect = Rect(5, 2, 'yellow')
shape.draw(blueRect)
