a = 'abcefg'

start_ord = None
length = 0
end = 0
for i in range(len(a)):
    current_start = ord(a[i])
    current_length = 1
    for j in range(i,len(a)):
        if current_start == ord(a[j])-current_length:
            current_length += 1

    if current_length > length:
        start_ord = current_start
        length = current_length
    current_start += current_length
print(length)
i = start_ord
for _ in range(length):
    print(chr(i),end = '')
    i += 1
