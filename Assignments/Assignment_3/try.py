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
			
			for i in config:
				result, remain_shape = compare(i,next.shape,random_dir) #result is the solution,remain_shape is the shape after merge
				if c:
					next.shape = remain_shape
					next.solution.append(result)
					start = next.used.pop()
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

def compare(piece, shape,dirn):
	import * from Ring
	piece = find_corner(piece,dirn)
	shape = find_corner(shape,dirn)
	move = (shape[0].x - piece[0].x, shape[0].y - piece[0].y) #move the piece to shape point
	for i in piece:
		i.x -= move[0]
		i.y -= move[1]
	step = []
	for i in range(len(shape)):
		if shape[i] == piece[i] and shape[i+1] == piece[i+1]:#这可能有错，因为两个不能直接比
			记录重合点
			continue
		if shape[i],shape[i+1] collinear piece[i],piece[i+1]:
			判断并记录重合点，并返回【0】点 -1 计算
			break

	for i in range(len(shape)):
		i = -i
		if shape[i] == piece[i] and shape[i+1] == piece[i+1]:#这可能有错，因为两个不能直接比
			记录重合点
			continue
		if shape[i],shape[i+1] collinear piece[i],piece[i+1]:
			判断并记录重合点，并返回【0】点 -1 计算
			break 
		else:
			
		
			
	
	
		
	
		
	
	#piece的线段和shape的线段是否重合，重合部分表示出来。
	#分为两种情况。1，piece的线段在shape线段上。2，piece线段在shape线段延长线上，并在shape内。

def edge_incomman() 
def find_corner(shape,dirn):
	import * from ring
	b = None
	a = shape[0].x
	for i in shape:
		if dirn == 1 or dirn == 2:
			a = min(a,i.x)
	for i in shape:
		if i.x == a:
			if not b:
				b = i.y
			elif dirn ==2 or dirn ==3:	
				b = min(i.y,b) 
			else:
				b = max(i.y,b)

	shape = Ring(shape)
	for i in range(len(shape)):
		if shape[i].x == a and shape[i].y == b:
			if cross_product(Vector(shape[i-1], shape[i]), Vector(shape[i], shape[i+1])) < 0:
				shape = shape[::-1] #let all of them be clockwise
				for j in range(len(shape)):
					if shape[j].x == a and shape[j].y == b:
						return Ring[j:j-1]
			else:
				return Ring(shape[i:i-1])

	
				
			
				