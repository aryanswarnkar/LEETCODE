# nums = [2,1,3,4,5,2]
# # Output: 7
# score=[]
# k=[]
# for i in range(len(nums)):
#     if nums[i]==min(nums):
#         score.append(min(nums))
#         if i==0:
#             k.append(nums[i+1])
#         if i==len(nums)-1:
#             k.append(nums[i-1])
#         else:    
#             k.append(nums[i-1])
#             k.append(nums[i+1])
# print(nums)            
nums = [2,1,3,4,5,2]
# [1, 2, 2, 3, 4, 5]
k=sorted(nums)
score=[]
j=0
for i in range(len(nums)):
    
    min=k[j]
    score.append(min)
    nums.pop(min)
    
    

