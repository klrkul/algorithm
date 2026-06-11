class Solution(object):
    def evalRPN(self, tokens):
        stack =[]
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                b=stack.pop()
                a=stack.pop()
                if t == '+':
                    stack.append(a+b)
                if t == '-':
                    stack.append(a-b)
                if t == '/':
                    if b!=0:
                        stack.append(int(float(a) / b))
                if t == '*':
                    stack.append(a*b)
        return stack[0]