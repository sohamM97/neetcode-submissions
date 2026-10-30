class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows

        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])

        # columns

        for j in range(9):
            nums = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])

        # grids
        for grid_i in range(3):
            for grid_j in range(3):
                nums = set()

                for i in range(grid_i*3, grid_i*3 + 3):
                    for j in range(grid_j*3, grid_j*3 + 3):
                        if board[i][j] != ".":
                            if board[i][j] in nums:
                                return False
                            nums.add(board[i][j])

        return True
        