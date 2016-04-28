import copy
O=[[i for i in range(1,5)],[i for i in range(5,9)],0]
O[1].reverse()
C=[]
D=[]
R=[[2,6,8,4],[1,3,7,5]]
def RE(A):
    B = copy.deepcopy(A)
    temp=B[0]
    B[0]=B[1]
    B[1]=temp
    B[2]=B[2]+1

    return(B)

def RC(A):
    B = copy.deepcopy(A)
    B[0].insert(0,B[0][3])
    B[0].pop()
    B[1].insert(0,B[1][3])
    B[1].pop()
    B[2]=B[2]+1

    return(B)
    
def MC(A):
    B = copy.deepcopy(A)
    temp=B[0][1]
    B[0][1]=B[1][1]
    B[1][1]=B[1][2]
    B[1][2]=B[0][2]
    B[0][2]=temp
    B[2]=B[2]+1
    
    return(B)

C.append(O)
D.append(O[0:-1])
for i in range(1000000000):
    p=RE(C[i])
    if p[0]==R[0]and p[1]==R[1]:
        break
    elif not p in C:
              C.append(p)
             # D.append(srt(p[0:-1]))
         #     print('RC=',p)
    p=RC(C[i])
    if p[0]==R[0]and p[1]==R[1]:
        break
    elif not p in C:
              C.append(p)
             # D.append(srt(p[0:-1]))
           #   print('RE=',p)
    p=MC(C[i])
    if p[0]==R[0]and p[1]==R[1]:

        break
    elif not p in C:
              C.append(p)
              #D.append(srt(p[0:-1]))
            #  print('Mc=',p)
print('too many steps, stop')

print(C[-1])
