def solve(ava, desired):
    if desired<0:
        return 0
    if ava == 0:
        if desired == 0:
            return 1
        return 0
    return(solve(ava//10,desired) +
           solve(ava//10,desired - ava%10))

print(solve(12234,5))