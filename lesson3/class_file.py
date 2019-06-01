"Конструктор класса "



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def coordinates(self):
        print(f'coordinates are: {self.x}, {self.y}')
    def __repr__(self):
        return f'<Point x: {self.x}, y: {self.y}>'    

my_point = Point(5, 16)
print(my_point)
#<Point x: 5, y: 16>

