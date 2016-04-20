for x in range(10,100):
    for y in range(x,100):    
        for z in range(y,100):
             c=x*y*z
             if c>100000:
                if set(int(i) for i in str(c)) == set([x%10,x//10,y%10,y//10,z//10,z%10]) \
		   and len(set([x%10,x//10,y%10,y//10,z//10,z%10]))==6:
                         print(x,y,z)
                             
             
