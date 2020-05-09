def calculate_vector_distance( vector1, vector2):
    x1, y1 =  vector1 if type(vector1) is tuple else (vector1.x, vector1.y)
    x2, y2 =  vector2 if type(vector2) is tuple else (vector2.x, vector2.y)
    
    return ((x1 - x2)**2 + (y1 - y2)**2 )**0.5


def rgb2hex(color):
    return '#%02x%02x%02x' % color


def hex2rgb(color):
    color = color.lstrip('#')
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))


class Vector:
    
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z


    def divide(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar


    def divide(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar


    def magnitude(self):
        return sqrt(self.x**2 + self.y ** 2 + self.z** 2)
