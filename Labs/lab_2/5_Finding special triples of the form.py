import math
def is_true(a):
    for i in range(0,int(math.sqrt(a)+1)):
        for m in range(i,int(math.sqrt(a)+1)):
            if a==i*i+m*m:
                return True
    return False
for i in range(100,1000):
    if is_true(i):
        if is_true(i+1):
            if is_true(i+2):
                print(i,i+1,i+2)
    
