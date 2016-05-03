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

def reverse(colour): #slip the piece
    for point in colour:
        temp = point.x
        point.x = point.y
        point.y = temp
   #     print('x=',point.x,'y=',point.y)
    return colour    

def print_Point(colour):
    for i in colour:
        print('({},{})'.format(i.x,i.y),end=' ')

        
def is_identical(A_colour, B_colour):
    if len(A_colour) != len(B_colour): #make sure the number of point is same
        return False
    A_colour = reset_position(A_colour)
    B_colour = reset_position(B_colour)
  #  print('A_colour')
  #  print_Point(A_colour)
 #   print()
  #  print('B_colour')

    for _ in range(4):
        for i in range(len(A_colour)):
      #    print(A_colour[i].x,B_colour[i].x)
          if A_colour[i].x != B_colour[i].x or A_colour[i].y != B_colour[i].y:
                B_colour = turn_90(B_colour)
      #          print('')
       #         print_Point(B_colour)
          else:
                return True              

    B_colour = reverse(B_colour)
    for _ in range(4):
       for i in range(len(A_colour)):
        if A_colour[i].x != B_colour[i].x or A_colour[i].y != B_colour[i].y:
            B_colour = turn_90(B_colour)
   #         print('')
 #           print_Point(B_colour)
        else:
            return True 

    return False
                           
def are_identical_sets_of_coloured_pieces(piece_A, piece_B):
    if len(piece_A) != len(piece_B):  #the number of pirece must be same
        return False
    else:
        for A_colour in piece_A:       #test same color of two pirece whether identical
            for B_colour in piece_B:
                if A_colour != B_colour:
                    continue
                else:
                    return is_identical(piece_A[A_colour], piece_B[B_colour])
                return False
    
def reset_position(piece):
    goal_x = None
    goal_y = None
    for i in piece:
        if goal_x == None:
            goal_x = i.x
        if goal_y == None:
            goal_y = i.y
        goal_x = min(goal_x,i.x)
        goal_y = min(goal_y,i.y)
        
    for n in piece:
        n.x -= goal_x
        n.y -= goal_y

    start_point=[]                  #let the start point be (0,min)
    for j in range(len(piece)):
        if piece[j].x == 0:
            start_point.append(j)
 #   print(start_point)
    temp = piece[start_point[0]].y
    result = start_point[0]
    for x in start_point:
   #     print('temp,y',temp,piece[x].y,x)
        if piece[x].y < temp:
            result = x
 #           print(x,piece[x].y)
    
    piece = piece[result:] + piece[0:result]

    return piece          

def turn_90(piece):
    piece = reset_position(piece)
    for i in piece:
       # print('i',i.x,i.y)
        temp = i.x
        i.x = -i.y
        i.y = temp
       # print('changed',i.x,i.y,temp)
    piece = reset_position(piece)
    return piece
        
file = open('pieces_A.xml')    
piece=available_coloured_pieces(file)
new = turn_90(piece['red'])
new = turn_90(new)
new = turn_90(new)
new = turn_90(new)
for i in new:
	print(i.x,i.y)            
