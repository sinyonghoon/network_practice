import figure
import turtle

class Triangle(figure.Polygon):
    def __init__(self):
        figure.Polygon.__init__(self, 4)
    def getArea(self):
        self.area = self.sideLen * self.sideLen / 2
        print(self.area)
    def draw(self):
        for steps in range(3):
            turtle.forward(self.sideLen)
            turtle.right(120)
        input("Press Enter to quit")

r = Triangle()
r.setSide()
r.getArea()
r.getShape()
r.draw()