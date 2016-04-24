all_nonzero_digits = set(range(1, 10))
for a in range(1, 10):
    for b in range(1, 10):
        candidate = (a        , 15 - a - b, b        ,
                     5 + b - a, 5         , 5 + a - b,
                     10 - b   , a + b - 5 , 10 - a   )
        if set(candidate) == all_nonzero_digits:
            print('  {:}  {:}  {:}\n  {:}  {:}  {:}\n  {:}  {:}  {:}\n'.format(*candidate))
