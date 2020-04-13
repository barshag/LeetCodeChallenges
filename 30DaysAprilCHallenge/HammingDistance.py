import random, math

get_bin = lambda x, n: format(x, 'b').zfill(n)

x= (get_bin(10,32))
y= (get_bin(20,32))
count =0
for ind in range(32):
    if(str(x[ind]) !=str(y[ind])):
        count=count +1

print( count)