"""
901. Online Stock Span
Solved
Medium
Topics
premium lock icon
Companies
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 

Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
 

Constraints:

1 <= price <= 105
At most 104 calls will be made to next.
"""


from collections import defaultdict
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
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
        """ Dry run
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




        
