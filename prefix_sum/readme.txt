1. Prefix Sum

The Prefix Sum pattern involves preprocessing an array to create a new array where each element at index i represents the sum of all elements from the start up to i. This allows for O(1) sum queries on any subarray.

When to use
Multiple sum queries on subarrays

Finding subarrays with a target sum

Calculating cumulative totals

Template
// Build prefix sum array
int[] prefix = new int[n + 1];
for (int i = 0; i < n; i++) {
    prefix[i + 1] = prefix[i] + nums[i];
}

// Query sum of range [left, right]
int rangeSum = prefix[right + 1] - prefix[left];
Sample Problem
Range Sum Query: Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].

Example:
Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3

Output: 9

Step-by-Step Walkthrough:
nums = [1, 2, 3, 4, 5, 6]

Step 1: Build prefix sum array
  prefix[0] = 0
  prefix[1] = 0 + 1 = 1
  prefix[2] = 1 + 2 = 3
  prefix[3] = 3 + 3 = 6
  prefix[4] = 6 + 4 = 10
  prefix[5] = 10 + 5 = 15
  prefix[6] = 15 + 6 = 21

  prefix = [0, 1, 3, 6, 10, 15, 21]

Step 2: Query sum for range [1, 3]
  sum = prefix[3 + 1] - prefix[1]
  sum = prefix[4] - prefix[1]
  sum = 10 - 1 = 9
Practice Problems

Range Sum Query - Immutable (LeetCode #303)

Contiguous Array (LeetCode #525)

Subarray Sum Equals K (LeetCode #560)

Product of Array Except Self (LeetCode #238)
