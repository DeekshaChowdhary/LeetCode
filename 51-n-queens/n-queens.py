class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backtrack(row):
            if row == n:
                # If all queens are placed, convert board to result format
                solution = ["".join(board[i]) for i in range(n)]
                results.append(solution)
                return
            
            for col in range(n):
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue  # Skip invalid placements
                
                # Place the queen
                board[row][col] = 'Q'
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                
                # Recurse to the next row
                backtrack(row + 1)
                
                # Backtrack: Remove the queen
                board[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
        
        results = []
        board = [["." for _ in range(n)] for _ in range(n)]
        cols = set()  # Tracks used columns
        diagonals = set()  # Tracks used \ diagonals (row - col)
        anti_diagonals = set()  # Tracks used / diagonals (row + col)
        
        backtrack(0)
        return results
