nums = [3,2,1,1,4]
curr_jump_hurdle = len(nums)-2
ret_val = True

print (nums)

for ind in reversed( range(len(nums)-1)):
    # if (nums[ind]==0):
    #     curr_jump_hurdle = ind
    #     ret_val = False
    #     continue

    
    if ((ind+nums[ind] )> curr_jump_hurdle ): 
        curr_jump_hurdle= ind-1
        ret_val=True
    else:
        ret_val = False

    
    

print  (ret_val)

