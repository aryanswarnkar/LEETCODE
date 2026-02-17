class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert to string, replace the first '6' with '9', convert back to int
        return int(str(num).replace('6', '9', 1))
