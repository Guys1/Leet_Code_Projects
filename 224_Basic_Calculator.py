class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1 # starting with positive sign to multiply with positiveor negative number
        stack = [sign]  # stack[-1]: current env's sign

        for c in s:
            if c.isdigit(): # checking if current char can be a nuber (is char == ' ' we ignor it)
                num = num * 10 + (ord(c) - ord('0')) #calc the value as int

            #in case the char is a sign, figuring out which sign is it:

            #handling ')','(' signs with stack
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()

            #if sign is '+' or '-', 
            elif c == '+' or c == '-':
                #summing up and multiplying (1 or -1) num * sign
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0

        return ans + sign * num