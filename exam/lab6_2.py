def solve(a,b,c):
    if not a and c == b:
        return True
    if not b and c == a:
        return True
    if not a or not b:
        return False
    if a[0] == c[0] and solve(a[1:],b,c[1:]):
        return True
    if b[0] == c[0] and solve(a,b[1:],c[1:]):
        return True
    return False
print(solve('a','bcd','abc'))