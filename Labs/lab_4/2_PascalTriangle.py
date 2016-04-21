n=input('n=')
while True:
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print('WWWWWrong')
pascal_triangle = [[0 for i in range(n)]for i in range(n)]

pascal_triangle[0][0]=1
for i in range(1,n):
    pascal_triangle[i][0]=1
    pascal_triangle[i][i]=1
    for b in range(1,i):
        pascal_triangle[i][b]=pascal_triangle[i-1][b]+pascal_triangle[i-1][b-1]


for i in range(n):
    print(' '*(n-i),end='')
    for a in range(i+1):
        print(pascal_triangle[i][a], end='')
        print(' ',end='')
    print()
    

