nums=[1,5,0,3,5]
nums.sort()
i=0
op=0
while i<len(nums):
    if nums[i]==0:
        i=i+1
    else:
        min=nums[i]
        for j in range(i,len(nums)):
            nums[j]-=min
        op+=1
print(op)                 

        
