from ring import *
class Point():
    def __init__(self,point):
        self.x = point[0]
        self.y = point[1]

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

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
    return pieces

def solve(pieces, shape):
    pieces_list = [[],[],None]
    config = []
    for i in pieces: #append colour into piece_list[0], just colour no position
        pieces_list[0].append(i)          #initialization of piece_list

    pieces_list[3] = rest_position(pieces(pieces_list[0].pop()))     #select the first colour in piece_list into using_piece
    shape = [pieces_list[3]]
   
def product_result(polygon): #get all cross_product in the polygon
    product_result=[]
    for i in range(-2,len(polygon)-2):
        ab = Vector(polygon[i], polygon[i+1])
        bc = Vector(polygon[i+1], polygon[i+2])

        r = cross_product(ab,bc)
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
            

def reverse(c): #slip the piece
    import copy
    colour = copy.deepcopy(c)
    for point in colour:       
        point.x,point.y = point.y,point.x 
    colour = colour[::-1]
    colour = reset_position(colour)
    return colour    

def print_Point(colour):
    for i in colour:
        print('({},{})'.format(i.x,i.y),end=' ')
    print()

def get_config(A_colour):
     result = [reset_position(A_colour)]
     B_colour = turn_90(A_colour)

     for _ in range(4):
        for i in result:
            if not equal(i,B_colour):
                if i == result[-1]:
                    result.append(B_colour)
                continue
            else:
                B_colour = turn_90(B_colour)
                break

     B_colour = reset_position(reverse(B_colour))
     for _ in range(4):
        for i in result:
            if not equal(i,B_colour):
                if i == result[-1]:
                    print(result)
                    result.append(B_colour)
                continue
            else:
                B_colour = turn_90(B_colour)
                break
     return result
   
def equal(a,b):
    for i in range(len(a)):
            if a[i].x != b[i].x or a[i].y != b[i].y:
                return False
    return True

def is_identical(A_colour, B_colour):
    if len(A_colour) != len(B_colour): #make sure the number of point is same
        return False
    A_colour = reset_position(A_colour)
    B_colour = reset_position(B_colour)

    for _ in range(4):
        for i in range(len(A_colour)):
          if A_colour[i].x != B_colour[i].x or A_colour[i].y != B_colour[i].y:
                B_colour = turn_90(B_colour)
          else:
                return True              

    B_colour = reverse(B_colour)
    for _ in range(4):
       for i in range(len(A_colour)):
        if A_colour[i].x != B_colour[i].x or A_colour[i].y != B_colour[i].y:
            B_colour = turn_90(B_colour)
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
                    if not is_identical(piece_A[A_colour], piece_B[B_colour]):
                        return False
    return True
    
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
    k  = None
    for j in range(len(piece)):
        if piece[j].x == 0:
            if k == None:
                k = j
            if piece[k].y > piece[j].y:
                k = j
    piece = piece[k:] + piece[0:k]
	
    return piece          

def turn_90(piece):
    new_piece=[]
    for i in piece:
        a,b = -i.y, i.x
        new_piece.append(Point([a,b]))
    new_piece = reset_position(new_piece)
    return new_piece

def area(piece):
    
    total_area = 0
    
    for p in piece:
        colour = piece[p]
        area = 0
        for i in range(-2,len(colour)-2):   #point in the same ploygon
            area += 0.5*cross_product(colour[i], colour[i+1])
        total_area += abs(area)
    return abs(total_area)           
                     
  
def is_solution(tangram, shape):
    if area(tangram) != area(shape):   #total area is equal
        return False

    for i in tangram:                  #judge each of two pieces whether overliped or not
        for j in tangram:
            if i != j:
                unions = union(tangram[i],tangram[j])
                if unions == False:
                    return False
                else:
                    if unions == 'not union':
                        continue


    for k in tangram:                # determine if every points is in the shape 
        if not is_in_shape(tangram[k],shape):
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

