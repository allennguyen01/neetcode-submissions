class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefixes: [0, 2, 1, 2, 4]
        # prefixMap: {0: 1, 2: 2, 1: 1, 4: 1}

        currSum = 0
        prefixSums = {0: 1}
        res = 0

        # 1. get the running sum
        # 2. check if current subarray has any internal subarrays that would equal k
        # 3. check freq of (k-currSum), increment freq to res
        # 4. update prefix map with currSum

        for i in range(len(nums)):
            currSum += nums[i]
            freq = currSum - k
            res += prefixSums.get(freq, 0)
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

        return res
