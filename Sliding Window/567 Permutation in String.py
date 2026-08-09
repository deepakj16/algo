"""
567. Permutation in String
Medium
Topics
premium lock icon
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = set(list(s1))
        s2 = list(s2)
        i=0
        l=len(list(s1))
        s2_set = set(s2[:l])
        while i+l<len(s2):
            if s1==s2_set:
                return True
            else:
                s2_set.remove(s2[i])
                s2_set.add(s2[i+l])
                i+=1
        return False
            

        
