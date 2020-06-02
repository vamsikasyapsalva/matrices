def sp(a,m):
    
    left = top = 0
    bottom = r - 1
    right = c - 1
    index = 0
    
    while True:
    
        if left > right:
            break
    
        for i in range(left,right+1):
            m[top][i] = a[index]
            index = index + 1
        top = top + 1
        
        if top > bottom:
            break
        
        for i in range(top,bottom + 1):
            m[i][right] = a[index]
            index = index + 1
        right = right - 1
        
        if left > right:
            break
        
        for i in range(right,left-1,-1):
            m[bottom][i] = a[index]
            index = index + 1
        bottom = bottom - 1
        
        if top > bottom:
            break
        
        for i in range(bottom,top-1,-1):
            m[i][left] = a[index]
            index = index + 1
        left = left + 1
        
    for i in m:
        print(i)
    

a = list(map(int,input().split(',')))
l = input().split()
r = int(l[0])
c = int(l[1])
m = [[0 for i in range(c)]for i in range(r)]
sp(a,m)   