def point_in_shape(q,shape_point):   #judge the single point if in the piece 
    flag = False
    for p in range(len(shape_point)):
        p1 = shape_point[p-1]
        p2 = shape_point[p]
        
        if q.x == p1.x and q.y == p1.y:
            return True

        if cross_product(Vector(p1,q),Vector(q,p2)) == 0:
            if min(p1.y, p2.y) <= q.y <= max(p1.y, p2.y):
                if min(p1.x, p2.x) <= q.x <= max(p1.x, p2.x):
                    return True
                else:
                    continue
            
        if min(p1.y, p2.y) <= q.y < max(p1.y, p2.y):

            if p1.x == p2.x:
                if q.x <= p1.x:
                    flag = not flag

            else:
                if q.x <= max(p1.x, p2.x):
                    if q.y == p1.y:
                        if q.x < p1.x:
                            flag = not flag
                    else:               #q0 is the x坐标 point on the line when q0.y = qy                                                                            
                        q0 = (p1.x - p2.x) * (q.y - p1.y) / (p1.y - p2.y) + p1.x
                        if q0 > q.x:
                            flag = not flag

                        if q0 == q.x:
                            return True
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
                min_a = min(A_colour[i].x, A_colour[i+1].x)
                max_a = max(A_colour[i].x, A_colour[i+1].x)
                if min_a < B_colour[j].x < max_a and min_a < B_colour[j+1].x < max_a:
               #     is the the line ab print('在范围内')
                    if abs(A_colour[i].x - B_colour[j].x) < abs(A_colour[i].x - B_colour[j+1].x):

                        new_A.append(B_colour[j])
                        new_A.append(B_colour[j+1])
                        
                    else:

                        new_A.append(B_colour[j+1])
                        new_A.append(B_colour[j])

                elif min_a < B_colour[j].x < max_a:

                    new_A.append(B_colour[j])

                elif min_a < B_colour[j+1].x < max_a:
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

    count = 0
    for i in A:
        for j in B:
            if i.x == j.x and i.y == j.y:
                count += 1
    if count <= 1:
        return 'not union'

    if count >=3:
        return False


    a = None

    i = 0
    j = 0
    for i in range(0,len(A)):    
        if a == None:
            for j in B:
                if A[i].x == j.x and A[i].y == j.y:
                    a = i
                    break
            
    b = None

    i = 0
    j = 0
    for i in range(0,len(A)):
        if b == None:
            for j in B:
                if A[i].x == j.x and A[i].y == j.y:
                    if  i != a:
                        b = i
                        if b != a + 1:
                            a = len(A) - 1
                            b = 0
                else:
                    continue
                break

    i = 0
    j = 0
    for j in range(0,len(B)):
        if B[j].x == A[a].x and B[j].y == A[a].y:         
            c = j
            break
        
    if B[c-1].x != A[b].x or B[c-1].y != A[b].y:
        return False
    return True

def solve(pieces, shape):
    import random
    dirn = random.randint(1,4) #start point of shape, randomly choose topleft or topright of bottomleft etc.
    pieces_list = [pieces,[],None]
    config = []
    solution = {}
    if len(shape) != 1:
        return "Shape is  wrong"
    for i in shape:
        remain_shape = shape[i] #remain shape is a list of shape minus piece
        
    while pieces_list[0] != []: #append colour into piece_list[0], just colour no position
        pieces_list[2] = pieces_list[0].pop()          #initialization of piece_list
        config = get_config(pieces[pieces_list[2]]) #select the piece
        while True:
            if config == []:            #if all config is failure, put this piece into piece_list[1] (have_been used list)
                pieces_list[1].append(pieces_list[2])
                break
            now_config = config.pop()
            a= merge(now_config, remain_shape)
            if a:
                remain_shape = a
                solution[i] = now_config
                break
        
class pieces_result:
	def __init__(self):
		self.unused = []
		self.used = []
		self.shape = []
		self.solution = []
		self.father = None
	
	def inherit(self,List):
		import copy 
		self.unused = copy.deepcopy(List.unused)
		self.unused.pop()
		self.used = []
		#self.shape = shape
		#self.solution = 
		self.father = List
		self.shape = List.shape
	
	def __repr__(self):
		return ('used=',str(self.used),' unused=',str(self.unused))
		

