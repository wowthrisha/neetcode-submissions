class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=defaultdict(set)
        row=defaultdict(set)
        s=defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in s[(r//3,c//3)]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                s[(r//3,c//3)].add(board[r][c])
        return True