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

## Day 4 – Jan 31, 2026

Problem:    
- Leetcode 128. Longest Consecutive Sequence

Topics:
- Hash Set
- Array
- Greedy

Notes:
- Converted array to set for O(1) lookup operations
- Only start counting from sequence beginnings (when i-1 not in set)
- Avoided redundant work by skipping elements in the middle of sequences
- Used greedy approach to find maximum consecutive length
- Time Complexity: O(n)
- Space Complexity: O(n)

## Day 5 – Feb 01, 2026

Problem:
- Leetcode 217. Contains Duplicate

Topics:
- Array
- Hash Set

Notes:
- Used a set to track unique elements
- Compared length of array vs set
- Time Complexity: O(n)
- Space Complexity: O(n)

## Day 6 – Feb 02, 2026

Problem:
- Leetcode 448. Find All Numbers Disappeared in an Array

Topics:
- Array
- In-place marking

Notes:
- Used index mapping (value → index)
- Marked visited indices by negating values
- Missing numbers correspond to positive indices
- Time Complexity: O(n)
- Space Complexity: O(1) (ignoring output array)

## Day 7 – Feb 03, 2026

Problem:
- Leetcode 169. Majority Element

Topics:
- Array
- Boyer–Moore Voting Algorithm

Notes:
- Used cancellation logic to find majority element
- Maintains candidate and counter
- Optimal O(n) time and O(1) space solution

## Day 8 – Feb 04, 2026

Problem:
- Leetcode 350. Intersection of Two Arrays II

Topics:
- Hash Map
- Frequency Counting

Notes:
- Built frequency map on smaller array
- Iterated through second array and decremented counts
- Time: O(n + m)
- Space: O(min(n, m))