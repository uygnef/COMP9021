class Point():
    def __init__(self,point):
        self.x = point[0]
        self.y = point[1]

class Vector():
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y
        self.length = (self.x**2 + self.y**2)**(1/2)
        

def cross_product(A, B):  #defin the cross product, A,B are vector 
    return A.x * B.y - B.x * A.y      
        
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
      #  print('r=',r)
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
    print()

        
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

def area(piece):
    
    total_area = 0
    
    for p in piece:
        colour = piece[p]
      #  print_Point(colour)  #colour actually means the list of
      #  print()
        area = 0
        for i in range(-2,len(colour)-2):   #point in the same ploygon

            area += 0.5*cross_product(colour[i], colour[i+1])
           # print(cross_product(colour[i], colour[i+1]))
       # print(p,area)
        total_area += abs(area)
      #  print('total=',total_area)
    return abs(total_area)           
                     
  
def is_solution(tangram, shape):
    if area(tangram) != area(shape):
      #  print(area(tangram),area(shape))
##        print('area wrong')
        return False

    for i in tangram:
        for j in tangram:
            if i != j:
                unions = union(tangram[i],tangram[j])
                if unions == False:
##                    print('point in piece')
                    return False
                else:
                    if unions == 'not union':
                        continue


    for k in tangram: 
        if not is_in_shape(tangram[k],shape):
##            print('point not in shape')
            return False   
    return True

def is_in_shape(piece, shape):
    for i in shape:
        shape_point = shape[i]
        true_list=[]
    for q in piece:
        true_list.append(point_in_shape(q,shape_point))

    if False in true_list:
        return False
    return True

def point_in_shape(q,shape_point):    
   # for q in piece:
    flag = False
  #  print(q.x,'---',q.y)
    for p in range(len(shape_point)):
        p1 = shape_point[p-1]
        p2 = shape_point[p]
    #    print('p1,p2',p1.x,p1.y,'-',p2.x,p2.y)
        
        if q.x == p1.x and q.y == p1.y:
        #    print('点重合')
            return True

        if cross_product(Vector(p1,q),Vector(q,p2)) == 0:
            if min(p1.y, p2.y) <= q.y <= max(p1.y, p2.y):
                if min(p1.x, p2.x) <= q.x <= max(p1.x, p2.x):
           #         print('点再线上')
                    return True
                else:
                    continue
            
        if min(p1.y, p2.y) <= q.y < max(p1.y, p2.y):

            if p1.x == p2.x:
                if q.x <= p1.x:
                    flag = not flag

            else:
                
                if q.y == p1.y:
                    judge = (q.y - p2.y) * (q.x -p2.x) - (p2.x - p1.x) * (p2.y - p1.y)
                else:
                    judge = (q.y - p1.y) * (q.x -p1.x) - (p2.x - p1.x) * (p2.y - p1.y)
     
                  #  print('q=',q.x,q.y)
                  #  print('P=',p1.x,p1.y,' ',p2.x,p2.y)
                 #   print('qian=',(p2.x - p1.x) * (p2.y - p1.y))
                  #  print('({}-{})*({}-{})={}'.format(q.y,p1.y,q.x,p1.x,(q.y - p1.y) * (q.x -p1.x)))
                   # print('hou=',(p2.x - p1.x) * (p2.y - p1.y))
                  #  print('({}-{})*({}-{})={}'.format(p2.x,p1.x,p2.y,p1.y,(p2.x - p1.x) * (p2.y - p1.y)))
                    
                  #  print(judge)

                if judge == 0:
                  #  print('点又重合')
                    return True
                if judge > 0:
                  #  print('射线相交')
                    flag = not flag
                # when q1.y = q2.y ignore
##    if flag == False:
##        print('错误点',q.x,q.y)
    return flag                  
    

