class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            elif len(minHeap) >= k and minHeap[0] < n:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, n)

        return minHeap[0]
