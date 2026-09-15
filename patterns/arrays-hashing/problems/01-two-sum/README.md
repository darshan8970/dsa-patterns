# 1. Two Sum

# Problem

Given an array of numbers and a target, find two different numbers that add up to the target. Return the indices of those two numbers.

# Pattern

**Arrays & Hashing.** When we need to find two numbers that add up to a target, we can use a HashMap to quickly check if the number we need was already seen.

# Approach

**Brute force:** check every possible pair of numbers to see if their sum equals the target — O(n²) time, O(1) space.

**Optimized:** go through the array once. For each number, calculate target - nums[i] to find the number we need. If that number is already in the HashMap, return its index and the current index. Otherwise, store nums[i] -> i in the HashMap and continue.

# Complexity

**Time:** O(n) — we go through the array once, and HashMap lookup takes O(1) on average.

**Space:** O(n) — in the worst case, we store all n elements in the HashMap.


# What I missed on the first try

Got it after understanding that I don't need to check every pair. For each number, I can find the number I need and check if I have already seen it using a HashMap.