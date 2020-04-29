nums = [0]
CanJumpList = [0]*len(nums) #initilize the list


print (nums)

for ind in reversed( range(len(nums))):
    if ((ind+nums[ind] )>= len(nums)-1 ): 
        CanJumpList[ind] =1
        continue


    for pot in reversed(range(nums[ind]+1)): #Potential
        if (CanJumpList[ind+pot] ==1):
            CanJumpList[ind] =1
            break
        


print (CanJumpList)

print (CanJumpList[0]) #Returned value
        
