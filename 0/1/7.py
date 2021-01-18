def snail(snail_map):
    print(snail_map)
    if snail_map == [[]]:
        return []
    n = len(snail_map)
    print(type(snail_map[0]))
    snail_map= [[-1 for i in range(n + 2)]]  + snail_map
    print(snail_map)
    for i in range(1, n + 1):
        k = snail_map[i]
        snail_map[i] = [-1] + snail_map[i] + [-1]
    snail_map += [[-1] * (n + 2)]
    print(snail_map)
    k = 1
    i = 1
    j = 1
    nap = 1
    ans = []
    while (k <= n * n):
        print(i, j)
        ans.append(snail_map[i][j])
        if (n > 4):
            print(snail_map[2][5])
        snail_map[i][j]= -1
        k+=1
        if nap==1:
            j+=1
            if snail_map[i][j]== -1:
                i+=1
                j-=1
                nap = 2
        elif nap==2:
            i+=1
            if snail_map[i][j]==-1:
                i-=1
                j-=1
                nap = 3
        elif nap==3:
            j-=1
            if snail_map[i][j]==-1:
                i-=1
                j+=1
                nap = 4
        elif nap==4:
            i-=1
            if snail_map[i][j]==-1:
                i+=1
                j+=1
                nap = 1
    return ans
        
    
    
            
