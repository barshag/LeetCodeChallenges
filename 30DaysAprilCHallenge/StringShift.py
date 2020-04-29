#shift a string (left/right)*amount : n times.
str_input ="xqgwkiqpif"
shift=[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
 #= [[1,1],[1,1],[0,2],[1,3]]
curr_dir =1
curr_amount=0
ret_str =""
for item in shift:
    print("curr amount:"+str(curr_amount) +"curr_dir:" + str(curr_dir))
    if (curr_dir!=item[0]):
        if (item[1]>curr_amount):
            curr_dir =1 -curr_dir #switch direction
            curr_amount =item[1] - curr_amount
        else:
            curr_amount = curr_amount - item[1] #not need to change directions
    else:
        curr_amount=curr_amount+item[1] 

#now we can rid of un-neccessary loops
curr_amount= curr_amount% len(str_input)

print("curr amount:"+str(curr_amount) +"curr_dir:" + str(curr_dir))



if (curr_dir==1):
    ret_str = str_input[len(str_input)-curr_amount:]
    ret_str = ret_str + str_input[0:len(str_input)-curr_amount]

if (curr_dir==0):
    ret_str = str_input[curr_amount:]
    ret_str = ret_str +str_input[0:curr_amount]


print (ret_str)

