The Sliding Window pattern maintains a window of elements and slides it across the array to find subarrays or substrings that satisfy certain conditions. It avoids recalculating overlapping parts of consecutive windows.

When to use
Contiguous subarray/substring problems

Finding maximum/minimum in window of size k

Longest/shortest substring with certain properties

Problems involving consecutive elements

Template
// Fixed-size window
int windowSum = 0;
for (int i = 0; i < n; i++) {
    windowSum += nums[i];
    if (i >= k - 1) {
        // process window
        result = Math.max(result, windowSum);
        windowSum -= nums[i - k + 1];
    }
}

// Variable-size window
int left = 0;
for (int right = 0; right < n; right++) {
    // expand window by including nums[right]

    while (window_condition_violated) {
        // shrink window from left
        left++;
    }

    // update result
}
Sample Problem
Maximum Sum Subarray of Size K: Find the maximum sum of any contiguous subarray of size k.

Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3

Output: 9

Step-by-Step Walkthrough:
nums = [2, 1, 5, 1, 3, 2], k = 3

Step 1: Build initial window [2, 1, 5]
  windowSum = 2 + 1 + 5 = 8
  maxSum = 8

Step 2: Slide window to [1, 5, 1]
  windowSum = 8 - 2 + 1 = 7
  maxSum = max(8, 7) = 8

Step 3: Slide window to [5, 1, 3]
  windowSum = 7 - 1 + 3 = 9
  maxSum = max(8, 9) = 9

Step 4: Slide window to [1, 3, 2]
  windowSum = 9 - 5 + 2 = 6
  maxSum = max(9, 6) = 9

Result: 9
Practice Problems
Maximum Average Subarray I (LeetCode #643)

Longest Substring Without Repeating Characters (LeetCode #3)

Minimum Window Substring (LeetCode #76)

Permutation in String (LeetCode #567)

Sliding Window Maximum (LeetCode #239)

