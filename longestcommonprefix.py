"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""







class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return result
        result = strs[0]
        for sd in strs:
            for i in range(len(result)):
                if i>=len(sd) or result[i] != sd[i]:
                    #print("hi")
                    result = result[:i]
                    break
                    
        return result
