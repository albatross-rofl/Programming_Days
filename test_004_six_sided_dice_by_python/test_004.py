import numpy as np

count_list = []

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for i in range (0, 100000):
    dice = np.random.randint(1, 7)
    if dice == 1:
        a += 1
    elif dice == 2:
        b += 1
    elif dice == 3:
        c += 1
    elif dice == 4:
        d += 1
    elif dice == 5:
        e += 1
    elif dice == 6:
        f += 1

count_list = [a, b, c, d, e, f]

print(count_list)
