class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev=0
        tot=0
        for i in bank:
            curr=i.count('1')
            if curr>0:
                tot+=prev*curr 
                prev=curr

        return tot           