def collinear(A_colour, B_colour):
    new_A = []
    for i in range(-1, len(A_colour)-1):
        new_A.append(A_colour[i])
        for j in range(-2, len(B_colour)-2):
            
            #two lines ai-ai+1, bi-bi+1 are collinear
            if cross_product(Vector(A_colour[i], A_colour[i+1]), Vector(B_colour[j], B_colour[j+1])) != 0 \
               or cross_product(Vector(A_colour[i], A_colour[i+1]), Vector(B_colour[j], A_colour[i])) != 0: 
                continue
            else:
            #    print('有共线')
             #   print_Point([A_colour[i], B_colour[j]])
                min_a = min(A_colour[i].x, A_colour[i+1].x)
                max_a = max(A_colour[i].x, A_colour[i+1].x)
                if min_a < B_colour[j].x < max_a and min_a < B_colour[j+1].x < max_a:
               #     print('在范围内')
                    if abs(A_colour[i].x - B_colour[j].x) < abs(A_colour[i].x - B_colour[j+1].x):
                  #      print('j>j+1')
                        new_A.append(B_colour[j])
                        new_A.append(B_colour[j+1])
                        
                    else:
                    #    print('j<j+1')
                        new_A.append(B_colour[j+1])
                        new_A.append(B_colour[j])

                elif min_a < B_colour[j].x < max_a:
                  # print('only j')
                    new_A.append(B_colour[j])

                elif min_a < B_colour[j+1].x < max_a:
                  #  print('j=',j)
                 #   print('---',B_colour[j+1].x , min_a, max_a)
                #    print('only j+1')
                    new_A.append(B_colour[j+1])
    return new_A 
##
##
def union(A_colour, B_colour):
    import copy

    if cross_product(Vector(A_colour[0], A_colour[1]), Vector(A_colour[1], A_colour[2])) < 0:
        A_colour = A_colour[::-1]
    if cross_product(Vector(B_colour[0], B_colour[1]), Vector(B_colour[1], B_colour[2])) < 0:
        B_colour = B_colour[::-1]        
    A = copy.deepcopy(collinear(A_colour, B_colour))
    B = copy.deepcopy(collinear(B_colour, A_colour))
##    print_Point(A)
##    print()
##    print_Point(B)
##    print()
##    
##    for i in A:
##       if point_in_shape(i, B):
##            print(i.x,i.y)
##            print(1)
##            return False
##    for j in B:
##        if point_in_shape(j, A):
##            print(2)
##            return False
##

    count = 0
    for i in A:
        for j in B:
            if i.x == j.x and i.y == j.y:
                count += 1
    if count <= 1:
        return 'not union'

    if count >=3:
##        print(4)
        return False

##    print_Point(A)
##    print()
##    print_Point(B)
##    print()

    a = None

    i = 0
    j = 0
    for i in range(0,len(A)):    
        if a == None:
            for j in B:
                if A[i].x == j.x and A[i].y == j.y:
  #                  print(A[i].x , A[i].y)
                    a = i
  #                  print('a=',a)
                    break
            
    b = None

    i = 0
    j = 0
    for i in range(0,len(A)):
        if b == None:
            for j in B:
                if A[i].x == j.x and A[i].y == j.y:
 #                   print('b 可能的值',i,'x,y=',A[i].x,A[i].y,'  ',)
                    if  i != a:
                        b = i
                        if b != a + 1:
                            a = len(A) - 1
                            b = 0
 #                       print('b=',b)
 #                       print('a=',a)
                else:
                    continue
                break

    i = 0
    j = 0
 #   print('BBB=',len(B))
    for j in range(0,len(B)):
 #       print('j===',j)
        if B[j].x == A[a].x and B[j].y == A[a].y:
         
            c = j
            break
        
    if B[c-1].x != A[b].x or B[c-1].y != A[b].y:
 #       print(c,c-1)
 #       print(B[c-1].x, B[c-1].y,'  ',A[b].x,A[b].y)
 #       print(3)
        return False

    return True

##    
##
##    b_start = min(a,b)
##    b_end = max(a,b)
##    if A[a_end - 1] != A[a_start]:
##        return False
##    
##    if b_end == len(B) +1 and b_start == 0 :
##        return B[ :b_start] + A[a_end:] + A[:a_start] + A[a_start]
##    else:
##        
##       return B[b_end+1:] + B[ :b_start] + A[a_end:] + A[:a_start] + A[a_start] 
           
file = open ('shape_Z.xml')
shape = available_coloured_pieces ( file )
file = open ('tangram_Z.xml')
tangram = available_coloured_pieces ( file )
s = is_solution ( tangram , shape )
print(s)
