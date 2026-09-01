class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for j in range(9)]
        boxes = [set() for k in range(9)]
        for i in range(9):
            for j in range(9):
                box_index = (i//3) * 3 + (j//3)
                if board[i][j] == '.':
                    continue
                elif board[i][j] in rows[i] :
                    return False
                elif board[i][j] in cols[j] :
                    return False
                elif board[i][j] in boxes[box_index] :
                    return False
                else :
                    rows[i].add(str(board[i][j]))
                    cols[j].add(str(board[i][j]))
                    boxes[box_index].add(str(board[i][j]))
        return True


        