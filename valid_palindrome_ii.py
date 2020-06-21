"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""
class Solution:
    def validPalindrome(self, s):
        first = 0 
        last = len(s)-1
        while first < last:
            if s[first] == s[last]:
                first+=1
                last-=1
            else:
                return self.isPalindrome(s,first,last-1) or self.isPalindrome(s,first+1,last)
                
        return True
    
    def isPalindrome(self,s,first,last):
        while first < last:
            if s[first] == s[last]:
                first+=1
                last-=1
            else:
                return False
        return True
        
