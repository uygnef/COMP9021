def fenjie(a):
    divisor=[]
    for i in range(1,a//2+1):
      if a%i==0:          
          divisor.append(i)
    return divisor
    
for i in range(100,999):
    if i==sum(i for i in fenjie(i)):
        print(i)
