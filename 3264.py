nums = [2,1,3,5,6]
k = 5
m=2

# Output: [8,4,6,5,6]
while k!=0:
    for i in range(len(nums)):
        if nums[i]==min(nums):
            nums[i]=nums[i]*m
            k=k-1
            break
print(nums)    