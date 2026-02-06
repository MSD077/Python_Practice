class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windows_sum = sum(nums[:k])
        max_sum = windows_sum

        for i in range(k,len(nums)):
            windows_sum = windows_sum-nums[i-k]+nums[i]
            max_sum = max(windows_sum,max_sum)

        return max_sum/k