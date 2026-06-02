n = int(input())
counter = 0
s = []

for i in range(n):
    l = int(input())
    counter += l
    s.append(counter)
    counter = l

print(s[1:])

