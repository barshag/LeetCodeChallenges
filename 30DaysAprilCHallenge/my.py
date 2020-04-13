import random, math

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

#List =[[]]
#print (rec( [2,7,4,1,8,1]))


# rect_num=0
# circle_num=0
# for ind in range(1,1000000):
#     x=random.uniform(0, 1)
#     y=random.uniform(0, 1)
#     if(math.sqrt( (x)**2 +(y)**2)<1): 
#         circle_num=circle_num+1

#     rect_num=rect_num+1
        
# #print (rect_num/circle_num )
# print (4*(circle_num/rect_num))

#def add_elem()


# L= [0,0,1,1,1,1,0,0,0,0]
# #dict = {"1":"dasdsa"}
# dict = {}
# #print ( "1" in dict)
# count=0
# dict[0] = {'first':-1, 'lenght':0}
# #print (dict)
# for ind in range(len(L)):
#     if (L[ind] ==1):
#         count =count +1
#         if count in dict:
#             #print (dict)
#             dict[count] ={'first':dict[count]['first'] ,  'lenght':(ind-dict[count]['first'])}
#         else:
#             dict[count] ={'first':ind, 'lenght':0}
#     else: #=='0'
#         count =count -1
#         if count in dict:
#             #print (dict[count])
#             dict[count] ={'first':dict[count]['first'], 'lenght':(ind-dict[count]['first'])}
#         else:
#             dict[count] ={'first':ind, 'lenght':0}

# max = -1
# for key in dict:
#      if(dict[key]['lenght']>max):   
#         max = dict[key]['lenght']
# print (max)
# #print (max(dict, key =dict['lenght']))


get_bin = lambda x, n: format(x, 'b').zfill(n)

x= (get_bin(10,32))
y= (get_bin(20,32))
count =0
for ind in range(32):
    if(str(x[ind]) !=str(y[ind])):
        count=count +1

print( count)