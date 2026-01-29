class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        
        sorted_list = sorted(count.items(), key = lambda x:x[1], reverse = True)

        return_list = []
        for num, count in sorted_list:
            if len(return_list) < k:
                return_list.append(num)

        return return_list