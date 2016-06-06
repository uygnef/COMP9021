def solve(ava_digits, desired_sum):
    if ava_digits < 0:
        return 0
    if ava_digits == 0:
        if desired_sum ==0:
            return 1
        return 0
    return(solve(ava_digits//10,desired_sum)+solve(ava_digits//10,desired_sum - ava_digits%10))

print(solve(12234,5))
