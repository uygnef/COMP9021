a=[0 for i in range(101)]

for i in range(1,101):
    for n in range(i,101,i):
        a[n] = not a[n]    
        
print('{} prisoners find their doors open after 100 rounds.'.format(
                           sum(a[i] for i in range(1, 101) if a[i])))
