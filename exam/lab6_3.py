word = 'abcsdefhigjrws'
current_start = 0
start = None
length = 0
current_length = 0
for _ in range(len(word)):
    current_start = _
    current_length = 0
    for i in word[current_start:]:
        if ord(i) == ord(word[current_start]) + current_length:
            print(current_start,current_length,i)
            current_length += 1
    if current_length > length:
        start = current_start
        length = current_length

for i in range(length):
    print(chr(ord(word[start])+i),end='')

