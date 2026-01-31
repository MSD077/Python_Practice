## Day 1 – Jan 28, 2026

Problems Solved:
- Leetcode 347. Top K Frequent Elements

Topics:
- Hash Map
- Bucket Sort
- Heap

Notes:
- Used two approaches - sorting approach and bucket array approach
- Both use a hash map to count frequencies first
- Sorting approach has O(N log N) time complexity
- Bucket array approach has O(N) time complexity

## Day 2 – Jan 29, 2026

Problem:
- Leetcode 242. Valid Anagram
d
Topics:
- Hash Map
- String

Notes:
- Used hashmap / Counter to count character frequencies
- Compared counts of both strings
- Time Complexity: O(n)

## Day 3 – Jan 30, 2026

Problem:
- Leetcode 238. Product of Array Except Self

Topics:
- Array
- Prefix Product
- Suffix Product

Notes:
- Used prefix (left) and suffix (right) product technique
- Avoided division to handle zero cases
- First pass stores product of elements to the left
- Second pass multiplies product of elements to the right
- Time Complexity: O(n)
- Space Complexity: O(1) extra space (excluding output)