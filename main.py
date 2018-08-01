import random
class Point2D(object):
    def __init__(self, x, y, quantization=1):
        self.x = x
        self.y = y
        self.quant = quantization

    def distance(self, point):
        return (self.x - point.x)**2 + (self.y - point.y)**2
    
    def __eq__(self, point):
        return (self.x <= point.x + self.quant
                and self.x >= point.x - self.quant and
                self.y <= point.y + self.quant
                and self.y >= point.y - self.quant)

    def __neq__(self, point):
        return not self.__eq__(point)

class Grid2D(object):
    def __init__(self, minimum_dist=1):
        self.grid = {}
        self.minimum_dist = minimum_dist

    def append(self, point, id):
        self.__setitem__(point, id)
    
    def __setitem__(self, point, id):
        assert isinstance(point, Point2D), 'Supplied point is not Point2D'
        self.grid[id] = point

    def __getitem__(self, id):
        return self.grid[id]

    def __contains__(self, point):
        return any(point in self.grid.values())

grid = Grid2D()
class Neuron(Point2D):
    def __init__(self, x, y, id, quantization=1):
        super().__init__(x, y, quantization)
        self.parents = []
        self.children = []
        self.alive = 0
        self.connections = []
        self.id = id
        self.min_radius = 1
        self.max_radius = 3
    
    def random_evolution(self):
        global grid
        random_x = self.x + random.random() * 2 - 1
        random_y = self.y + random.random() * 2 - 1
        new_point = Point2D(random_x, random_y,
                            quantization=self.quant)
        if new_point not in grid:
            self.point = new_point
            grid[self.id] = new_point

    def power(self):
        power = 0
        for child in self.children:
            
            power += child.size 