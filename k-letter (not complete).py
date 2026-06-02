n = int(input())
s = []
k = int(input())


for i in range(1, n + 1):
    stroke = input()
    stroke = stroke[k - 1]
    s.append(stroke)    
    


print(s)
