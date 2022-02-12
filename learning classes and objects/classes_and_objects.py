class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_color(self):
        print("My color is " + self.color)


# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "blue", 30)
r2 = Robot("Jerry", "red", 40)

r1.introduce_color()
r2.introduce_color()
