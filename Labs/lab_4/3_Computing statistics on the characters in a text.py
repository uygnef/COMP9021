a=[0 for i in range(10)]
with open('test_1.txt',encoding='utf-8') as file:
    for line in file:
        for c in line:
            if c.isdigit():
                if a[int(c)] ==0:
                    a[int(c)]=1
                 
                else:
                    a[int(c)] += 1
for i in range(10):
    if a[i] != 0:
        print(i,end=' ')
print()
for i in range(10):
    if a[i] != 0:
        print(a[i],end=' ')
