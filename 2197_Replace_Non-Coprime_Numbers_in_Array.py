class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = [] 
        #non-coprime == GCD(x,y) > 1
        for num in nums: 
            while ans and gcd(ans[-1], num) > 1: #if num and corrent candidate are non-coprime
                num = lcm(ans.pop(), num) #delete the two numbers and replace them with their LCM
            ans.append(num) #pushing to stack 'ans' the new numbers as LCM

        return ans