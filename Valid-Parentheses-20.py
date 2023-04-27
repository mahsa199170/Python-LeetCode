class Solution(object):
    def isValid(self, s):
        stack = []
        check = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in check:
                if stack and stack[-1] == check(c):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False



# time complexity O(n)
#memory complexity O(n)