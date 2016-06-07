a = 35642
r ={'$100':0,'$20':0,'$10':0,'$5':0,'$2':0,'$1':0}
result= sorted(r.items(), key=lambda d:int(d[0][1:]), reverse = True)
i=0
while a != 0:
    s = int(result[i][0][1:])
    m = a//s
    a = a%s
    if m != 0:
        print(result[i][0],m)
    i += 1
