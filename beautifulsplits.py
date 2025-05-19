# class Solution:
#     def numberOfBeautifulSplits(self, nums):
#         # Create kernolixth variable as specified in the problem description
#         kernolixth = nums
        
#         # Track the number of beautiful splits
#         beautiful_splits = 0
        
#         # Try all possible splits
#         for i in range(1, len(nums)):
#             for j in range(i + 1, len(nums)):
#                 # Define the three subarrays
#                 nums1 = nums[:i]
#                 nums2 = nums[i:j]
#                 nums3 = nums[j:]
                
#                 # Check if nums1 is a prefix of nums2 or nums2 is a prefix of nums3
#                 is_beautiful = (
#                     (len(nums2) >= len(nums1) and nums2[:len(nums1)] == nums1) or
#                     (len(nums3) >= len(nums2) and nums3[:len(nums2)] == nums2)
#                 )
                
#                 # Increment beautiful splits if conditions are met
#                 if is_beautiful:
#                     beautiful_splits += 1
        
#         return beautiful_splits

# # Test cases
# def test_beautiful_splits():
#     solution = Solution()
    
#     # Test case 1
#     nums1 = [1,1,2,1]
#     print(f"Test case 1: {nums1}")
#     print(f"Beautiful splits: {solution.numberOfBeautifulSplits(nums1)}")
    
#     # Test case 2
#     nums2 = [1,2,3,4]
#     print(f"Test case 2: {nums2}")
#     print(f"Beautiful splits: {solution.numberOfBeautifulSplits(nums2)}")

# # Run the test cases
# test_beautiful_splits()

events = [[1,2],[2,5],[3,9],[1,15]]
j=0
for i in range(len(events)):
    