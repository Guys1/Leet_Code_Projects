class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings) #number of kids
        kids_candies = [1] * n #eveery kid has one candy so it's a list for each kid
        #loop that passes on every kid
        for kid in range(1, n):
            if ratings[kid] > ratings[kid-1]: #if the current is bigger than the left neighbor
                kids_candies[kid] = kids_candies[kid-1] + 1 #add one to the current from the left kid amount
        #loop for from right to left scan so that is why the -1, -1 
        for kid in range(n-2, -1, -1):
            #we already have some numbers in our kids_candies
            if ratings[kid] > ratings[kid+1]: #check the current with the right kid
                kids_candies[kid] = max(kids_candies[kid], kids_candies[kid+1] + 1) #the current kid has the maximum from his place or his right kid                                                                                      plus one because he has to be bigger, it's or to keep him with                                                                                        the same amount of candies or to give him one more candy from                                                                                        his right kid
        total_amount_of_candies = sum(kids_candies) #sum the total amount of candies
        return(total_amount_of_candies)  
            