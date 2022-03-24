import figure

class Rectangle(figure.Polygon):
    def __init__(self):
        figure.Polygon.__init__(self, 4)
    def getArea(self):
        self.area = self.sideLen * self.sideLen
        print(self.area)

r = Rectangle()
r.setSide()
r.getArea()
r.getShape()