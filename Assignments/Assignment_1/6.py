data_file=input('Which data file do you want to use?')

dic=[]
with open(data_file) as file:
    for word in file:
      word=word.strip()
      word=word.split(' ')
      dic=dic+word
#print(dic)

i=0
coordinates=[]
while i < len(dic):
    a=min(int(dic[i]),int(dic[i+2]))
    b=min(int(dic[i+1]),int(dic[i+3]))
    A=[a,b]
    a=max(int(dic[i]),int(dic[i+2]))
    b=max(int(dic[i+1]),int(dic[i+3]))
    B=[a,b]
    coordinates.append(A+B)
    i=i+4
coordinates.sort()
#print(coordinates)

def caculate(A,B):
 #   print('A=',A,'B=',B)
    if not (A[0]<B[2]<A[2] and  A[1]<B[1]<A[3] and A[1]<B[3]<A[3]):
        if A[0]<B[0]<A[2] and (A[1]<B[1]<A[3] or A[1]<B[3]<A[3]) :
            if A[1]<B[1]<A[3] :
              C=[B[0],B[1],A[2],A[3]]         
            else:
              C=[B[0],A[1],A[2],B[3]]
            S=-abs(C[0]-C[2]+C[1]-C[3])*2
            return(S)
    else:
         return(-abs((B[0]-B[2])+(B[1]-B[3]))*2)
    return(0)
#A=coordinates[0]
#B=coordinates[1]
#caculate(A,B)
#abs((A[0]-A[2])+(A[1]-A[3]))*2
result=0
i=0
m=0
reduce=0
S=0
while i< len(coordinates):
    A=coordinates[i]
    S=abs((A[0]-A[2])+(A[1]-A[3]))*2
    i=i+1
    m=i
    while m< len(coordinates):
        B=coordinates[m]
        reduce=reduce+caculate(A,B)
        m=m+1
        print('A=',A)
        print('B=',B)
        print('caclut=',caculate(A,B))      
        
    result=reduce+S+result
    reduce=0
    print(result)

        
