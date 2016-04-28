import sys

inp=input('Input final configuration :')
P=[]
inp=inp.replace(' ','')
for i in range(len(inp)):  
    if len(inp)==8 and inp[i] in [str(i) for i in range(1,9)]: 
        if inp[i] not in P:
                P.append(inp[i])
        else:
            print('Incorrect configuration , giving up . . .')
            sys.exit()       
    else:
        print('Incorrect configuration , giving up . . .')
        sys.exit()


def RC(A):
    B=A[3]+A[0:3]+A[5:8]+A[4]
    return(B)

def RE(A):
    B=A[::-1]
    return(B)

def MC(A):
    B=A[0]+A[6]+A[1]+A[3:5]+A[2]+A[5]+A[7]
    return(B)

Start='12345678'
All=[Start]
Exit=set([Start])
Count=[0]
i=0
if inp in Exit:
    print('0 step is needed to reach the final configuration . ')
else:
    while i<10000000:
        p=RE(All[i])  
        if p==inp:
              break
        elif p not in Exit:
                Exit.add(p)
                All.append(p)
                Count.append(Count[i]+1)   
        p=RC(All[i])
        
        if p==inp:
              break
        elif p not in Exit:
                Exit.add(p)
                All.append(p)
                Count.append(Count[i]+1)
        p=MC(All[i])  
        if p==inp:
              break
        elif p not in Exit:
                Exit.add(p)
                All.append(p)
                Count.append(Count[i]+1)
        i=i+1
    print(Count[-1],'steps are needed to reach the final configuration.')
