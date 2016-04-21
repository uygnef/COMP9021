code=input('integer')

try:
    s=bin(int(code))    
except TypeError:
    print('wrong')

m=[]
a=len(s)
for i in str(s):
    a -=1
    if i == '1':
        m.append(a)
print(set(m))
