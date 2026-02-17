class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        count = Counter(tasks)
        max_count = max(count.values())
        max_count_tasks = sum(1 for c in count.values() if c == max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)