"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


"""

class Solution:
    def decodeWays(self,st):
        ls = len(st)
        temp = [0]*(ls+1)
        temp[0] = 1
        temp[1] = 1 if int(st[0]) != 0 else 0
        for i in range(2,ls+1):
            oneletter = int(st[i-1:i])
            twoletter = int(st[i-2:i]) 
            if oneletter > 0:
                temp[i] += temp[i-1]
            if twoletter >=10 and twoletter <=26:
                temp[i] += temp[i-2]
        return temp[ls]








if __name__  == '__main__':
    sol = Solution()
    ex1 = "12"
    assert sol.decodeWays(ex1) == 2
    ex2 = "226"
    assert sol.decodeWays(ex2) == 3
    ex3 = '4532'
    assert sol.decodeWays(ex3) == 1
