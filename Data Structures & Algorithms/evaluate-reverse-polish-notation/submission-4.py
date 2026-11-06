class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def op(x,y,o):
            if o == "+":
                return x+y
            elif o == "-":
                return y-x
            elif o =="*":
                return x*y
            elif o == "/":
                return y/x
        arth = "*+-/"
        stack = []
        result = 0
        for t in tokens:
            if t in arth:
                val1 = stack.pop()
                val2 = stack.pop()
                result = op(val1,val2,t)
                stack.append(int(result))
            else:
                stack.append(int(t))
        p = stack.pop()
        return p