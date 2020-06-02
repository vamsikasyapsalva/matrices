l = input().split()
r = int(l[0])
c = int(l[1])
m = []
k = []
s = 0
for i in range(r):
    m.append([int(x) for x in input().split()])
    
#print(m)

for i in m:
    for j in i:
        if j < 0:
            s += 1
            
print(s)
