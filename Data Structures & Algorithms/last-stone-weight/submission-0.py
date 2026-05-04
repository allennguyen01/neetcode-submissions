class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stoneWeight for stoneWeight in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            firstStone = -heapq.heappop(maxHeap)
            secondStone = -heapq.heappop(maxHeap)

            if firstStone > secondStone:
                newStone = firstStone - secondStone
                heapq.heappush(maxHeap, -newStone)

        return -maxHeap[0] if len(maxHeap) else 0