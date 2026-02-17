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

## Day 9 – Feb 05, 2026

- Leetcode 643. Maximum Average Subarray I

Topics:
- Sliding Window
- Array

Notes:
- Used fixed-size sliding window
- Time: O(n)
- Space: O(1)

## Day 10 – Feb 06, 2026

Problem:
- Leetcode 1480. Running Sum of 1D Array

Topics:
- Prefix Sum
- Array

Notes:
- Computed cumulative sum in-place
- Updated each element with sum of all previous elements
- Time: O(n)
- Space: O(1)

## Day 11 – Feb 07, 2026

Problem:
- Leetcode 704. Binary Search

Topics:
- Binary Search

Notes:
- Implemented iterative search on sorted array. This solution is not optimized.
- Time: O(n)
- Space: O(1)

## Day 12 – Feb 08, 2026

Problem:
- Leetcode 704. Binary Search

Topics:
- Binary Search

Notes:
- Implemented iterative binary search on sorted array. Optimized solution
- Reduced search space by half each iteration
- Time: O(log n)
- Space: O(1)

## Day 13 – Feb 09, 2026

Problem:
- Leetcode 278. First Bad Version

Topics:
- Binary Search

Notes:
- Used binary search to find the first bad version
- Time: O(log n)
- Space: O(1)

## Day 13 – Feb 09, 2026

Problem:
- Stratascratch SQL: Premium vs Freemium

Topics:
- SQL CTE
- Case
- Joins
- Group By

Notes:
- Joined user, account, and download tables
- Used conditional aggregation to count downloads by customer type
- Filtered dates where non-paying downloads exceed paying downloads
- Sorted results by earliest date

## Day 14 – Feb 10, 2026

Problem:
- Leetcode 167. Two Sum II – Input Array Is Sorted

Topics:
- Two Pointers

Notes:
- Used two pointers starting from both ends of sorted array
- Moved pointers based on current sum vs target
- Time: O(n)
- Space: O(1)

## Day 15 – Feb 11, 2026

Problem:
- Leetcode 20. Valid Parentheses

Topics:
- Stack

Notes:
- Used stack to track opening brackets
- Matched closing brackets using a hashmap
- Time: O(n)
- Space: O(n)

## Day 16 – Feb 12, 2026

Problem:
- Leetcode 121. Best Time to Buy and Sell Stock

Topics:
- Array
- Greedy

Notes:
- Tracked minimum price while iterating
- Calculated profit at each step
- Updated maximum profit in one pass
- Time: O(n)
- Space: O(1)

## Day 17 – Feb 13, 2026

Problem:
- Leetcode 215. Kth Largest Element in an Array

Topics:
- Heap (Priority Queue)

Notes:
- Maintained a min-heap of size k
- Pushed each element into heap
- Removed smallest element when heap size exceeded k
- Time: O(n log k)
- Space: O(k)

## Day 18 – Feb 14, 2026

Problem:
- Leetcode 347. Top K Frequent Elements (Heap solution)

Topics:
- Heap (Priority Queue)

Notes:
- Used Counter to count frequency of each element
- Stored (frequency, number) in a min-heap
- Maintained heap size k by removing smallest frequency
- Returned elements from heap as final answer
- Time: O(n log k)
- Space: O(n)

## Day 19 – Feb 15, 2026

Problem:
- Leetcode 973. K Closest Points to Origin

Topics:
- Heap (Priority Queue)

Notes:
- Computed squared distance (x^2 + y^2)
- Used max-heap (simulated with negative distance)
- Maintained heap size k by removing farthest point
- Heap always stored k closest points
- Time: O(n log k)
- Space: O(k)

## Day 20 – Feb 16, 2026

Problem:
- Leetcode 1046. Last Stone Weight

Topics:
- Heap (Max Heap)
- Greedy

Notes:
- Converted array into max-heap using negative values
- Repeatedly removed two largest stones
- Inserted difference back into heap if not equal
- Continued until one or zero stones remained
- Time: O(n log n)
- Space: O(n)

## Day 21 – Feb 17, 2026

Problem:
- Leetcode 621. Task Scheduler

Topics:
- Greedy
- Frequency Counting
- Mathematical Optimization

Notes:
- Identified most frequent task (max_count)
- Used formula: (max_count - 1) * (n + 1) + max_count_tasks
- Time: O(n)
- Space: O(1)
