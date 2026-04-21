# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  
                    stack.append(int(a / b))  
                
            else:
                stack.append(int(token))
        
        return stack[0]


s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
 






        