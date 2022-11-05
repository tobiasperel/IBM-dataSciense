class rectangle(object):

    def __init__(self, height,width, color):
        self.height = height
        self.width = width
        self.color = color

    def add_width(self, w):
        self.width = self.width+w
        print(self.width)

    def add_height(self, h):
        self.height = self.width+h
        print(self.height)

    def change_color(self, c):
        self.color = c
        print(self.color)

    def drawRectangle(self):
        import matplotlib.pyplot as plt
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

r1 = rectangle(10,20,"blue")
r1.add_width(8)
r1.add_height(3)
r1.change_color("brown")
r1.drawRectangle()

'''
class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x=3  #linea opcional unicamente cambia el valor de 'x'

p2.print_point()
'''