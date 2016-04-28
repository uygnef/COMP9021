from sys import exit
from math import factorial

try:
    nonnegative=int(input('Input a nonnegative integer: '))
except ValueError:
    print('Incorrect input, giving up...')
    exit()
if not nonnegative > 0:
    print('Incorrect input, giving up...')
    exit()        
#input the end

i=0
while nonnegative > factorial(i):
    i=i+1
i=i-1
#get the largest i

y=nonnegative
result=0
for a in range(i,0,-1):
    f=y//factorial(a)
    y=y%factorial(a)
    result=f*10**(a-1)+result

print('Decimal {} reads as {} in factorialbase.'.format(nonnegative,result))
