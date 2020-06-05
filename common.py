l = input().split()
r = int(l[0])
c = int(l[1])
d = []
s = []
k = []
for i in range(r):
    d.append([int(x) for x in input().split()])
print(d)
a = set.intersection(*map(set, d))
print(list(a))
