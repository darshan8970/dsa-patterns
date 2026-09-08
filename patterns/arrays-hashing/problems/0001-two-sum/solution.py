"""
LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # problem guarantees a solution, so this should never hit


if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    print("All test cases passed.")
