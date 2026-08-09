"""
347. Top K Frequent Elements
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ct = Counter(nums)
        print(ct)
        hp = []
        for k1, v in ct.items():
            heapq.heappush(hp, [v, k1])
            print(hp)
            if len(hp)>k:
                heapq.heappop(hp)
                print(hp)

        return [i[1] for i in hp]
        


        '''
        counter_d = Counter(nums)
        print(counter_d)
        heap = []
        for kv, v in counter_d.items():
            heapq.heappush(heap,(v,kv))
            print(len(heap), k)
            if len(heap)>k:
                print('if loop')
                heapq.heappop(heap)
                print(heap)
        print(heap)
        op = []
        for i in heap:
            op.append(i[1])
        print(op)
        return op
        '''
        
