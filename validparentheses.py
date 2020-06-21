"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


"""



class Solution:
    def isValid(self, s):
        firstbrackets = ["(","{","["]
        endbrackets = [")","}","]"] 
        stack = []
        if not s:
            return True
        for x in s:
            if x in firstbrackets:
                stack.append(x)
            if x in endbrackets:
                bracket_place = endbrackets.index(x)
                if len(stack) > 0 and stack.pop() == firstbrackets[bracket_place]:
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
