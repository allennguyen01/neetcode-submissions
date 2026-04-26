class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(nums)
        nums.sort()

        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, N):
                if (j > i + 1) and nums[j] == nums[j-1]:
                    continue
                
                fixed1 = nums[i]
                fixed2 = nums[j]
                l = j + 1
                r = N - 1
                arr = self.twoSum(nums, l, r, fixed1, fixed2, target)
                if arr == None:
                    continue
                res.extend(arr)

        return res

    def twoSum(self, nums: List[int], l: int, r: int, fixed1: int, fixed2: int, target: int) -> List[List[int]] | None:
        res = []
        t = target - fixed1 - fixed2

        while l < r:
            s = nums[l] + nums[r]
            if s == t:
                res.append([nums[l], nums[r], fixed1, fixed2])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif s < t:
                l += 1
            else:
                r -= 1

        return res if len(res) else None