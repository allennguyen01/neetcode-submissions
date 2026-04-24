class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            if n-1 in numSet:
                continue
            
            # beginning of seq
            l = 0
            while n + l in numSet:
                l += 1
            res = max(res, l)

        # [0,3,2,5,4,6,1,1] -> 7
            
        return res