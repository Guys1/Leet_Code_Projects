from functools import cmp_to_key

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        #need to compare between two plans about their "plantTime" + "growTime"
        #plant_A is a touple and plant_B is also a touple
        def ComparePlantsDays(plant_A, plant_B):
            plantTime_A, growTime_A = plant_A #plantTime_A gets the left value, growTime_A the right value
            plantTime_B, growTime_B = plant_B #plantTime_B gets the left value, growTime_B the right value
            
            #number_of_days is the best number of days to plant the plants
            #we calculate the time it will take to plant two plants according to the rules in the question
            #like: no plants two plants in the same day so this calculation does that.
            A = (plantTime_A + max(plantTime_B + growTime_B, growTime_A))
            B = (plantTime_B + max(plantTime_A + growTime_A, growTime_B))
            number_of_days =  A - B #minus between touples -> because we want the difference and that is the number_of_days
                                            
            return number_of_days
        
        data_of_each_plant = list(zip(plantTime, growTime)) #split each plant to touple and put all plants in a list of touples. the left                                                              value is plantTime and the right value is the growTime
                                                                
        #print(data_of_each_plant)
        data_of_each_plant.sort(key=cmp_to_key(ComparePlantsDays)) #we sort our list according to the ComparePlantsDays function and that                                                                     is why we using the functools -> cmp_to_key, this value uses a key to compare elements and we sort it by that.
                                                                    #the key it will use is the number_of_days, each time it will check                                                                                                                    two touples from the list.
        
        last_day = 0    #last_day is the last day we have in our timeline
        current_day = 0 #current_day is our current day we are now and what we planning to do 
        
        for plantT,growT in data_of_each_plant: #two indexs because it is a for on a touple
            last_day = max(last_day, plantT + growT + current_day) #calculate the last day we have arrived and it will always be the max                                                                     between the last itself or the plantT + growT + current_day
            current_day += plantT #and we calculate the current_day as the current plus the relevant plantT
            
        return last_day