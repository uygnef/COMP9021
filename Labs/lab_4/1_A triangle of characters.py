while True:
    try:
        height = int(input('Enter strictly positive number: '))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')

A_code = ord('A')
c = A_code

for i in range(1, height + 1):
    for j in range(height - i):
        print(' ', end='')
    
    for k in range(1, i):
        print(chr(c), end = '')
        c = (c - A_code +1) % 26 + A_code

    print(chr(c), end = '')
    for k in range(1, i):
        c = (c - A_code +25) % 26 + A_code
        print(chr(c), end = '')
    print()
    c = (i*(i+1)//2 ) % 26 + A_code
