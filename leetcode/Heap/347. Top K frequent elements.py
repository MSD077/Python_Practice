#Heap solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        import heapq

        count = Counter(nums)

        min_heap =[]

        for num, freq in count.items():
            heapq.heappush(min_heap,(freq,num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [nums for freq,nums in min_heap]