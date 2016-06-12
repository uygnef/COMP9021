import random
b = list(range(1,13))
time=0
for _ in range(1000):
    c = set()
    not_all_in = True
    while not_all_in:
        time += 1
        a = random.randint(1, 12)
        c.add(a)
        for i in b:
            if i not in c:
                break
            else:
                if i == 12:

                    not_all_in = False

print(time/1000)


