data_file=input('Which data file do you want to use? ')

def caculate(verti):
  s=0
  for m in verti:
    b=m[0]
    a=m[1]
    while a<m[3]:
      for n in verti:
        if n[1]<=a<n[3] and n[0]<b<n[2]:
          a=a+1
          break
        elif n==verti[-1]:
          a=a+1
          s=s+1
  return(s)
dic=[]
with open(data_file) as file:
    for word in file:
      word=word.strip()
      word=word.split(' ')
      dic=dic+word
i=0
horizon=[]
while i < len(dic):
    a=min(int(dic[i]),int(dic[i+2]))
    b=min(int(dic[i+1]),int(dic[i+3]))
    A=[a,b]
    a=max(int(dic[i]),int(dic[i+2]))
    b=max(int(dic[i+1]),int(dic[i+3]))
    B=[a,b]
    horizon.append(A+B)
    i=i+4
horizon.sort()

i=0
verti=[]
while i < len(dic):
    b=min(int(dic[i]),int(dic[i+2]))
    a=min(int(dic[i+1]),int(dic[i+3]))
    A=[a,b]
    b=max(int(dic[i]),int(dic[i+2]))
    a=max(int(dic[i+1]),int(dic[i+3]))
    B=[a,b]
    verti.append(A+B)
    i=i+4
verti.sort()

S=caculate(verti)*2+2*caculate(horizon)
print('The perimeter is : ',S)

   

