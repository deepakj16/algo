"""
10. Overlapping Intervals

This pattern handles problems involving intervals that may overlap. The key insight is that after sorting by start time, two intervals [a, b] and [c, d] overlap if b >= c.

When to use
Merging overlapping intervals

Finding interval intersections

Scheduling problems (meeting rooms)

Inserting into sorted intervals

Template
// Sort by start time
Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

// Merge overlapping intervals
List<int[]> merged = new ArrayList<>();
for (int[] interval : intervals) {
    if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < interval[0]) {
        // no overlap, add new interval
        merged.add(interval);
    } else {
        // overlap, merge by extending end time
        merged.get(merged.size() - 1)[1] =
            Math.max(merged.get(merged.size() - 1)[1], interval[1]);
    }
}
Sample Problem
Merge Intervals: Given a collection of intervals, merge all overlapping intervals.

Example:
Input: intervals = [[1,3], [2,6], [8,10], [15,18]]

Output: [[1,6], [8,10], [15,18]]

Step-by-Step Walkthrough:
intervals = [[1,3], [2,6], [8,10], [15,18]]
(Already sorted by start time)

Step 1: interval = [1,3]
  merged is empty, add [1,3]
  merged = [[1,3]]

Step 2: interval = [2,6]
  last = [1,3], start = 2 <= end = 3
  Overlap! Merge: end = max(3, 6) = 6
  merged = [[1,6]]

Step 3: interval = [8,10]
  last = [1,6], start = 8 > end = 6
  No overlap, add [8,10]
  merged = [[1,6], [8,10]]

Step 4: interval = [15,18]
  last = [8,10], start = 15 > end = 10
  No overlap, add [15,18]
  merged = [[1,6], [8,10], [15,18]]
Practice Problems
Merge Intervals (LeetCode #56)

Insert Interval (LeetCode #57)

Non-overlapping Intervals (LeetCode #435)

Meeting Rooms (LeetCode #252)

Meeting Rooms II (LeetCode #253)
"""
