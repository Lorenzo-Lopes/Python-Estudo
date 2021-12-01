s=0
tot =0
for c in range(1, 500, 2):
    if (c % 3) == 0:
        s += c
        tot += 1
print(s)
print(tot)