class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {'+', '-', '*', '/'}
        stack = []
        n = len(tokens)
        
        def cal(v1, v2, op):
            if op == '+':
                return v1 + v2
            elif op == '-':
                return v1 - v2
            elif op == '*':
                return v1 * v2
            else:
                return int(v1 / v2) # Python2 is wired
        
        for i in range(n):
            if tokens[i] in operators:
                p_right = stack.pop()
                p_left = stack.pop()
                stack.append(cal(int(p_left), int(p_right), tokens[i]))
            else:   
                stack.append(tokens[i])
        return stack[0]
    
    
    
solution = Solution()
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

# T:O(n)
# S:O(n)