# 347. Top K Frequent Elements

## Problem

Given an array of integers, return the `k` numbers that appear most frequently.

## Pattern

**Arrays & Hashing / Bucket Sort.** Count how often each number appears, then use buckets based on frequency to collect the most frequent numbers.

## Approach

1. **Brute force:** count the frequency of each number, sort the numbers by their frequency, and return the top `k` — O(n log n) time.

2. **Optimized:** use a HashMap to count the frequency of each number. Then create buckets where the index represents the frequency.
For each number, put it into the bucket that matches its frequency.

Start from the bucket with the highest frequency and move down, adding numbers to the result until we have `k` numbers.

## Complexity

- **Time:** O(n) — counting frequencies and going through the buckets both take linear time.
- **Space:** O(n) — the HashMap and buckets can store up to n elements.

## What I missed on the first try

The key idea was using the frequency of each number as the bucket index. This avoids sorting and gives an O(n) solution.