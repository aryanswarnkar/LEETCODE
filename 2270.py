nums=[10,4,-8,7]
res=len(nums)*[0]
res[0]=nums[0]
c=0
for i in range(1,len(nums)):
    res[i]=res[i-1]+nums[i]
for i in res:
    if i>sum(nums)-i:
        c+=1       