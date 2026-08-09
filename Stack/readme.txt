7. Monotonic Stack

A Monotonic Stack maintains elements in either increasing or decreasing order. As you iterate, you pop elements that violate the order, which reveals relationships between elements.

When to use
Finding the next greater/smaller element

Finding previous greater/smaller element

Problems involving spans or ranges

Histogram problems

Template
/// Next Greater Element (decreasing stack)
int[] result = new int[n];
Arrays.fill(result, -1);
Stack<Integer> stack = new Stack<>(); // stores indices

for (int i = 0; i < n; i++) {
    while (!stack.isEmpty() && nums[i] > nums[stack.peek()]) {
        int idx = stack.pop();
        result[idx] = nums[i];
    }
    stack.push(i);
}
Sample Problem
Next Greater Element: For each element in an array, find the next greater element. Output -1 if none exists.

Example:
Input: nums = [2, 1, 2, 4, 3]

Output: [4, 2, 4, -1, -1]

Step-by-Step Walkthrough:
nums = [2, 1, 2, 4, 3]
result = [-1, -1, -1, -1, -1]
stack = []

Step 1: i = 0, nums[0] = 2
  stack is empty, push 0
  stack = [0]

Step 2: i = 1, nums[1] = 1
  1 < nums[0]=2, push 1
  stack = [0, 1]

Step 3: i = 2, nums[2] = 2
  2 > nums[1]=1, pop 1, result[1] = 2
  2 <= nums[0]=2, push 2
  stack = [0, 2], result = [-1, 2, -1, -1, -1]

Step 4: i = 3, nums[3] = 4
  4 > nums[2]=2, pop 2, result[2] = 4
  4 > nums[0]=2, pop 0, result[0] = 4
  push 3
  stack = [3], result = [4, 2, 4, -1, -1]

Step 5: i = 4, nums[4] = 3
  3 < nums[3]=4, push 4
  stack = [3, 4]

Result: [4, 2, 4, -1, -1]
Practice Problems
Next Greater Element I (LeetCode #496)

Daily Temperatures (LeetCode #739)

Largest Rectangle in Histogram (LeetCode #84)

Trapping Rain Water (LeetCode #42)

Online Stock Span (LeetCode #901)

