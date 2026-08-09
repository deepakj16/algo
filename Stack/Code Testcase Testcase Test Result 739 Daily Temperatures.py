"""
739. Daily Temperatures
Attempted
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

""""
from collections import defaultdict
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while stack and temperatures[i]> temperatures[stack[-1]]:
                j = stack.pop()
                result[j]= i-j
            stack.append(i)
            print(temperatures[i])
            print(stack)
            print(result)

        return result





        """

        stack = []
        result = [0] * len(temperatures)
        map = defaultdict(int) 
        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                result[stack.pop()] = map[stack[-1]]
            print('after while')
            print(i, stack, result, map)
            stack.append(i)
            map[i] = 0
            for m in map.keys():
                map[m] += 1
            print('after stack and map')
            print(i, stack, result, map)
        return result
        """
        """ 
        Dry run
        [73,74,75,71,69,72,76,73]
        i = 0 , v = 73, while fails, results - no chnage, stack = [0], 0:1
        i=1,v=74, while passes 74>73,  results - [1,0,0,0,0,0,0,0], stack=[1], 1:1
        i=2, v=75 while passes 75>74, results - [1,1,0,0,0,0,0,0], stack=[2], 2:1
        i=3, v=71 while fails 71>75, results  - no chnage, stack=[2, 3], 2:2, 3:1
        i=4, v=69 while fails 69>71, results  - no chnage, stack=[2, 3, 4], 2:3, 3:2, 4:1
        i=5, v=72 while passes 72>69, results  - [1,1,0,0,1,0,0,0] , stack=[2, 3], 2:3, 3:2
        i=5, v=72 ,while passes 72>71, results - [1,1,0,2,1,0,0,0] , stack = [2], 2:3
        i=5, v=72 ,while fails 72>75, results - no change, stack = [2, 5], 2:4, 5:1
        i=6, v=76, while passes 76>72 results - [1,1,0,2,1,1,0,0], stack = [2], 2:4
        i=6, v=76, while passes 76>75 results - [1,1,4,2,1,1,0,0], stack =[], {}, stack = [6], 6:1
        i=7, v=73, while fails 73>76  results - [1,1,4,2,1,1,0,0], stack = [6,7], 6:2, 7:1

        """




        



