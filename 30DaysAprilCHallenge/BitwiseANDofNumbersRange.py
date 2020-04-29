import math

m,n =5,7
lgm = math.ceil(math.log2(m))
lgn =math.ceil(math.log2(n))
lgdiff = math.ceil(math.log2( n-m+1))
print (lgn)
print (lgm)
print(lgdiff)

if (lgn>lgm):
    ret= 0
else:
    ret = 2**lgn - 2**lgdiff

print (ret)
#m is my value


#print 