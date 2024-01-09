class Solution:
    def longestValidParentheses(self, s: str) -> int:
            count = 0
            stack = [-1]
            for i, char in enumerate(s):
                if char == '(':
                    #save previous streak 
                    stack.append(i)
                elif char == ')':
                    #poping from stack if
                    if len(stack)>1 and s[stack[-1]] == '(':
                        stack.pop()
                        #saving streak
                        count = max(count,(i-stack[-1]))
                    else:
                        #invalid parenthesis
                        stack.append(i)

            return count