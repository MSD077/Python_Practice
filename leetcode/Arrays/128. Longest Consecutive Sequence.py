class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        subsequence = 0
        nums = set(nums)

        for i in nums:
            length = 1
            if (i-1) in nums:
                continue
            while (i+length) in nums:
                length += 1
            subsequence = max(subsequence,length)

        return subsequence