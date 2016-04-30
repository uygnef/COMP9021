class Point():
    def __init__(self,point):
        self.x = point[0]
        self.y = point[1]

class Vector():
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.dir_x = end_point.x - start_point.x
        self.dir_y = end_point.y - start_point.y

def product(A, B):  #vector
    return A.dir_x * B.dir_y - B.dir_x * A.dir_y

a=Point([1,0])
b=Point([2,3])
c=Point([3,2])
d=Point([4,1])
ac=Vector(a,c)
bd=Vector(b,d)
f=product(ac,bd)
