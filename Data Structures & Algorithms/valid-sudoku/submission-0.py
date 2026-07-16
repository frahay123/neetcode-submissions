class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #validate row
        for i in range(9):
            s = set()
            for j in range(9):
                letter = board[i][j]
                if letter in s:
                    return False
                elif letter != '.':
                    s.add(letter)
        

        # validate column
        for i in range(9):
            s = set()
            for j in range(9):
                letter = board[j][i]
                if letter in s:
                    return False
                elif letter != '.':
                    s.add(letter)
        
        # validate boxes
        starts = [(0,0),(0,3),(0,6),
                    (3,0),(3,3),(3,6),
                    (6,0),(6,3),(6,6)]
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j,j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True


        

        