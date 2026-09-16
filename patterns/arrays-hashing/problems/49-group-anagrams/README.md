# 49. Group Anagrams

## Problem

Given a list of strings, group together the strings that are anagrams of each other. Strings belong in the same group if they contain the same characters with the same frequencies.

## Pattern

**Arrays & Hashing.** When we need to group strings with the same character frequencies, use a frequency count as a key in a HashMap.

## Approach

1. **Brute force:** compare each string with every other string and check if they are anagrams — O(m² × n) time.

2. **Optimized:** use a HashMap where each key represents the frequency of the 26 lowercase letters.

For each string:
- Create an array of 26 zeros.
- Count how many times each character appears.
- Convert the frequency array into a tuple so it can be used as a HashMap key.
- Add the string to the list for that key.

Strings with the same character frequencies will have the same key, so they are grouped together.

## Complexity

- **Time:** O(m × n) — we go through each character of each string once.
- **Space:** O(m) — the HashMap stores a group for each string in the worst case.

## What I missed on the first try

I initially used sorting to create a common key for each anagram. The better approach is to count the frequency of each character and use that frequency count as the key, which improves the time complexity from O(m × n log n) to O(m × n).