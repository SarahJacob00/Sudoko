import pprint



def solve(bo):

    #Solves a sudoko board using backtracking
    #bo:2D list of ints

    find=find_empty(bo) #looks for the empty position
    if find :
        row,col=find
    else:
        return True

    for i in range (1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i

            if solve(bo):
                return True       
            
            bo[row][col]=0

    return False






def valid(bo,num,pos):
    x,y=pos
    #check row
    for j in range (len(bo[0])):        
        if bo[pos[0]][j]==num and pos[1]!=j:
            return False
    #check col
    for j in range (len(bo[0])):        
        if bo[j][pos[1]]==num and pos[0]!=j:
            return False
    #check box
    box_x=y//3
    box_y=x//3

    for i in range (box_y*3,box_y*3+3):
        for j in range (box_x*3,box_x*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True





def find_empty(bo):
    for i in range(len(bo)):
        for j in range (len(bo[0])):
            if bo[i][j]==0:
                return (i,j)

    return False





def print_board(bo):

    for i in range(len(bo)):
        if i%3==0 or i==0 :
            print("--------------------")

        for j in range(len(bo[0])):
            if j%3==0 or j==0:
                print("|",end="")

            if j==8:
                print(bo[i][j],"|")
               
            else:
                print(str(bo[i][j])+" ",end="")
        if i==len(bo)-1:
            print("---------------------")





if __name__=="__main__":    
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    print('Initial Board:')
    print_board(board)
    solve(board)
    print('Final Board:')
    print_board(board)






