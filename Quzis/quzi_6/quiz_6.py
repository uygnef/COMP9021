# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by *** and Eric Martin for COMP9021


from math import pi, hypot


class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({:.2f}, {:.2f})'.format(self.x, self.y)

class Disk():
    
    def __init__(self, radius=0.00,centre=Point() ):
        import re
        result = re.findall('\d+\.\d+', str(centre))
        print('radius',radius, type(radius))
        print(result)
        self.x = float(result[0])
        self.y = float(result[1])  
        self.r = float(radius)

    def change_radius(self, r):
        self.r = r

    def area(self, r):
        print(pi*r*r)

    def __repr__(self):
        return 'Disk(Point({:.2f}, {:.2f}), {:.2f})'.format(self.x, self.y, self.r)      
    
    
            
        

            
            
