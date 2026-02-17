class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap)>1:
            max1 = -heapq.heappop(max_heap)
            max2 = -heapq.heappop(max_heap)

            if max1 != max2:
                heapq.heappush(max_heap,-(max1-max2))

        return -max_heap[0] if max_heap else 0

        