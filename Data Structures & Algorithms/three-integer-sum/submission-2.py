class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. sort the array
        # 2. have a fixed target number, use 2 pointers to find the numbers that add up to target
        # 3. once I reach positive number, no more triplets so end loop

        # [-4, -1, -1, 0, 1, 2]

        nums.sort()
        res = []

        for i in range(len(nums)):
            target = nums[i]
            if i > 0 and target == nums[i-1]:
                continue
            if target > 0:
                break
            l = i + 1
            r = len(nums) - 1

            twoSumRes = self.sortedTwoSum(nums, target, l, r)
            if twoSumRes == None:
                continue

            res.extend(twoSumRes)

        return res

    def sortedTwoSum(self, nums, target, l, r):
        res = []

        while l < r:
            s = nums[l] + nums[r] + target
            if s == 0:
                res.append([nums[l], nums[r], target])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif s > 0:
                r -= 1
            else:
                l += 1

        return res if len(res) else None