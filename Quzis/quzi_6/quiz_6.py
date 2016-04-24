# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by Yu Feng and Eric Martin for COMP9021


from math import pi, hypot


class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({:.2f}, {:.2f})'.format(self.x, self.y)

class Disk():
    
    def __init__(self, **X ):
        import re
        if len(X)==0:
            X['centre'] = Point()
            X['radius'] = 0
        self.x = X['centre'].x
        self.y = X['centre'].y  
        self.r = float(X['radius'])
        self.area = pi*self.r*self.r

    def change_radius(self,r):
        self.r = r
        self.area = pi*self.r*self.r

    def intersects(self, disk):
        if hypot((disk.x - self.x), (disk.y - self.y)) <= self.r + disk.r:
            return True
        else:
            return False

    def absorb(self, disk):
        X = disk.x - self.x
        Y = disk.y - self.y
        R = (hypot(X, Y) + self.r + disk.r) / 2 
        if R  > max(self.r, disk.r) :
            k=(R - self.r)/hypot(X,Y)
            x = k * (disk.x - self.x) + self.x
            y = k * (disk.y - self.y) + self.y
            r = R
        else:
            if disk.r == max(self.r, disk.r):
                x = disk.x
                y = disk.y
                r = disk.r
        return(Disk(centre=Point(x, y), radius=r))        

    def __repr__(self):
        return 'Disk(Point({:.2f}, {:.2f}), {:.2f})'.format(self.x, self.y, self.r)      
    
    
            
        

            
            
