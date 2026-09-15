# 217. Contains Duplicate

# Problem

Given an array of numbers, return True if any number appears more than once. Otherwise, return False.

# Pattern

**Arrays & Hashing.** Whenever a problem asks whether an element has appeared before, use a HashSet for fast lookup.

# Approach

**Brute force:** compare every element with every other element — O(n²) time, O(1) space.
**Optimized:** walk through the array once. For each number, check if it already exists in the set.
If it exists → duplicate found.
Otherwise → add it to the set and continue.

# Complexity

**Time:** O(n) — one pass, with average O(1) set lookup.
**Space:** O(n) — in the worst case, we store all n elements.

# What I missed on the first try

The key idea was realizing that I don't need to compare every pair. I can remember the numbers I've already seen using a HashSet and check each new number against it.