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

def cross_product(A, B):  #defin the cross product, A,B are vector 
    return A.dir_x * B.dir_y - B.dir_x * A.dir_y      
        
def available_coloured_pieces(file): #transfer the xml documents to the list of points
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(file, "html.parser")
    pieces=[]
    for position in soup.find_all('path'):
        a=((position.get('d')).replace('M','')).replace('z','').split('L')
        point=[]
        for i in a:
            i = i.split(' ')
            i = [int(i) for i in i if i ]
            point.append(Point(i))
        pieces.append(point)
    return pieces

def product_result(polygon): #get all cross_product in the polygon
    product_result=[]
    for i in range(-2,len(polygon)-2):
        ab = Vector(polygon[i], polygon[i+1])
        bc = Vector(polygon[i+1], polygon[i+2])

        r = cross_product(ab,bc)
        #print('r=',r)
        product_result.append(r)
    return(product_result)
    
def if_cross(a, b, c, d): #input Point()
    ac = Vector(a,c)
    ad = Vector(a,d)
    bc = Vector(b,c)
    bd = Vector(b,d)
    ca = Vector(c,a)
    da = Vector(d,a)
    cb = Vector(c,b)
    db = Vector(d,b)
    return (cross_product(ac, ad) * cross_product(bc, bd) <= 0) \
        and (cross_product(ca, cb) * cross_product(da, db) <= 0)
    
    
def are_valid (pieces):
    for polygon  in pieces:
        result=product_result(polygon)  #use cross product(judge clockwise)
      #  print(result)
        for i in range(len(result)-1):
            if result[i]*result[i+1] <= 0:
                return False
     
        for m in range(len(polygon)-1): # comfirm the line not across
            a = polygon[m]
            b = polygon[m+1]
            if m+2 < len(polygon)-1:
                for n in range(m+2, len(polygon)-1):
                    c = polygon[n]
                    d = polygon[n+1]
                    if if_cross(a,b,c,d):
                            return False
        
    return True
            
 


        
            

            
        
    
            
            
