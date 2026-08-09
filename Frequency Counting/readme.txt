6. Frequency Counting
The Frequency Counting pattern uses hash maps or arrays to count occurrences of elements. It transforms O(n^2) lookup problems into O(n) by trading space for time.

When to use
Finding duplicates or unique elements

Checking if two collections have same elements

Finding elements that appear k times

Anagram problems

Template
// Using HashMap
Map<Integer, Integer> freq = new HashMap<>();
for (int num : nums) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}

// Using array (when range is known)
int[] freq = new int[26]; // for lowercase letters
for (char c : str.toCharArray()) {
    freq[c - 'a']++;
}

// Finding element with specific frequency
for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
    if (entry.getValue() == target) {
        return entry.getKey();
    }
}
Sample Problem
Valid Anagram: Given two strings s and t, return true if t is an anagram of s.

Example:
Input: s = "anagram", t = "nagaram"

Output: true

Step-by-Step Walkthrough:
s = "anagram", t = "nagaram"

Step 1: Count frequencies in s
  freq = {a: 3, n: 1, g: 1, r: 1, m: 1}

Step 2: Decrement frequencies using t
  't' -> n: freq[n] = 1 - 1 = 0
  't' -> a: freq[a] = 3 - 1 = 2
  't' -> g: freq[g] = 1 - 1 = 0
  't' -> a: freq[a] = 2 - 1 = 1
  't' -> r: freq[r] = 1 - 1 = 0
  't' -> a: freq[a] = 1 - 1 = 0
  't' -> m: freq[m] = 1 - 1 = 0

Step 3: Check all frequencies are 0
  freq = {a: 0, n: 0, g: 0, r: 0, m: 0}
  All zero -> Return true
Practice Problems
Valid Anagram (LeetCode #242)

Group Anagrams (LeetCode #49)

Top K Frequent Elements (LeetCode #347)

First Unique Character in a String (LeetCode #387)
