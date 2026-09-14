242. Valid Anagram

Pattern

Arrays & Hashing. Whenever a problem asks whether two strings contain the same characters with the same frequency, use a HashMap to count and compare them.

Approach

Brute force: sort both strings and compare them — O(n log n) time, O(n) space.
Optimized: check if both strings have the same length. Then walk through both strings and count the frequency of each character using two HashMaps.
If the frequency of any character is different → not an anagram.
Otherwise → they are an anagram.

Complexity

Time: O(n) — one pass to count characters and one pass to compare the frequencies.
Space: O(n) — in the worst case, the HashMaps store all n characters.

What I missed on the first try

The key idea was realizing that anagrams don't need to have the same order. They only need to have the same characters with the same frequencies, so I used HashMaps to count and compare each character.