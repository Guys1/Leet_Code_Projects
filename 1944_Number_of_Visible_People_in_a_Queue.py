class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = [] #creating a stack (implemented by a list)
        n = len(heights) #length of all the heights we got
        result = [0] * n  # array that contains n zeros for eventually the result
        # print(result)
        for i in range(n - 1, -1, -1): #a loop from n-1 until -1 (not included) decrementing -1 each iteration
            count_per_minion = 0
            #as long as stack is not empty and the current height minion is taller than his right friend 
            while (stack) and heights[i] > stack[-1]:
                stack.pop() #than the friend is not relevant so we pop it out
                count_per_minion += 1 #increase total
            #this is to count the person who is higher than the current
            if stack: #if the stack is not empty (stack!=0)
                count_per_minion += 1 #increase count_per_minion by one 
 
            stack.append(heights[i]) #add to stack the current height according to the terms
            result[i] = count_per_minion #add each count for each minion to the result array

        return result