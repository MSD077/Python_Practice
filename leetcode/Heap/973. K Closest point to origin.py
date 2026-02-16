class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        min_heap = []

        for x, y in points:
            distance = (x*x)+(y*y)
            heapq.heappush(min_heap,(-distance,x,y))

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return [[x,y] for distance, x, y in min_heap]



       
        