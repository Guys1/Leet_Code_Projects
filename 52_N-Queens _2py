class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        def dfs(row:int, wrong_cell:set):
            nonlocal result
            if row < n:
                for col in range(n):
                    if (row, col) in wrong_cell:
                        continue
                    ex_sub = set()
                    row1, row2, row3 = row, row, row
                    col1, col2, col3 = col, col, col
                    
                    while row1 < n:
                        row1 += 1
                        ex_sub.add((row1, col1))
                    while col2 < n:
                        col2 += 1
                        row2 += 1
                        ex_sub.add((row2, col2))
                    while col3 > 0:
                        col3 -= 1
                        row3 += 1
                        ex_sub.add((row3, col3))
                    dfs(row + 1, wrong_cell | ex_sub)
            else:
                result += 1
        dfs(0, set())
        return result