class Point():
    def __init__(self,point):
        self.x = point[0]
        self.y = point[1]

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

def reset_position(piece):
    goal = None
    for i in piece:
        if goal == None:
            goal = i
        goal.x = min(goal.x,i.x)
        goal.y = min(goal.y,i.y)
    temp_x = goal.x
    temp_y = goal.y
    for n in piece:
        n.x -= temp.x
        n.y -= temp.y
    return piece
        
    
def turn_90(piece):
        pass
