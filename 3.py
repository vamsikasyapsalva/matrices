l = input().split()
r = int(l[0])
c = int(l[1])
m = []
b = []
for  i in range(r):
    m.append([int(x) for x in input().split()])
    
print(m)
key = int(input())

for i in range(len(m)):
    for j in range(len(str(i))):
        if m[i][j] == key:
            print('('+str(i)+','+str(j)+')')
