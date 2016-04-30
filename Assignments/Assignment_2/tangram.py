file = open('pieces_A.xml')
import bs4
for line in file:
      point_sets = []
      pattern = re.compile(r'^d="M (.+) z"$')
      point_set = re.compile(pattern,line)
    
##      if len(Point) != 0:
##          Point = Point[0].split('L')    
##          temp = []
##          for i in Point:
##              i = (i.split(' ')).remove('')
##              print(i)
##              a = []
##              for n in i:
##                  a.append(int(n))
##              temp.append(a)
##          point_sets.append(temp)
##              
              
    
      print(pattern)
