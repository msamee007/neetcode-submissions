class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[[] for i in range(9)]
        l=[[]for i in range(9)]
        for i in range(9):
            s=[]
            for j in range(9):
                if board[i][j]=='.':
                    continue
                boxId = (i // 3) * 3 + (j // 3)
                if board[i][j] in l[boxId]:
                     return False
                l[boxId].append(board[i][j])
                r[j].append(board[i][j])
                s.append(board[i][j])
            if len(set(s))!=len(s):
                return False
        for i in r:
            if len(set(i))!=len(i):
                return False
        return True
            
        
        