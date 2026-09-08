# 1. Two Sum

[LeetCode link](https://leetcode.com/problems/two-sum/) · Difficulty: Easy

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the
two numbers that add up to `target`. Exactly one valid answer exists.

## Pattern

**Arrays & Hashing.** Whenever a problem needs "does the complement of what I'm looking
at already exist somewhere in what I've seen," a hashmap turns an O(n) lookup into O(1).

## Approach

1. **Brute force:** check every pair — O(n²) time, O(1) space.
2. **Optimized:** walk the array once. At each index, compute `complement = target - nums[i]`.
   If `complement` is already a key in the hashmap, we've found our pair. Otherwise, store
   `nums[i] -> i` and keep going. This works in one pass because by the time we'd need the
   complement, it's already been recorded.

## Complexity

- **Time:** O(n) — one pass, O(1) hashmap operations.
- **Space:** O(n) — worst case, we store all n elements before finding a match.

## What I missed on the first try

Initially checked `if nums[i] in seen` instead of checking for the *complement* — that finds
duplicates of the current value, not pairs summing to target. Fixed by computing
`target - nums[i]` and checking for that instead.
