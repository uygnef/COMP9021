import copy
import sys
import time
import profile
import collections  

O=[[str(i) for i in range(1,5)],[str(i) for i in range(5,9)]]
O[1].reverse()
C=[]
D=[0]
inp='72154368'

P=[]
inp=inp.replace(' ','')
for i in range(len(inp)):  
    if len(inp)==8 and inp[i] in [str(i) for i in range(1,9)]: 
        if inp[i] not in P:
            P.append(inp[i])
        else:
            print('error')
            sys.exit()       
    else:
        print('error')
        sys.exit()
        




R=[[],[]]
R[0]=P[0:4]
R[1]=P[4:8]
R[1].reverse()

def RE(A):
    B = copy.deepcopy(A)
    temp=B[0]
    B[0]=B[1]
    B[1]=temp
    return(B)

def RC(A):
    B = copy.deepcopy(A)
    B[0].insert(0,B[0][3])
    B[0].pop()
    B[1].insert(0,B[1][3])
    B[1].pop()
    return(B)

    
def MC(A):
    B = copy.deepcopy(A)
    temp=B[0][1]
    B[0][1]=B[1][1]
    B[1][1]=B[1][2]
    B[1][2]=B[0][2]
    B[0][2]=temp
    return(B)


C=collections.deque(C)
sa=1



C.append(O)
i=0
t=0
if C[0][0]==R[0]and C[0][1]==R[1]:
    print('steo is 0')
else:
    while i<100000000:
        p=RE(C[-i])  
        if p==R:
              break
        elif p not in C:
                C.appendleft(p)
                D.append(D[i]+1)
    
        p=RC(C[-i])
        if p==R:
            break
        elif p not in C:
              C.appendleft(p)
              D.append(D[i]+1)
                               
        p=MC(C[-i])
        if p==R:
              break
        elif p not in C:
              C.appendleft(p)
              D.append(D[i]+1)
        i=i+1

print(D[-1])
    
    

