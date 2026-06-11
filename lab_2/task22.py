class Solution(object):
    def generateParenthesis(self, n):
        result = []
        stack = [('', 0, 0)]
        while stack:
            s, l, r = stack.pop()
            if len(s) == n * 2:
                result.append(s)
                continue
            if l < n:
                stack.append(( s + '(', l + 1, r))
            if l > r:
                stack.append(( s + ')', l, r + 1))
        return result