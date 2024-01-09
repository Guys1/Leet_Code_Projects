class Solution:
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        number_of_rows = len(grid) #number of rows in the grid
        number_of_columns = len(grid[0]) #number of columns in the grid
        sum = 0 #sum the number of cherries in total
        @lru_cache(None)
        def HelpCalcCherries(row:int, col_1:int, col_2:int) -> int:
            temp = 0
            #count number of cherries
            number_of_cherries = grid[row][col_1]
            if col_1 != col_2:
                number_of_cherries += grid[row][col_2]
            # stop condition for the recursion function    
            if row == number_of_rows - 1:
                return number_of_cherries
            #checking all 9 combinations for both robots
            # (DL, D, DR) -> 3 possabilities for each robot 
            for move_1 in (col_1 - 1, col_1 + 1, col_1):
                for move_2 in (col_2 - 1, col_2 + 1, col_2):
                    if move_1 >= 0 and move_2 >= 0 and move_1 < number_of_columns and move_2 < number_of_columns:
                        # if we came so far we are in a good cell
                        temp = max(temp, HelpCalcCherries(row + 1, move_1, move_2))
            return temp + number_of_cherries
        sum = HelpCalcCherries(0,0, number_of_columns - 1)
        return sum