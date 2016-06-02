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
				result, remain_shape = compare(i,next.shape) #result is the solution,remain_shape is the shape after merge
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
				
			
				