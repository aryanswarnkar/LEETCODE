class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
           if arr.count(arr[i])==1:
            k-=1
            if k==0:
                return arr[i]

        return ""
        
        
