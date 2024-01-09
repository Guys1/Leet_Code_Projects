@lru_cache(None)
class Solution:
   
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x_point = 0 #init the x coordinate of start point
        start_y_point = 0 #init the y coordinate of start point
        number_of_usful_cells = 0 #counter that counts the number of usful cells
        row = len(grid) #number of rows in the matrix
        col = len(grid[0]) #number of columns in the matrix
        #loop inside a loop because we need to go through every cell in the matrix
        for i in range(0, row):
            for j in range(0, col): 
                cell = grid[i][j] #store the current cell 
                if cell >= 0: #check the cell's option ('1', '2', '0', '-1') and if it's '1' or '2' or '0'
                    number_of_usful_cells += 1 #we need to count it
                if cell == 1: #if the cell is exactly '1' so we know we are at the starting point so
                    start_x_point, start_y_point = i, j #we keep the (i, j) coordinates of start ('1') point
        #after all this begining we use dfs algorithm to find the paths from the start point to the end
        return self.DFSAlgoPath(grid, start_x_point, start_y_point, number_of_usful_cells)
    
    #deepth first search algorithm 
    def DFSAlgoPath(self, grid, x, y, step):
        row = len(grid) #number of rows in the matrix
        col = len(grid[0]) #number of columns in the matrix
        
        if grid[x][y] == 2: #if the cell is '2' so we are at the end point
            return step == 1 #check that the remaining step is one until the end (last step) 
        
        number_of_paths = 0 #counter for number of paths we have
        current_cell = grid[x][y] #save the current cell
        grid[x][y] = -2 #flag to the programmer that if you already passed this cell before
        # pass on each direction we can go
        for point_x, point_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            #update our new possible place to move
            new_x, new_y = x + point_x, y + point_y
            
            if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] >= 0: #if the robot is on valid place first condition is for                                                                                    x second condition is for y, last condition is for the                                                                                    new cell if it's in a valid place  
                number_of_paths += self.DFSAlgoPath(grid, new_x, new_y, step - 1) #step - 1 in the recursive call because we are limited                                                                                    to number of steps and we init it in the begining with                                                                                    the maximum value, and recursive call for the dfs
        grid[x][y] = current_cell #take the current cell back
        return number_of_paths #eventually this is the output.