s = input().lower().split()
count = {}

for n in s:
    

    if n not in count:
        count[n] = 1
    else:
        count[n] += 1

for n in count:
    print(n, count[n])