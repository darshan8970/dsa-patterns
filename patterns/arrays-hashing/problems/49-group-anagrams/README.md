# 49. Group Anagrams

## Problem

Given a list of strings, group together the strings that contain the same characters. The order of the strings in the result does not matter.

## Pattern

**Arrays & Hashing.** When we need to group strings that have the same characters, create a common key and use a HashMap to store strings with the same key.

## Approach

1. **Brute force:** compare each string with other strings and check if they are anagrams — O(n² × k log k) time.

2. **Optimized:** sort each string to create a common key. Use a HashMap where the key is the sorted string and the value is a list of strings. Strings with the same sorted key are placed in the same group.

## Complexity

- **Time:** O(n × k log k) — we sort each of the n strings, where k is the average length of a string.
- **Space:** O(n × k) — we store all the strings in the HashMap.

## What I missed on the first try

The main idea was realizing that anagrams can be turned into the same key by sorting their characters. I then used that key in a HashMap to group the strings.