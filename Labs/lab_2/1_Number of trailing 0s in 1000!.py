import math

s=0
a=math.factorial(1000)
while a%10 == 0:
    s += 1
    a=a//10
print('There are {} trailing 0s in 1000!.'.format(s))
