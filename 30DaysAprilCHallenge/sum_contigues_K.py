nums =[1,1,1]
k=2
left=0
right =0
curr_sum=nums[0]
ret=0

while (left <len(nums)):
    if (curr_sum==k):
        curr_sum= ((curr_sum - nums[left])+nums[right])
        ret=ret+1
        if (right<len(nums)-1):
            right=right+1
        continue
    if(curr_sum>k):
        curr_sum=curr_sum-nums[left]
        left=left+1
        continue
    else: #<K
        if (right<len(nums)-1):
            right=right+1
            curr_sum=curr_sum+nums[right]

        
print (ret)