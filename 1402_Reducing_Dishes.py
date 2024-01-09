class Solution(object):
    def maxSatisfaction(self, satisfaction):
        final_result = sum_total = 0 #reset the sum_total and the final result
        satisfaction.sort() # starting with sorting our array
        while satisfaction and satisfaction[-1] + sum_total > 0: # as long as satisfaction is not zero and the last place in satisfaction + sum_total is not negative we will calculate the dishes (like the example with [-8, -9])
            sum_total += satisfaction.pop() # the pop every iteration pop the last value in the array
            final_result += sum_total # every time we pop someone we add the previus value again because it is the last one
        return final_result
        