def solve(pieces,shape):
	import copy
	import random
	random_dir = random.randint(1,4)
	start = pieces_result()
	start.unused = [i for i in pieces] #imput color name in pieces
	for i in shape:
		start.shape = copy.deepcopy(shape[i])	
	
	while True:
		next = pieces_result()
		next.inherit(start)
		
		while next.unused != []:

			a = next.unused.pop()
			next.used.append(a)
			config = get_config(pieces[a])
			#print('1',config)
			
			for i in config:
				mi = i
				result, remain_shape = compare(mi,next.shape,random_dir) #result is the solution,remain_shape is the shape after merge
				#print('2',i,next.shape,random_dir)
				if result:
					print('next',next.unused,next.used,next.shape,remain_shape)
					next.shape = remain_shape
					next.solution.append(result)
					start = copy.deepcopy(next)					
					start.unused = next.unused + next.used
					break
				else:
					if i == config[-1]:
						while next.unused == []:
							next = next.father
							if next.father == None and next.unused == []:
								return False
						start = next
						start.used.append(unused.pop())

def compare(piece,shape,dirn):
	#print('-1','compare:',piece,shape)
	piece = find_corner(piece,dirn)
	shape = find_corner(shape,dirn)
	#print('-2','compare:',piece,shape)
	move = (shape[0].x - piece[0].x, shape[0].y - piece[0].y) #move the piece to shape point
	for i in piece:
		i.x -= move[0]
		i.y -= move[1]
	shape_cut_point = []
	piece_merge_point = []
		#judge the line if cross
	for i in range(len(piece)): # comfirm the line not across
		a = piece[i]
		b = piece[i+1]
		for j in range(len(shape)):
			c = shape[j]
			d = shape[j+1]
			if if_cross(a,b,c,d):
				return False,False
	
	for i in range(len(shape)):
		if shape[i] == piece[i] and shape[i+1] == piece[i+1]:#这可能有错，因为两个不能直接比
			continue
		ab = Vector(shape[i], shape[i+1])
		cd = Vector(piece[i], piece[i+1])
		if cross_product(ab, cd) == 0:
			shape_cut_point.append(i+1)
			piece_merge_point.append(i+1)
			break
		else:
			shape_cut_point.append(i)
			piece_merge_point.append(i)
			break				
	for i in range(len(shape)):
		i = -i 
		if shape[i] == piece[i] and shape[i-1] == piece[i-1]:#这可能有错，因为两个不能直接比
			continue
		ab = Vector(shape[i], shape[i-1])
		cd = Vector(piece[i], piece[i-1])
		if cross_product(ab, cd) == 0:
			shape_cut_point.append(i-1)
			piece_merge_point.append(i-1)
			break
		else:
			shape_cut_point.append(i)
			piece_merge_point.append(i)
			break
	if piece_merge_point == [0,0] or shape_cut_point == [0,0]:
		return False,False
	a = piece[piece_merge_point[0]:piece_merge_point[1]]
	b = shape[shape_cut_point[0]:shape_cut_point[1]]
	remain_shape = a[::-1] + b
	return piece,remain_shape
	
			
		
			
	
	
		
	
		
	
	#piece的线段和shape的线段是否重合，重合部分表示出来。
	#分为两种情况。1，piece的线段在shape线段上。2，piece线段在shape线段延长线上，并在shape内。


def find_corner(shape,dirn):
	b = None
	a = shape[0].x
	for i in shape:
		if dirn == 1 or dirn == 2:
			a = min(a,i.x)
		else:
			a = max(a,i.x)
	for i in shape:
		if i.x == a:
			if not b:
				b = i.y
			elif dirn ==2 or dirn ==3:	
				b = min(i.y,b) 
			else:
				b = max(i.y,b)

	shape = Ring(shape)
	#print(shape)
	#print('a,b=',a,b)
	for i in range(len(shape)):
		if shape[i].x == a and shape[i].y == b:
			if cross_product(Vector(shape[i-1], shape[i]), Vector(shape[i], shape[i+1])) < 0:
				shape = Ring(shape[::-1]) #let all of them be clockwise
				for j in range(len(shape)):
					if shape[j].x == a and shape[j].y == b:
						return Ring(shape[j:j-1])
			else:
				return Ring(shape[i:i-1])
a = available_coloured_pieces(open('pieces_A.xml'))
s = available_coloured_pieces(open('shape_A_1.xml'))
solve(a,s)
	
				
			
				
