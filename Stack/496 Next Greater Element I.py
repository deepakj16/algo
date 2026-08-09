"""
496. Next Greater Element I
Easy
Topics
premium lock icon
Companies
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """ 
        op = [-1] * len(nums1)
       
        print(nums1, nums2)
        for i in range(0,len(nums1)):
            print('i ' + str(nums1[i]))
            j = nums2.index(nums1[i])
            print('j ' + str(j))
            for k in range(j,len(nums2)):
                print('k ' + str(k))
                if nums2[k]>nums1[i]:
                    op[i] = nums2[k]
                    break
        return op
        """

        stack = []
        mp = {}

        for i in range(0, len(nums2)):
            while stack and nums2[i] >  nums2[stack[-1]]:
                mp[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
        op = []
        for n in nums1:
            if n in mp.keys():
                op.append(mp[n])
            else:
                op.append(-1)
        return op








        """
        op = [-1] * len(nums1)
        stack = []
        mpp = {}

        for i in range(0, len(nums2)):
            while stack and nums2[i]> nums2[stack[-1]]:
                mpp[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        print(mpp)
        for i in range(0, len(nums1)):
            print(nums1[i])
            print(mpp.keys())
            #print(mpp[nums1[i]])
            if nums1[i] in mpp.keys():
                print(mpp[nums1[i]])
                op[i] = mpp[nums1[i]]
            else:
                op[i] = -1

        return op
        """




