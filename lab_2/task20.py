class Solution(object):
    def isValid(self, s):
        a = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in a:
                if not stack or stack[-1] != a[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0