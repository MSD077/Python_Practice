class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1

        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in count.items():
            buckets[count].append(num)
        
        output = []

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                if len(output) < k:
                    output.append(num)
        return output