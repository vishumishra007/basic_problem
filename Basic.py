def city_cont(lis):
    n,k,x,y = lis[0],lis[1],lis[2],lis[3]
    reach = []
    while(True):
        if x == y:
            return('YES')
        x = x + k
        if x>n:
            x = x%k
            if x in reach:
                return 'NO'
            else :
                return 'YES'
    return 'NO'
                
T = int(input())
while(T>0):
    lis = list(map(int, input().rstrip().split()))
    result = city_cont(lis)
    print(result)
    T = T-1
