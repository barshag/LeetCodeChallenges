def rec(stones):
    print (stones[0])
    if (len(stones)==0):
        return 0
    if (len(stones)==1):
        return stones[0]

    stones.sort(reverse=True)
    print (stones)
    if (stones[0]==stones[1]):
        del stones[0]
        del stones[1]
    else:
        stones[0] = stones[0] -stones[1]
        del stones[1] 
    return rec(stones)
