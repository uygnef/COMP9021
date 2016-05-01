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
        self.length = (self.dir_x**2 + self.dir_y**2)**(1/2)
        

def cross_product(A, B):  #defin the cross product, A,B are vector 
    return A.dir_x * B.dir_y - B.dir_x * A.dir_y      
        
def available_coloured_pieces(file): #transfer the xml documents to the list of points
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(file, "html.parser")
    pieces={}
    for position in soup.find_all('path'):
        a=((position.get('d')).replace('M','')).replace('z','').split('L')
        colour = position.get('fill')
        point=[]
        for i in a:
            i = i.split(' ')
            i = [int(i) for i in i if i ]
            point.append(Point(i))
        pieces[colour] = point
   # print(pieces)
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
    for colour in pieces:
        result=product_result(pieces[colour])  #use cross product(judge clockwise)
        #print(result)
        for i in range(len(result)-1):
            if result[i]*result[i+1] <= 0:
                return False
     
        for m in range(len(pieces[colour])-1): # comfirm the line not across
            a = pieces[colour][m]
            b = pieces[colour][m+1]
            if m+2 < len(pieces[colour])-1:
                for n in range(m+2, len(pieces[colour])-1):
                    c = pieces[colour][n]
                    d = pieces[colour][n+1]
                    if if_cross(a,b,c,d):
                            return False       
    return True
            
##file = open ('incorrect_pieces_3.xml')
##coloured_pieces = available_coloured_pieces ( file )
##are_valid ( coloured_pieces )
def angle(A, B): #vectorA ,B    cacult the angle to the two vectors
    return (A.dir_x*A.dir_y + B.dir_x*B.dir_y)/(A.length*B.length)

def reverse(A): #slip the piece
    for colour in A:
        temp = A[colour].x
        A[colour].x = A[colour].y
        A[colour].y = temp
    return A    

def vector_set(colour):         #change the color pirece into vector set
    v_set=[]
    i = -1
    while i < len(colour)-1:
        ab = Vector(colour[i], colour[i+1])
        v_set.append(ab)
        i += 1
    return v_set

def is_identical(A_colour, B_colour):
    if len(A_colour) != len(B_colour): #make sure the number of point is same
        return False
    A_colour_vector_set = vector_set(A_colour)
    B_colour_vector_set = vector_set(B_colour)

    for b in range(len(B_colour_vector_set)):
        for i in range(len(A_colour_vector_set)):
            if A_colour_vector_set[-i].length != B_colour_vector_set[b-i].length:
                break
     #   for i in range(len(A_colour_vector_set)-1):
            if angle(A_colour_vector_set[-i],A_colour_vector_set[1-i]) != \
               angle(B_colour_vector_set[b-i],B_colour_vector_set[b+1-i]):
                break
            return True

    B_colour = reverse(B_colour)
    B_colour_vector_set = vector_set(B_colour)
    for b in range(len(B_colour_vector_set)):
        for i in range(len(A_colour_vector_set)):
            if A_colour_vector_set[-i].length != B_colour_vector_set[b-i].length:
                break
     #   for i in range(len(A_colour_vector_set)-1):
            if angle(A_colour_vector_set[-i],A_colour_vector_set[1-i]) != \
               angle(B_colour_vector_set[b-i],B_colour_vector_set[b+1-i]):
                break
            return True

    return False
                    

                



def are_identical_sets_of_coloured_pieces(pirece_A, pirece_B):
    if len(pirece_A) != len(pirece_B):  #the number of pirece must be same
        return False
    else:
        for A_colour in pirece_A:       #test same color of two pirece whether identical
            for B_colour in pirece_B:
                if A_colour != B_colour:
                    continue
                else:
                    return is_identical(pirece_A[A_colour], pirece_B[B_colour])
    
            

            
        
    
            
            
