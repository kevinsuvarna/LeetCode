class Solution(object):
    def gridExtractor(self, board, num):
        x1 = (num - 1) // 3 * 3
        y1 = (num - 1) % 3 * 3
        x2 = x1 + 2
        y2 = y1 + 2
        check = [False] * 10
        for i in range(x1, x2+1):
            for j in range (y1, y2+1):
                if board[i][j] != '.':
                    if check[int(board[i][j])]:
                        return False
                    else:
                        check[int(board[i][j])] = True
        return True
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check = [False] * 10
        # check rows
        for i in range(9):
            check = [False] * 10
            row = board[i]
            for j in range(9):
                if row[j] != '.':
                    if check[int(row[j])]:
                        return False
                    else:
                        check[int(row[j])] = True
        for i in range(9):
            check = [False] * 10
            for j in range(9):
                if board[j][i] != '.':
                    if check[int(board[j][i])]:
                        return False
                    else:
                        check[int(board[j][i])] = True

        for i in range(1,10):
            isValid = self.gridExtractor(board, i)
            if not isValid:
                return isValid
                        
        return True