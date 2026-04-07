class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l=[]  
        count=0
        
        for row in board:
            new_row=[int(i) for i in row if i.isdigit()]
            if sorted(new_row)!=sorted(set(new_row)):
                count+=1
        
        for j in range(len(board)):   
            l.append([i[j] for i in board])
        
        for column in l:
            new_column=[int(i) for i in column if i.isdigit()] 
            if sorted(new_column)!=sorted(set(new_column)):
                count+=1
        
        l1=[board[i][j] for i in range(3) for j in range(3) if board[i][j].isdigit()] 
        l2=[board[i][j] for i in range(3,6) for j in range(3) if board[i][j].isdigit()] 
        l3=[board[i][j] for i in range(6,9) for j in range(3) if board[i][j].isdigit()] 
        l4=[board[i][j] for i in range(3) for j in range(3,6) if board[i][j].isdigit()] 
        l5=[board[i][j] for i in range(3,6) for j in range(3,6) if board[i][j].isdigit()]  
        l6=[board[i][j] for i in range(6,9) for j in range(3,6) if board[i][j].isdigit()] 
        l7=[board[i][j] for i in range(3) for j in range(6,9) if board[i][j].isdigit()] 
        l8=[board[i][j] for i in range(3,6) for j in range(6,9) if board[i][j].isdigit()] 
        l9=[board[i][j] for i in range(6,9) for j in range(6,9) if board[i][j].isdigit()] 
        
        matrix=[l1,l2,l3,l4,l5,l6,l7,l8,l9]
        print("matrix:",matrix)
        for j in matrix:
            new_matrix=[int(i) for i in j]
            if sorted(new_matrix)!=sorted(set(new_matrix)):
             count+=1
        if count==0:
            return(True)
        else:
            return(False)        